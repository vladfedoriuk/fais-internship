from utils.db import ConfTableFactory, engine, DB, Files, tables_query, EXCLUDE, Table
from utils.time import convert_datetime, r_time_patterns, validate_date
from datetime import datetime
from sqlalchemy.sql import select, join
from functools import reduce, cached_property
import pandas
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Set, Tuple, Optional, Dict, NamedTuple
from sqlalchemy.sql.selectable import Select, Join
import argparse
import logging
import sys

parser = argparse.ArgumentParser()
connection = engine.connect()
factory = ConfTableFactory()


@dataclass(eq=True, frozen=True, unsafe_hash=True)
class SearchDetails:
    valid_from: datetime
    valid_to: datetime
    version: int
    
    def to_tuple(self):
        return tuple(x for x in self.__dict__.values())
    

@dataclass(eq=True, frozen=True, unsafe_hash=True)
class VersionDetails(SearchDetails):
    remarks: Optional[str]
    

class Parameter(ABC): 
       
    def _select(self, table: Table)-> Select:
        return select(
            table.c.valid_from, 
            table.c.valid_to, 
            table.c.version, 
            table.c.remarks
        )
    
    @abstractmethod
    def where(self, table: Table) -> Select:
        ...
 

@dataclass 
class DateTimes(Parameter):   
    param: Tuple[datetime, datetime]
    
    def where(self, table: Table) -> Select:
        return super(DateTimes, self)._select(table).\
            where(table.c.valid_from <= self.param[0], \
                table.c.valid_to >= self.param[1]
            )  
        
@dataclass    
class Run(Parameter):
    param: int
    
    def _join(self, table: Table) -> Join:
        return join(
            Files, table, 
            (Files.c.start_time >= table.c.valid_from) & \
                (Files.c.stop_time <= table.c.valid_to)
        )
        
    def where(self, table: Table) -> Select:
       return super(Run, self)._select(table).\
            select_from(self._join(table)).\
                where(Files.c.run_id == self.param)
     
        
@dataclass        
class FileName(Run):
    param: str
    
    def where(self, table: Table) -> Select:
        return super(FileName, self)._select(table).\
            select_from(super(FileName, self)._join(table)).\
                where(Files.c.file_name == self.param)
    
    
class Extractor(object):
    
    @cached_property
    def tables(self) -> Dict[str, Table]:
        table_names = connection.execute(tables_query)
        tables_dict = {}
        for table_name in table_names:
            if not any(re.match(x, table_name[0]) for x in EXCLUDE):
                tables_dict[table_name[0]] = factory(table_name[0])
        return tables_dict
    
    @staticmethod
    def __get_df(versions: Set[VersionDetails]) -> pandas.DataFrame:
        available_versions = reduce(lambda s1, s2: s1 & s2, versions.values())
        available_versions = list(map(lambda x: x.to_tuple(), available_versions))
    
        df = pandas.DataFrame(
            data=available_versions, 
            index=range(len(available_versions)),
            columns=['VALID_FROM', 'VALID_TO', 'VERSION', 'REMARKS']
        )
        df.index.name = 'ID'
        df['REMARKS'] = df['REMARKS'].apply(lambda x: None if x == '' else x)
        return df  
    
    def process(self, param: Parameter) -> pandas.DataFrame:
        if not isinstance(param, Parameter):
            raise ValueError(f'{param} is not an instance of the subclass of {Parameter}')
        versions = {}
        for table_name, table in self.tables.items():
            s = param.where(table)
            results = connection.execute(s).fetchall()
            versions[table_name] = frozenset(
                VersionDetails(*res) for res in results
            )
        return self.__get_df(versions)
    
    @staticmethod
    def version_exists(df: pandas.DataFrame, version: int) -> bool:
        version = df.loc[df['VERSION']==version]
        return not version.empty
    
    @staticmethod
    def filter_by_version(df: pandas.DataFrame, version: int) -> pandas.DataFrame:
        return  df.loc[df['VERSION']==version]
    
    @staticmethod
    def convert_datetimes(df: pandas.DataFrame) -> pandas.DataFrame:
        df['VALID_FROM'] = df['VALID_FROM'].apply(convert_datetime)
        df['VALID_TO'] = df['VALID_TO'].apply(convert_datetime)
        return df
    
    def write_to_file(self, details: SearchDetails, filename: str = None) -> str:
        valid_from, valid_to, version = details.to_tuple()
        if not filename:
            filename = f"conf-{valid_from}-{valid_to}-v-{version}"
        with open(filename, 'w') as conf:
            for table_name, table in self.tables.items():
                conf.write(f'[{table_name}]\n')
                query = select(table.c.parameters).where(
                    table.c.valid_from <= valid_from,
                    table.c.valid_to >= valid_to,
                    table.c.version == version
                )
                result = connection.execute(query).fetchone()
                if result:
                    result = result[0]
                    conf.write(result + '\n\n')
        return filename

if __name__ == '__main__':
    
    parser.add_argument("--validfrom", "-vf", 
                        help=f'The date the configuration is valid from {r_time_patterns}')
    parser.add_argument("--validto", "-vt",
                        help=f'The date the configuration is valid to {r_time_patterns}')
    parser.add_argument('-v', '--version', 
                        help='The version of the configurations', type=int)
    parser.add_argument('-n', '--name',
                        help='The name of the output file')
    parser.add_argument('-r', '--run', 
                        help="The run id to extract datetimes from", type=int)
    parser.add_argument('-f', '--file', 
                        help="The run file name to extract datetimes from")
    
    args = parser.parse_args()
    extractor = Extractor()
    
    if args.validfrom is not None and args.validto is not None:
        valid_from = validate_date(args.validfrom, 'validfrom')
        valid_to = validate_date(args.validto, 'validto')
        param = DateTimes((valid_from, valid_to))
        
    elif args.run is not None:
        try:
            run = int(args.run)
            if run < 0:
                raise ValueError()
        except:
            logging.error(f'run must be a positive integer, got {args.run} instead.')
            sys.exit()
        param = Run(run)
    
    elif args.file is not None:
        param = FileName(args.file)
    
    available_versions = extractor.process(param)
    version = None
    version_exists = True
    versions_table = None
    if args.version:
        try:
            version = int(args.version)
            if version < 1:
                raise ValueError()
        except:
            logging.error(
                f'version must be a positive integer greater than 1, got {args.version} instead.')
            sys.exit()

        version_exists = extractor.version_exists(available_versions, version)
        if version_exists:
            versions_table = extractor.filter_by_version(available_versions, version)
    if not args.version or not version_exists:
        version_exists = False
        versions_table = available_versions
    
    versions_table = extractor.convert_datetimes(versions_table)
    if not version_exists:
        logging.warning('There was no version provided or the provided version does not exist')
        
    print(versions_table)
    idx = input('provide an ID of desired configuration: ')
    
    try:
        idx = int(idx)
        if not idx in versions_table.index:
            raise ValueError()
    except ValueError:
        logging.error(
            f'The index must be present in the table above, got {idx} instead')
        sys.exit()
        
    des_version = versions_table.iloc[idx]
    details = SearchDetails(
        des_version['VALID_FROM'],
        des_version['VALID_TO'],
        des_version['VERSION']
    )
    extractor.write_to_file(details, args.name)
    
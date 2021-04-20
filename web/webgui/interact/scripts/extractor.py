from .utils.db import ConfTableFactory, engine, DB, Files, tables_query, EXCLUDE, Table
from .utils.time import convert_datetime
from datetime import datetime
from sqlalchemy.sql import select, join
from functools import reduce
import pandas
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Set, Tuple, Optional, Dict, NamedTuple
from sqlalchemy.sql.selectable import Select, Join

connection = engine.connect()

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
    
    
factory = ConfTableFactory()

class Extractor(object):
    
    @property
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
    
    def write_to_file(self, details: SearchDetails) -> str:
        valid_from, valid_to, version = details.to_tuple()
        filename = f"./interact/files/extracted/{valid_from}-{valid_to}-v-{version}"
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
    
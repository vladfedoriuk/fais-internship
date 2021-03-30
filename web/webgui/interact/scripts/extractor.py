from .utils.db import ConfTableFactory, engine, DB, Files, tables_query, EXCLUDE, Table
from datetime import datetime
from sqlalchemy.sql import select, join
from functools import reduce, cached_property
import pandas
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Set, Tuple, Optional, Dict
from sqlalchemy.sql.selectable import Select, Join


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
    
    
connection = engine.connect()
factory = ConfTableFactory()

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
    def __get_df(versions: Set[Tuple[datetime, datetime, int, Optional[str]]]) \
        -> pandas.DataFrame:
        available_versions = reduce(lambda s1, s2: s1 & s2, versions.values())
        available_versions = list(available_versions)
    
        df = pandas.DataFrame(
            data=available_versions, 
            index=range(len(available_versions)),
            columns=['VALID_FROM', 'VALID_TO', 'VERSION', 'REMARKS']
        )
        df.index.name = 'ID'
        return df  
    
    def process(self, param: Parameter) -> pandas.DataFrame:
        if not isinstance(param, Parameter):
            raise ValueError(f'{param} is not an instance of the subclass of {Parameter}')
        versions = {}
        for table_name, table in self.tables.items():
            s = param.where(table)
            results = connection.execute(s).fetchall()
            versions[table_name] = frozenset(
                res for res in results
            )
        return self.__get_df(versions)
    
    def params_for_version(self, df: pandas.DataFrame, version: int)\
        -> Optional[Tuple[datetime, datetime, int]]:
        version = df.loc[df['VERSION']==version]
        if not version.empty:
            idx = version.index
            valid_from = df.loc[idx, 'VALID_FROM'].values[0]
            valid_to = df.loc[idx, 'VALID_TO'].values[0]
            version = df.loc[idx, 'VERSION'].values[0]
            return valid_from, valid_to, version
    
    def write_to_file(self, valid_from: datetime, valid_to: datetime, version: int) -> str:
        valid_from = datetime.utcfromtimestamp(valid_from.tolist()/1e9)
        valid_to = datetime.utcfromtimestamp(valid_to.tolist()/1e9)
        filename = f"./interact/configuration_files/{valid_from}-{valid_to}-v-{version}"
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
    
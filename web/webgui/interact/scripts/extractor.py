from .utils.db import ConfTableFactory, engine, DB, Files, tables_query, EXCLUDE
from datetime import datetime
from sqlalchemy.sql import select, join
from functools import reduce, cached_property
import pandas
import re

connection = engine.connect()
factory = ConfTableFactory()

class Extractor(object):
    
    @cached_property
    def tables(self):
        table_names = connection.execute(tables_query)
        tables_dict = {}
        for table_name in table_names:
            if not any(re.match(x, table_name[0]) for x in EXCLUDE):
                tables_dict[table_name[0]] = factory(table_name[0])
        return tables_dict
    
    @staticmethod
    def __get_df(versions):
        available_versions = reduce(lambda s1, s2: s1 & s2, versions.values())
        available_versions = list(available_versions)
    
        df = pandas.DataFrame(
            data=available_versions, 
            index=range(len(available_versions)),
            columns=['VALID_FROM', 'VALID_TO', 'VERSION', 'REMARKS']
        )
        df.index.name = 'ID'
        
        return df  

    def process_run(self, run=None, filename=None):
        if not (filename or run):
            raise ValueError('Have got no information about the run.')
        versions = {}
        for table_name, table in self.tables.items():
            j = join(
                Files, table, 
                (Files.c.start_time >= table.c.valid_from) & \
                    (Files.c.stop_time <= table.c.valid_to)
            )
            if run:
                s = select(
                    table.c.valid_from, 
                    table.c.valid_to, 
                    table.c.version, 
                    table.c.remarks
                ).select_from(j).where(Files.c.run_id == run)
            else:
                s = select(
                    table.c.valid_from, 
                    table.c.valid_to, 
                    table.c.version, 
                    table.c.remarks
                ).select_from(j).where(Files.c.file_name == filename)
            
            results = connection.execute(s).fetchall()
            versions[table_name] = frozenset(
                res for res in results
            )
        return self.__get_df(versions)
    
    def params_for_version(self, df, version):
        version = df.loc[df['VERSION']==version]
        if not version.empty:
            idx = version.index
            valid_from = df.loc[idx, 'VALID_FROM'].values[0]
            valid_to = df.loc[idx, 'VALID_TO'].values[0]
            version = df.loc[idx, 'VERSION'].values[0]
            return valid_from, valid_to, version
 
    def process_dates(self, valid_from, valid_to):
        versions = {}
        for table_name, table in self.tables.items():
            query = select(table.c.valid_from, table.c.valid_to, \
                table.c.version, table.c.remarks)\
                .where(table.c.valid_from <= valid_from, \
                    table.c.valid_to >= valid_to
                )
            results = connection.execute(query).fetchall()
            versions[table_name] = frozenset(
                res for res in results
            )
        
        return self.__get_df(versions)


"""
            
    with open(file_name, 'w') as conf:
        for table_name, table in tables.items():
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
"""
    
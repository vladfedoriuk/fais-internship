from utils.db import ConfTableFactory, engine, DB, Files, tables_query, EXCLUDE
from utils.time import time_patterns_set, r_time_patterns, validate_date
import argparse
from datetime import datetime
from sqlalchemy.sql import select, join
from functools import reduce
import logging
import pandas
import sys
import re

parser = argparse.ArgumentParser()
connection = engine.connect()
factory = ConfTableFactory()

def process_run(tables, args, run=True):
    
    if run:
        try:
            run_id = int(args.run)
            if run_id < 1:
                raise ValueError()
        except ValueError:
            logging.error('The run id shoud be a positive integer')
            sys.exit()
    else:
        file = args.file
    
    versions = {}
    
    for table_name, table in tables.items():
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
                ).select_from(j).where(Files.c.run_id == run_id)
        else:
            s = select(
                    table.c.valid_from, 
                    table.c.valid_to, 
                    table.c.version, 
                    table.c.remarks
                ).select_from(j).where(Files.c.file_name == file)
            
        results = connection.execute(s).fetchall()
        versions[table_name] = set(res for res in results)
    
    available_versions = reduce(lambda s1, s2: s1 & s2, versions.values())
    available_versions = list(available_versions)
    
    df = pandas.DataFrame(
        data=available_versions, 
        index=range(len(available_versions)),
        columns=['VALID_FROM', 'VALID_TO', 'VERSION', 'REMARKS']
    )
    print(df)
    df.index.name = 'ID'

    idx = int(input('Input a version ID:'))
    
    if not all(available_versions[idx] in vers for vers in versions.values()):
        logging.error('The version in not present in some of the configurations.')
        sys.exit()  
        
    valid_from = available_versions[idx][0]
    valid_to = available_versions[idx][1]
    version = available_versions[idx][2]
    
    return valid_from, valid_to, version
 
 
def process_dates(tables, args):
    
    versions = {}
    for table_name, table in tables.items():
        query = select(table.c.version, table.c.remarks)\
            .where(table.c.valid_from <= valid_from, \
                table.c.valid_to >= valid_to
            )
        results = connection.execute(query).fetchall()
        versions[table_name] = frozenset(
            res for res in results
        )
        
    available_versions = reduce(lambda s1, s2: s1 & s2, versions.values())
    available_versions = list(available_versions)
    
    if not args.version:
        print(f'available verions of configurations:')
        df = pandas.DataFrame(
            data=available_versions,
            index=range(len(available_versions)),
            columns=['VERSION', 'REMARKS']
        )
        df.index.name = 'ID'
        print(df)   
        version_id = int(input('Please choose one [input an index]:'))
        version = available_versions[version_id]
        
    else:
        version = args.version
    
    if not all(version in vers for vers in versions.values()):
        logging.error('The version is not present in some of the configurations.')
        sys.exit()  
    
    return version     


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
    
    table_names = connection.execute(tables_query)
    tables = {}
    for table_name in table_names:
        if not any(re.match(x, table_name[0]) for x in EXCLUDE):
            tables[table_name[0]] = factory(table_name[0])
    
    args = parser.parse_args()
    
    if args.validfrom is not None:
        valid_from = validate_date(args.validfrom, 'validfrom')
        
    if args.validto is not None:   
        valid_to = validate_date(args.validto, 'validto')
    
    if args.file is not None:
        valid_from, valid_to, version = process_run(tables, args, run=False)
    elif args.run is not None:
        valid_from, valid_to, version = process_run(tables, args, run=True)
    else:
        version = process_dates(tables, args)
        
    if args.name is None:
        file_name = f'./configuration_{valid_from}_{valid_to}_version_{version}'
    else:
        file_name = args.name
            
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
    
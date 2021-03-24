from utils.db import ConfTableFactory, engine, DB, Files
from utils.time import time_patterns_set, r_time_patterns
import argparse
from datetime import datetime
from sqlalchemy.sql import select, join
from functools import reduce
import logging
import sys
import re

parser = argparse.ArgumentParser()
connection = engine.connect()
factory = ConfTableFactory()

tables_query = 'SELECT table_name FROM information_schema.tables ' + \
    f'WHERE table_name NOT IN ("configuration", "files") AND ' + \
        f'table_schema = \"{DB["database"]}\";'
        

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
    
    args = parser.parse_args()
    
    if args.validfrom:
        for pattern in time_patterns_set:
            try:
                valid_from = datetime.strptime(args.validfrom, pattern)
                break
            except ValueError:
                pass 
        else:
            logging.error('No time pattern matched for validfrom. Use -h flag to see the whole pattern')
            sys.exit()
    
    if args.validto:   
        for pattern in time_patterns_set:
            try:
                valid_to = datetime.strptime(args.validto, pattern)
                break
            except ValueError:
                pass
        else:
            logging.error('No time pattern matched for validto. Use -h flag to see the whole pattern')
            sys.exit()
    
    table_names = connection.execute(tables_query)
    tables = {}
    for table_name in table_names:
        tables[table_name[0]] = factory(table_name[0])
        
    if args.run:
        
        versions = set()
        for table_name, table in tables.items():
            j = join(
                Files, table, 
                (Files.c.start_time >= table.c.valid_from) & \
                    (Files.c.stop_time <= table.c.valid_to)
            )
            results = connection.execute(
                select(
                    table.c.valid_from, 
                    table.c.valid_to, 
                    table.c.version, 
                    table.c.remarks
                ).select_from(j)
            ).fetchall()
            versions |= set(res for res in results)
            
        versions = list(versions)
        print('ID\t\tVALID_FROM\t\t\t\tVALID_TO\tVERSION\t\t\tREMARKS') 
        for i, version in enumerate(versions):
            print(f"{i}\t\t{str(version[0])}\t\t{str(version[1])}\t\t{version[2]}\t{version[3] if version[3] else ''}")
        idx = int(input('Input a version ID:'))
        
        valid_from = versions[idx][0]
        valid_to = versions[idx][1]
        version = versions[idx][2]
        
    else:
        
        versions = {}
        for table_name, table in tables.items():
            query = select(table.c.version, table.c.remarks)\
                .where(table.c.valid_from <= valid_from, \
                    table.c.valid_to >= valid_to
                )
            results = connection.execute(query).fetchall()
            versions[table_name] = frozenset(
                (res[0], res[1]) if res[1] else res[0] for res in results
            )
        
        available_versions = reduce(lambda s1, s2: s1 & s2, versions.values())
    
        if not args.version:
        
            print(f'available verions of configurations:')
            print('VERSION\t\tREMARKS')
            for v in sorted(available_versions, key=lambda x: x if isinstance(x, int) else x[0]):
                if isinstance(v, tuple):
                    print(f"{v[0]}\t\t{v[1]}")
                else:
                    print(v)
                
            version = int(input('Please choose one [input a number]:'))
        else:
            version = args.version
    
        if not all(version in vers for vers in versions.values()):
            logging.error('The version in not present in some of the configurations.')
            sys.exit()
     
     
       
    if not args.name:
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
    
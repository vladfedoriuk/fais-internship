import re
import sys
import logging
import argparse
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime, timedelta
from utils.db import ConfTableFactory, Files, engine
from utils.time import time_patterns_set, r_time_patterns, validate_date
from sqlalchemy.sql import select


parser = argparse.ArgumentParser()
connection = engine.connect()


@dataclass
class Token:
    kind: str
    value: str

class Tokenizer(object):
    
    groups = (
        ('CLASS', r'\[\w+\]'),
        ('PARAMS', r'[^\[\]]*')
    )
    regex = re.compile(
        pattern='|'.join(f'(?P<{group[0]}>{group[1]})' for group in groups),
        flags=re.M
    )
    
    def __init__(self, text):
        self.text = text
    
    def __iter__(self):
        for match in self.regex.finditer(self.text.strip()):
            kind = match.lastgroup
            value = match.group()
            yield Token(
                kind=kind.strip(), 
                value=value.strip()
            )
  
            
class Converter(object):
    
    def __init__(self):
        self.table2params = defaultdict(lambda: '')
    
    def __setitem__(self, table_name, params):
        self.table2params[table_name] += params
    
    def __getitem__(self, table_name):
        return self.table2params[table_name]
    
    def save(self, version, valid_from, valid_to, remarks=None):
        connection = engine.connect()
        factory = ConfTableFactory()
        for table_name, params in self.table2params.items():
            table = factory(table_name)
            ins = table.insert().values(
                parameters=params,
                valid_from=valid_from,
                valid_to=valid_to,
                version=version,
                remarks=remarks
            )
            connection.execute(ins)   
                     

def write_to_database(conf_file, version, valid_from, valid_to, remarks=None):
    with open(conf_file) as file:
        tokenizer = Tokenizer(file.read())
        converter = Converter()
        current_table = None
        for token in tokenizer:
            if token.kind == 'CLASS':
                current_table = token.value[
                    token.value.index('[') + 1 : token.value.index(']')
                ]
            elif token.kind == 'PARAMS' and current_table:
                converter[current_table] = token.value
        converter.save(version, valid_from, valid_to, remarks=remarks)
            
            
if __name__ == '__main__':
    parser.add_argument("conf", 
                        help=f'The name of the configuration file')
    parser.add_argument("version",
                        help='The version of the configuration')
    parser.add_argument("-rf", "--runfrom",
                        help=f'The run from which the configuration is valid', type=int)
    parser.add_argument('-rt', '--runto', 
                        help='The run up to which the configuration is valid', type=int)
    parser.add_argument("-ff", "--filefrom",
                        help=f'The run file from which the configuration is valid')
    parser.add_argument('-ft', '--fileto', 
                        help='The run file up to which the configuration is valid')
    parser.add_argument('-vf', '--validfrom',
                        help='The datetime from which the configuration is valid\n' + \
                            f'Accepted patterns: {r_time_patterns}')
    parser.add_argument('-vt', '--validto', 
                        help='The datetime up to which the configuration is valid\n' + \
                            f'Accepted patterns: {r_time_patterns}')
    parser.add_argument('--remarks', '-r',
                        help="The optional remarks about the configuration version")
    
    args = parser.parse_args()
    
    valid_from = None
    valid_to = None
    conf_file = args.conf
    
    try:
        version = int(args.version)
    except ValueError:
        logging.error('Th version should be a positive integer')
    
    if args.runfrom is not None:
        valid_from = connection.execute(
            select(Files.c.start_time).where(
                Files.c.run_id==args.runfrom
            )
        ).fetchone()[0]
    
    if args.runto is not None:
        valid_to = connection.execute(
            select(Files.c.start_time).where(
                Files.c.run_id==args.runto
            )
        ).fetchone()[0]
    
    if args.filefrom is not None:
        valid_from = connection.execute(
            select(Files.c.start_time).where(
                Files.c.file_name==args.filefrom
            )
        ).fetchone()[0] 
    
    if args.fileto is not None:
        valid_to = connection.execute(
            select(Files.c.start_time).where(
                Files.c.file_name==args.fileto
            )
        ).fetchone()[0]  
        
    if args.validfrom and not valid_from:
        valid_from = validate_date(args.validfrom, 'validfrom')
    
    if args.validto and not valid_to:
        valid_to = validate_date(args.valid_to, 'validto')
        
    write_to_database(
        conf_file=conf_file,
        version=version,
        valid_from=valid_from,
        valid_to=valid_to,
        remarks=args.remarks
    )
        
                
    
import re
import sys
import logging
import argparse
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime, timedelta
from utils.db import ConfTableFactory, Files, engine, tables_query, EXCLUDE
from utils.time import time_patterns_set, r_time_patterns, validate_date
from sqlalchemy.sql import select
from itertools import chain
from functools import singledispatchmethod
from typing import Tuple


parser = argparse.ArgumentParser()
connection = engine.connect()


@dataclass
class Token:
    kind: str
    value: str
    
@dataclass
class Filenames:
    filename_from: str
    filename_to: str
    
@dataclass
class Runs:
    run_from: int
    run_to: int

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
                     

def write_to_database(conf_file_path, version, valid_from, valid_to, remarks=None):
    table_names = connection.execute(tables_query)
    table_names = set(x for x in chain.from_iterable(table_names) if \
        not any(re.match(y, x) for y in EXCLUDE)
    )
    seen_tables = set()
    with open(conf_file_path) as file:
        tokenizer = Tokenizer(file.read())
        converter = Converter()
        current_table = None
        for token in tokenizer:
            if token.kind == 'CLASS':
                current_table = token.value[
                    token.value.index('[') + 1 : token.value.index(']')
                ]
                if current_table not in table_names:
                    raise ValueError(f'there is no such table in the database: {current_table}')
                seen_tables.add(current_table)
            elif token.kind == 'PARAMS' and current_table:
                converter[current_table] = token.value
        if seen_tables != table_names:
            raise ValueError(f'The configurations for tables {", ".join(table_names - seen_tables)} where not found')
        converter.save(version, valid_from, valid_to, remarks=remarks)


class ValidityDates(object):
    
    @singledispatchmethod
    def from_params(self, arg) -> Tuple[datetime, datetime]:
        raise NotImplementedError(f"Cannot extract valididity dates from {type(arg)}")
         
    @from_params.register
    def _(self, arg: Runs) -> Tuple[datetime, datetime]:
        valid_from = connection.execute(
            select(Files.c.start_time).where(
                Files.c.run_id==arg.run_from
            )
        ).fetchone()
        
        if not valid_from:
            raise ValueError('incorrect run-from id (there is no such run in a database).')
        
        valid_from = valid_from[0]
        
        valid_to = connection.execute(
            select(Files.c.start_time).where(
                Files.c.run_id==arg.run_to
            )
        ).fetchone()
        
        if not valid_to:
            raise ValueError('incorrect run-to id (there is no such run in a database).')
        
        valid_to = valid_to[0]
        
        return valid_from, valid_to
        
    
    @from_params.register
    def _(self, arg: Filenames) -> Tuple[datetime, datetime]:
        valid_from = connection.execute(
            select(Files.c.start_time).where(
                Files.c.file_name==arg.filename_from
            )
        ).fetchone()
        
        if not valid_from:
            raise ValueError('incorrect run-from filename (there is no such run in a database).')
        
        valid_from = valid_from[0]
        
        valid_to = connection.execute(
            select(Files.c.start_time).where(
                Files.c.file_name==arg.filename_to
            )
        ).fetchone()
        
        if not valid_to:
            raise ValueError('incorrect run-to filename (there is no such run in a database).')
        
        valid_to = valid_to[0]
        
        return valid_from, valid_to          
            
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
        if version < 1:
            raise ValueError()
    except ValueError:
        logging.error('Th version should be a positive integer')
        
    if args.validfrom:
        valid_from = validate_date(args.validfrom, 'validfrom')
    
    if args.validto:
        valid_to = validate_date(args.valid_to, 'validto')
    
    if args.runfrom and args.runto:
        arg = Runs(args.runfrom, args.runto)
    elif args.filefrom and args.fileto:
        arg = Filenames(args.filefrom, args.fileto)
    
    if not valid_from and not valid_to:
        vd = ValidityDates()
        try:
            valid_from, valid_to = vd.from_params(arg)
        except Exception as e:
            error = e.args
            logging.error(error)
            sys.exit()
    
    if valid_from and valid_to:
        try:
            write_to_database(
                conf_file_path=conf_file,
                version=version,
                valid_from=valid_from,
                valid_to=valid_to,
                remarks=args.remarks
            )
        except Exception as e:
            error = e.args
            logging.error(error)
            sys.exit()
    else:
        logging.error('Failed to extract the validity dates from provided parameters.')
        sys.exit()
        
                
    
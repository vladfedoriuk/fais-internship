import re
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime, timedelta
from .utils.db import ConfTableFactory, Files, engine, tables_query
from sqlalchemy.sql import select
from functools import singledispatchmethod
from datetime import datetime
from typing import Tuple

connection = engine.connect()


@dataclass
class Filenames:
    filename_from: str
    filename_to: str
    
@dataclass
class Runs:
    run_from: int
    run_to: int
    
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
                     

def write_to_database(conf_file_path, version, valid_from, valid_to, remarks=None):
    with open(conf_file_path) as file:
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
        

def handle_uploaded_file(f):
    file_path = f'./interact/files/parsed/{str(f)}'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

            
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
                
    
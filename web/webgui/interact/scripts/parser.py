import re
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime, timedelta
from .utils.db import ConfTableFactory, Files, engine, tables_query, EXCLUDE
from sqlalchemy.sql import select
from functools import singledispatchmethod
from datetime import datetime
from typing import Tuple
from itertools import chain
from django.apps import apps
from core.models import Release
from typing import Optional

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
    
    def __init__(self, text: str):
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
    
    def save(self,
             release: Release, 
             version: int, 
             valid_from: datetime, 
             valid_to: datetime, 
             remarks: Optional[str]=None):
        
        for table_name, params in self.table2params.items():
            table = apps.get_model('core', table_name)
            new_conf = table(
                parameters=params,
                version=version,
                valid_from=valid_from,
                valid_to=valid_to,
                remarks=remarks,
                release=release
            )
            new_conf.save()
                     

def write_to_database(
    conf_file_path: str, 
    release: Release, 
    version: int, 
    valid_from: datetime, 
    valid_to: datetime, 
    remarks: Optional[str]=None):
    
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
        converter.save(
            release=release,
            version=version, 
            valid_from=valid_from, 
            valid_to=valid_to,
            remarks=remarks
        )
        

def handle_uploaded_file(f: str):
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
        Files = apps.get_model('core', 'Files')
        run_from = Files.objects.filter(run_id=arg.run_from)
        if not run_from:
            raise ValueError('incorrect run-from id (there are no such runs in the database).') 
        if len(run_from) > 1:
            raise ValueError('incorrect run-from id (there are more than 1 run with such an id).')  
        run_from = run_from.first()
        valid_from = run_from.start_time
        
        run_to = Files.objects.filter(run_id=arg.run_to) 
        if not run_to:
            raise ValueError('incorrect run-to id (there are no such runs in the database).') 
        if len(run_to) > 1:
            raise ValueError('incorrect run-to id (there are more than 1 run with such an id).')  
        run_to = run_to.first()
        valid_to = run_to.start_time
        
        return valid_from, valid_to
        
    
    @from_params.register
    def _(self, arg: Filenames) -> Tuple[datetime, datetime]:
        Files = apps.get_model('core', 'Files')
        run_from = Files.objects.filter(file_name=arg.filename_from)
        if not run_from:
            raise ValueError('incorrect run-from filename (there are no such runs in the database).') 
        if len(run_from) > 1:
            raise ValueError('incorrect run-from filename (there are more than 1 run with such a filename).')  
        run_from = run_from.first()
        valid_from = run_from.start_time
        
        run_to = Files.objects.filter(file_name=arg.filename_to) 
        if not run_to:
            raise ValueError('incorrect run-to filename (there are no such runs in the database).') 
        if len(run_to) > 1:
            raise ValueError('incorrect run-to filename (there are more than 1 run with such a filename).')  
        run_to = run_to.first()
        valid_to = run_to.start_time
        
        return valid_from, valid_to
                
    
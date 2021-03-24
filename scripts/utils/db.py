import os
import logging
from sqlalchemy import __version__ as sv
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, \
    Integer, String, MetaData, DateTime, Text
    
logging.info(f'Using sqlalchemy version: {sv}')

DB = {
    'dialect': 'mysql',
    'username': os.environ.get('username'),
    'password': os.environ.get('password'),
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'praktyki'
}

engine = create_engine(
    f"{DB['dialect']}://" + \
        f"{DB['username']}:" + \
            f"{DB['password']}@" + \
                f"{DB['host']}:{DB['port']}/{DB['database']}"
)

metadata = MetaData(engine)

class ConfTableFactory(object):
    def __call__(self, table_name):
        # return Table(table_name, metadata, autoload=True, autoload_with=engine)
        return Table(
            table_name, metadata,
            Column('id', Integer, primary_key=True),
            Column('parameters', Text, nullable=True),
            Column('valid_from', DateTime(timezone=True), nullable=False, default=datetime.utcnow),
            Column('valid_to', DateTime(timezone=True), nullable=False),
            Column('version', Integer, default=1, nullable=False),
            Column('remarks', String),
            autoload_with=engine
        )

Files = Table(
    'files', metadata,
    Column('id', Integer, primary_key=True),
    Column('file_name', String, nullable=False),
    Column('start_time', DateTime(timezone=True), nullable=False, default=datetime.utcnow),
    Column('stop_time', DateTime(timezone=True), nullable=False),
    Column('remarks', String),
    Column('run_id', Integer),
    autoload_with=engine
)
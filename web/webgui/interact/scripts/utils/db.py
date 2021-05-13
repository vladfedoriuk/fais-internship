from datetime import datetime
from functools import partial
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    DateTime,
    Text,
)

from django.conf import settings

DATABASES = settings.DATABASES

DB = {
    "dialect": "mysql",
    "username": DATABASES["default"]["USER"],
    "password": DATABASES["default"]["PASSWORD"],
    "host": DATABASES["default"]["HOST"],
    "port": DATABASES["default"]["PORT"],
    "database": DATABASES["default"]["NAME"],
}

tables_query = (
    "SELECT table_name FROM information_schema.tables WHERE "
    + 'table_name NOT IN ("configuration", "files", "release")'
    + f'AND table_schema = "{DB["database"]}";'
)

EXCLUDE = {r"auth.+", r"django.+"}

engine = create_engine(
    f"{DB['dialect']}://"
    + f"{DB['username']}:"
    + f"{DB['password']}@"
    + f"{DB['host']}:{DB['port']}/{DB['database']}"
)

metadata = MetaData(engine)


class Cache(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, obj, table_name):
        if table_name not in self.cache:
            self.cache[table_name] = self.func(obj, table_name)
        return self.cache[table_name]

    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)


class ConfTableFactory(object):

    # @Cache
    def __call__(self, table_name):
        # return Table(table_name, metadata, autoload=True, autoload_with=engine)
        return Table(
            table_name,
            metadata,
            Column("id", Integer, primary_key=True),
            Column("parameters", Text, nullable=True),
            Column(
                "valid_from",
                DateTime(timezone=True),
                nullable=False,
                default=datetime.utcnow,
            ),
            Column("valid_to", DateTime(timezone=True), nullable=False),
            Column("version", Integer, default=1, nullable=False),
            Column("remarks", String),
            autoload_with=engine,
            extend_existing=True,
        )


try:
    Files = Table(
        "files",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("file_name", String, nullable=False),
        Column(
            "start_time",
            DateTime(timezone=True),
            nullable=False,
            default=datetime.utcnow,
        ),
        Column("stop_time", DateTime(timezone=True), nullable=False),
        Column("remarks", String),
        Column("run_id", Integer),
        autoload_with=engine,
    )
except:
    Files = None

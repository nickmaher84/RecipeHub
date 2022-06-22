from sqlalchemy import MetaData, Table, Column, UniqueConstraint, engine_from_config, text
from sqlalchemy.types import String, DateTime, JSON
from configparser import ConfigParser

config = ConfigParser()
config.read('../scrapy.cfg')

engine = engine_from_config(config['database'])
metadata = MetaData(schema='raw', bind=engine)

raw_table = Table(
    'recipe', metadata,
    Column('spider', String(length=100), nullable=False),
    Column('url', String(length=255), nullable=False),
    Column('json', JSON(), nullable=False),
    Column('language', String(length=100), nullable=True),
    Column('checksum', String(length=32), nullable=False),
    Column('timestamp', DateTime(), nullable=False),
)

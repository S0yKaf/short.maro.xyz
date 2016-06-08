from sqlalchemy import Table, Column, Integer, String, Binary, Boolean
from sqlalchemy.orm import mapper

from database import metadata, db_session


class Url:
    query = db_session.query_property()

    def __init__(self, url, short_url):
        self.url = url
        self.short_url = short_url


urls = Table('urls', metadata,
             Column('id', Integer, primary_key=True),
             Column('url', String(2048), unique=True),
             Column('short_url', String(7), unique=True)
             )

mapper(Url, urls)

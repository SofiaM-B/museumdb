import sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('mysql:///:memory:', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users = Table('users', metadata, Column('id', Integer, primary_key=True), Column('name', String), Column('fullname', String),)
adresses = Table('addresses', metadata, Column('id', Integer, primary_key=True), Column('user_id', None, ForeignKey('user.id')), Column('email_address', String, nullable=False))

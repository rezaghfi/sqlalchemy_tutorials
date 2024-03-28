#start for connection to sqlalchemy 1.4

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#database connection --> library://username:password@host:port/dbname

engine = create_engine("sqlite:///test.sqlite")
base = declarative_base()

class Strudent(base):
    __tablename__ = 'student'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))

# use base to use engine
base.metadata.create_all(engine)

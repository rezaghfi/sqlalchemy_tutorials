from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

class DB:

    _engine = create_engine("sqlite:///mydatabase.db")
    _base = declarative_base()

    def __init__(self):
        self.session_maker = sessionmaker(bind=self._engine)
        self.session = None

    def create_session(self):
        self.session = self.session_maker()

    def create_all_table(self):
        self._base.metadata.create_all(self._engine)

    class SubClass:
        id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)

    class Person(SubClass, _base):
        __tablename__ = 'person'
        name = Column('name', String(50))
        family = Column('family', String(50))
        role_id = Column('role_id', Integer, ForeignKey('role.id'))
    class Role(SubClass, _base):
        __tablename__ = 'role'
        name = Column('name', String(50))
        users = relationship('Person', backref='role')
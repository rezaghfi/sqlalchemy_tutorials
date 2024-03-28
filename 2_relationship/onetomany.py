from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///rel.sqlite')
base = declarative_base()
Session = sessionmaker(bind=engine)
session =Session()

# one(classroom) ---> many(student)
class Student(base):
    __tablename__ = 'student'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    classroom_id = Column('classroom_id', Integer, ForeignKey('classroom.id'))
class ClassRoom(base):
    __tablename__ = 'classroom'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    students = relationship('Student', backref='classroom')

base.metadata.create_all(engine)
#sqlite can create new file if file dont exists.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_

engine = create_engine("sqlite:///db.sqlite")
# object of declarative
base = declarative_base()
#for use crud must use session
# sessionmaker pass function and must call it!!!!!!!!!
session = sessionmaker(bind=engine)()
class Student(base):
    __tablename__ = 'student'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))

base.metadata.create_all(engine)

#select
students = session.query(Student).all()
for student in students:
    print(student._id , student.name)
students = session.query(Student).filter(and_(Student.name=='reza', Student._id == 2)).all()
print(students)


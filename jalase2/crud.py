#sqlite can create new file if file dont exists.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_, or_

engine = create_engine("sqlite:///db.sqlite")
# object of declarative
base = declarative_base()
#for use crud must use session
# sessionmaker pass function and must call it!!!!!!!!!
# session = sessionmaker(bind=engine, autocommit=True)()
session = sessionmaker(bind=engine)()
class Student(base):
    __tablename__ = 'student'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))

base.metadata.create_all(engine)

#select_all
students = session.query(Student).all()
for student in students:
    print(student._id , student.name)
#select_first
student = session.query(Student).first()
print(student._id, student.name)
#filter in select
students = session.query(Student).filter(or_(Student._id <= 2, Student._id > 10)).all()
for student in students:
    print(student._id , student.name)

#insert
s1 = Student(name='zahra')
s2 = Student(name='farima')
session.add(s1)
session.add_all([s1, s2])
session.commit()

#delete
#first run query to select
# dele = session.query(Student).filter(Student.name=='zahra').first()
# session.delete(dele)
session.query(Student).filter(Student.name=='zahra').delete()
session.commit()

#update
session.query(Student).filter(Student._id == 1).update({'name' : 'nagi'})
stu = session.query(Student).filter(Student._id == 1).first()
stu.name = 'omid'
session.commit()
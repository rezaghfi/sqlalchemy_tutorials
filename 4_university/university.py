from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

class DB:

    _engine = create_engine("sqlite:///uni.db")
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

    class Student(SubClass, _base):
        __tablename__ = 'student'
        name = Column('name', String(50))
        dataOfBirth = Column('date_of_birth', Date)
        courses = relationship('Course', secondary='course_student', back_populates='student')

    class Course(SubClass, _base):
        __tablename__ = 'course'
        name = Column('name', String(50))
        duration = Column('duration', Integer)
        department_id = Column('department_id', Integer, ForeignKey('department.id'))
        instructor_id = Column('instructor_id', Integer, ForeignKey('instructor.id'))
        students = relationship('Student', secondary='course_student', back_populates='course')
    class Instructor(SubClass, _base):
        __tablename__ = 'instructor'
        name = Column('name', String(50))
        roomNo = Column('room_no', Integer)
        department_id = Column('department_id', Integer, ForeignKey('department.id'))
        courses = relationship('Course', backref='instructor')
        department = relationship('Department', backref='instructor')

    class Department(SubClass, _base):
        __tablename__ = 'department'
        name = Column('name', String(50))
        management_id = Column('management_id', Integer, ForeignKey('instructor.id'))
        instructors = relationship('Instructor', backref='department')

    class CourseStudent(SubClass, _base):
        __tablename__ = "course_student"
        course_id = Column('course_id', Integer, ForeignKey('course.id'))
        student_id = Column('student_id', Integer, ForeignKey('student.id'))

if __name__ == '__main__':
    db = DB()
    db.create_all_table()
    db.create_session()
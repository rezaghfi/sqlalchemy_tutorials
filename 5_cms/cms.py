from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

class DB:

    _engine = create_engine("sqlite:///cms.db")
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

    class User(SubClass, _base):
        __tablename__ = 'user'
        name = Column('name', String(50))
        dataOfBirth = Column('date_of_birth', Date)
        photo_id = Column('photo_id', ForeignKey('photo.id'))
        roles = relationship('Role', secondary='role_user', back_populates='user')

    class Post(SubClass, _base):
        __tablename__ = 'post'
        title = Column('name', String(50))
        content = Column('content', Text)
        photos = relationship('Photo', secondary='post_photo', back_populates='post')
        users = relationship('Users', backref = 'post')
    class Photo(SubClass, _base):
        __tablename__ = 'photo'
        name = Column('name', String(50))
        address = Column('address', String(200))
        Posts = relationship('Posts', secondary='post_photo', back_populates='photo')

    class Role(SubClass, _base):
        __tablename__ = 'role'
        name = Column('name', String(50))
        users = relationship('User', secondary='role_user', back_populates='role')

    class RoleUser(SubClass, _base):
        __tablename__ = "role_user"
        course_id = Column('role_id', Integer, ForeignKey('role.id'))
        student_id = Column('user_id', Integer, ForeignKey('user.id'))

if __name__ == '__main__':
    db = DB()
    db.create_all_table()
    db.create_session()
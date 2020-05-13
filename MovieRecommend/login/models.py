from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
import mysql.connector
# Create your models here.
Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Username = Column(String(128), unique=True, nullable=False)
    Password = Column(String(256), nullable=False)


engine = create_engine('mysql+mysqlconnector://peeeyiii:peeeyiii@127.0.0.1:3306/MovieRecommend')
# Base.metadata.create_all(engine)


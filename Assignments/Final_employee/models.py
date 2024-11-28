from sqlalchemy import Column,Integer, String, Date
from db import Base


class Employee(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer,primary_key=True ,index=True,nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob=Column(Date)
    doj=Column(Date)
    grade=Column(String)


class Login(Base):
    __tablename__ = 'login'
    user_id = Column(String,primary_key=True, unique=True, nullable=False) 
    password = Column(String, nullable=False)
   
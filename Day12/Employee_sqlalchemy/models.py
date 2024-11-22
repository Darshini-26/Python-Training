from sqlalchemy import Column,Integer, String
from database import Base

class Employee(Base):
    __tablename__ = 'employees'

    num = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location=Column(String,index=True)
    dept_id = Column(Integer,index=True)
    

    def __repr__(self):
        return f"Employee number={self.num}, name={self.name}, location={self.location},Department ID={self.dept_id}"

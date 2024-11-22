from fastapi import FastAPI
import models as models
from models import Employee
from database import session as db_session, engine
models.Base.metadata.create_all(bind=engine)


def update_location( num:int,location:str):
    db_employee = db_session.query(Employee).filter(Employee.num == num).first()
    if db_employee:
        db_employee.location = location
    db_session.commit()
    db_session.refresh(db_employee)
    return db_employee

def view_all():
    return db_session.query(Employee).all()

def view_number(num: int):
    return db_session.query(Employee).filter(Employee.num == num).first()

def view_location(location:str):
    return db_session.query(Employee).filter(Employee.location==location).first()

print(view_all())
print(view_number(1))
print(view_location("chennai"))
print(update_location(2,"Pune"))
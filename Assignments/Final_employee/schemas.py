from pydantic import BaseModel
from datetime import datetime


class Employee(BaseModel):
    emp_id : int
    first_name : str
    last_name : str
    dob:datetime
    doj:datetime
    grade:str

class Login(BaseModel):
    user_id:str
    password:str


from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from logic import Logic
from emplo import Employee

# Pydantic models for request validation
class EmployeeModel(BaseModel):
    empno: int
    empname: str
    location: str
    deptid: int

class UpdateLocationModel(BaseModel):
    location: str

# Initialize FastAPI app
app = FastAPI()
logic_manager = Logic()

@app.put("/update_employee/{empno}", status_code=status.HTTP_200_OK)
async def update_employee(empno: int, location: UpdateLocationModel):
    updated = logic_manager.update(empno, location.location)
    if updated:
        return {"message": "Employee location updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

@app.get("/list_employees", response_model=List[EmployeeModel], status_code=status.HTTP_200_OK)
async def list_employees():
    employees = logic_manager.view_all()
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")

@app.get("/view_location/location/{location}", response_model=List[EmployeeModel], status_code=status.HTTP_200_OK)
async def view_employees_by_location(location: str):
    employees = logic_manager.view_location(location)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found at this location")

@app.get("/view_employee/{empno}", status_code=status.HTTP_200_OK)
async def view_employee_by_empno(empno: int):
    employees = logic_manager.view_empno(empno)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
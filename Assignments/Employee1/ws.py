from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from main import Main


class EmployeeModel(BaseModel):
    """
    Schema for Employee data.

    Attributes:
        empno (int): Employee number.
        empname (str): Employee name.
        location (str): Employee location.
        deptid (int): Department ID.
    """
    empno: int
    empname: str
    location: str
    deptid: int


class UpdateLocationModel(BaseModel):
    """
    Schema for updating employee location.

    Attributes:
        location (str): The new location for the employee.
    """
    location: str


app = FastAPI()
logic_manager = Main()


@app.put("/update_employee/{empno}", status_code=status.HTTP_200_OK)
async def update_employee(empno: int, location: UpdateLocationModel):
    """
    Update an employee's location.

    Args:
        empno (int): The employee number.
        location (UpdateLocationModel): The new location data.

    Returns:
        dict: Success message if the update is successful.

    Raises:
        HTTPException: If the employee is not found (404).
    """
    updated = logic_manager.update_location(empno, location.location)
    if updated:
        return {"message": "Employee location updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")


@app.get("/list_employees", status_code=status.HTTP_200_OK)
async def list_employees():
    """
    Retrieve a list of all employees.

    Returns:
        list: A list of all employees.

    Raises:
        HTTPException: If no employees are found (404).
    """
    employees = logic_manager.view_all()
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")


@app.get("/view_location/{location}", status_code=status.HTTP_200_OK)
async def view_employees_by_location(location: str):
    """
    Retrieve employees by location.

    Args:
        location (str): The location to filter employees by.

    Returns:
        list: A list of employees at the specified location.

    Raises:
        HTTPException: If no employees are found at the location (404).
    """
    employees = logic_manager.view_location(location)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found at this location")


@app.get("/view_employee/{empno}", status_code=status.HTTP_200_OK)
async def view_employee_by_empno(empno: int):
    """
    Retrieve an employee by their employee number.

    Args:
        empno (int): The employee number.

    Returns:
        dict: The details of the employee.

    Raises:
        HTTPException: If the employee is not found (404).
    """
    employees = logic_manager.view_number(empno)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

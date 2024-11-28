from fastapi import FastAPI, status, HTTPException, UploadFile, File, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from main import Main
from schemas import Employee, Login
from db import get_db, Session

app = FastAPI()
security=HTTPBasic()
logic_manager = Main()


@app.post("/login", status_code=status.HTTP_200_OK)
async def login_endpoint(login_data: HTTPBasicCredentials=Depends(security)):
    """
    Authenticates a user using their user ID and password.

    Args:
        login_data (Login): The login credentials (user_id and password).

    Returns:
        dict: A success message if authentication is successful.

    Raises:
        HTTPException: If the user ID or password is invalid.
    """
    employee = logic_manager.login_user(login_data.username, login_data.password)
    if employee:
        return {"message": "Welcome all "}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ID or password"
        )


@app.put("/update_employee/{emp_id}",dependencies=[Depends(login_endpoint)], status_code=status.HTTP_200_OK)
async def update_employee(emp_id: int, updated_employee: Employee):
    """
    Updates employee information by employee ID.

    Args:
        emp_id (int): The employee ID of the employee to update.
        updated_employee (Employee): The updated employee data.

    Returns:
        dict: A success message if the employee is updated.

    Raises:
        HTTPException: If the employee ID is not found.
    """
    updated = logic_manager.update(emp_id, updated_employee)
    if updated:
        return {"message": "Employee updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")


@app.get("/view_employee_empno/{emp_id}",dependencies=[Depends(login_endpoint)], status_code=status.HTTP_200_OK)
async def view_employee_by_empno(emp_id: int):
    """
    Retrieves an employee's details by their employee ID.

    Args:
        emp_id (int): The employee ID to search.

    Returns:
        dict: The employee's details if found.

    Raises:
        HTTPException: If no employee is found with the given ID.
    """
    employees = logic_manager.view_by_number(emp_id)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")


@app.get("/search_firstname/{first_name}", dependencies=[Depends(login_endpoint)],status_code=status.HTTP_200_OK)
async def search_employees_by_firstname(first_name: str):
    """
    Searches employees by their first name.

    Args:
        first_name (str): The first name to search.

    Returns:
        list[dict]: A list of employees matching the first name.

    Raises:
        HTTPException: If no employees are found.
    """
    employees = logic_manager.search_by_first_name(first_name)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found ")


@app.get("/search_lastname/{last_name}", dependencies=[Depends(login_endpoint)],status_code=status.HTTP_200_OK)
async def search_employees_by_lastname(last_name: str):
    """
    Searches employees by their last name.

    Args:
        last_name (str): The last name to search.

    Returns:
        list[dict]: A list of employees matching the last name.

    Raises:
        HTTPException: If no employees are found.
    """
    employees = logic_manager.search_by_last_name(last_name)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found ")


@app.get("/search_by_dob/{dob}",dependencies=[Depends(login_endpoint)], status_code=status.HTTP_200_OK)
async def search_employees_by_dob(dob: str):
    """
    Searches employees by their date of birth.

    Args:
        dob (str): The date of birth to search.

    Returns:
        list[dict]: A list of employees matching the date of birth.

    Raises:
        HTTPException: If no employees are found.
    """
    employees = logic_manager.search_by_dob(dob)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found ")


@app.get("/search_by_doj/{doj}",dependencies=[Depends(login_endpoint)], status_code=status.HTTP_200_OK)
async def search_employees_by_doj(doj: str):
    """
    Searches employees by their date of joining.

    Args:
        doj (str): The date of joining to search.

    Returns:
        list[dict]: A list of employees matching the date of joining.

    Raises:
        HTTPException: If no employees are found.
    """
    employees = logic_manager.search_by_doj(doj)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found ")


@app.get("/search_by_grade/{grade}",dependencies=[Depends(login_endpoint)], status_code=status.HTTP_200_OK)
async def search_employees_by_grade(grade: str):
    """
    Searches employees by their grade.

    Args:
        grade (str): The grade to search.

    Returns:
        list[dict]: A list of employees matching the grade.

    Raises:
        HTTPException: If no employees are found.
    """
    employees = logic_manager.search_by_grade(grade)
    if employees:
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found ")


@app.post("/upload-csv",dependencies=[Depends(login_endpoint)])
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Uploads a CSV file containing employee data and processes it into the database.

    Args:
        file (UploadFile): The uploaded CSV file.
        db (Session): The database session dependency.

    Returns:
        dict: A success message upon successful CSV processing.
    """
    content = file.file.read().decode("utf-8")
    logic_manager.upload_csv(content, db)
    return {"message": "CSV file uploaded successfully"}

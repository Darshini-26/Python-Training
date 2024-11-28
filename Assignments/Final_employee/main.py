from fastapi import FastAPI
import csv
import models as models
from models import Employee,Login
from db import Session as db_session, engine,get_db
from datetime import datetime
models.Base.metadata.create_all(bind=engine)

class Main:

    def login_user(self, user_id: int, password: str):
        """
        Authenticates a user based on their user ID and password.

        Args:
            user_id (int): The ID of the user attempting to log in.
            password (str): The password of the user.

        Returns:
            Login: The user's login details if authentication is successful.
            None: If authentication fails.
        """
        db_employee = db_session.query(Login).filter(Login.user_id == user_id).first()
        if db_employee and db_employee.password == password:
            return db_employee
        else:
            return None

    def view_by_number(self, emp_id: int):
        """
        Retrieves an employee's details using their employee ID.

        Args:
            emp_id (int): The ID of the employee to retrieve.

        Returns:
            Employee: The employee's details if found.
            None: If no employee is found with the given ID.
        """
        return db_session.query(Employee).filter(Employee.emp_id == emp_id).first()

    def update(self, emp_id: int, updated_emp: Employee):
        """
        Updates the details of an existing employee.

        Args:
            emp_id (int): The ID of the employee to update.
            updated_emp (Employee): An object containing the updated employee details.

        Returns:
            Employee: The updated employee details.
            None: If no employee is found with the given ID.
        """
        db_employee = db_session.query(Employee).filter(Employee.emp_id == emp_id).first()
        if db_employee:
            db_employee.first_name = updated_emp.first_name
            db_employee.last_name = updated_emp.last_name
            db_employee.dob = updated_emp.dob
            db_employee.doj = updated_emp.doj
            db_employee.grade = updated_emp.grade
            db_session.commit()
            db_session.refresh(db_employee)
            return db_employee
        return None

    def search_by_first_name(self, first_name: str):
        """
        Searches employees by their first name.

        Args:
            first_name (str): The first name to search.

        Returns:
            list[Employee]: A list of employees with the matching first name.
        """
        return db_session.query(Employee).filter(Employee.first_name == first_name).all()

    def search_by_last_name(self, last_name: str):
        """
        Searches employees by their last name.

        Args:
            last_name (str): The last name to search.

        Returns:
            list[Employee]: A list of employees with the matching last name.
        """
        return db_session.query(Employee).filter(Employee.last_name == last_name).all()

    def search_by_dob(self, dob: str):
        """
        Searches employees by their date of birth.

        Args:
            dob (str): The date of birth in "YYYY-MM-DD" format.

        Returns:
            list[Employee]: A list of employees with the matching date of birth.
        """
        return db_session.query(Employee).filter(Employee.dob == dob).all()

    def search_by_doj(self, doj: str):
        """
        Searches employees by their date of joining.

        Args:
            doj (str): The date of joining in "YYYY-MM-DD" format.

        Returns:
            list[Employee]: A list of employees with the matching date of joining.
        """
        return db_session.query(Employee).filter(Employee.doj == doj).all()

    def search_by_grade(self, grade: str):
        """
        Searches employees by their grade.

        Args:
            grade (str): The grade to search.

        Returns:
            list[Employee]: A list of employees with the matching grade.
        """
        return db_session.query(Employee).filter(Employee.grade == grade).all()

    def upload_csv(self, content: str, db):
        """
        Parses a CSV file and uploads the employee data into the database.

        Args:
            content (str): The content of the CSV file as a string.
            db (Session): The database session used for committing data.

        Raises:
            Exception: If an error occurs during CSV processing or database insertion.
        """
        try:
            csv_data = csv.DictReader(content.splitlines())  # Parse the CSV content

            for row in csv_data:
                # Convert `dob` and `doj` to `datetime.date` objects
                dob = datetime.strptime(row["dob"], "%Y-%m-%d").date()
                doj = datetime.strptime(row["doj"], "%Y-%m-%d").date()

                # Create a new employee object from each row
                new_employee = Employee(
                    emp_id=int(row["emp_id"]),
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    dob=dob,
                    doj=doj,
                    grade=row["grade"],
                )
                db.add(new_employee)  # Add to the session

            db.commit()  # Commit all changes
        except Exception as e:
            db.rollback()  # Rollback if any error occurs
            raise Exception(f"Error processing the CSV: {str(e)}")
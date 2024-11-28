import models as models
from models import Employee
from database import session as db_session, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)


class Main:
    """
    Business logic class for performing CRUD operations on the Employee model.
    """

    def update_location(self, num: int, location: str):
        """
        Update the location of an employee.

        Args:
            num (int): The employee number.
            location (str): The new location for the employee.

        Returns:
            Employee: The updated employee object if the update is successful.
            None: If the employee is not found.
        """
        db_employee = db_session.query(Employee).filter(Employee.num == num).first()
        if db_employee:
            db_employee.location = location
            db_session.commit()
            db_session.refresh(db_employee)
        return db_employee

    def view_all(self):
        """
        Retrieve all employees from the database.

        Returns:
            list[Employee]: A list of all employees.
        """
        return db_session.query(Employee).all()

    def view_number(self, num: int):
        """
        Retrieve an employee by their employee number.

        Args:
            num (int): The employee number.

        Returns:
            Employee: The employee object if found.
            None: If no employee is found with the given number.
        """
        return db_session.query(Employee).filter(Employee.num == num).first()

    def view_location(self, location: str):
        """
        Retrieve employees by their location.

        Args:
            location (str): The location to filter employees by.

        Returns:
            list[Employee]: A list of employees located in the specified location.
            list: An empty list if no employees are found at the location.
        """
        return db_session.query(Employee).filter(Employee.location == location).all()


    # print(view_all())
    # print(view_number(1))
    # print(view_location("Chennai"))
    # print(update_location(2,"Pune"))
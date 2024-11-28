from sqlalchemy import Column, Integer, String
from database import Base


class Employee(Base):
    """
    ORM model representing the Employee table in the database.

    Attributes:
        num (int): The primary key, representing the employee number.
        name (str): The name of the employee.
        location (str): The location of the employee.
        dept_id (int): The ID of the department to which the employee belongs.
    """

    __tablename__ = 'employees'

    num = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    dept_id = Column(Integer, index=True)

    def __repr__(self):
        """
        Returns a string representation of the Employee instance.

        Returns:
            str: A formatted string with employee details.
        """
        return (
            f"Employee number={self.num}, "
            f"name={self.name}, "
            f"location={self.location}, "
            f"Department ID={self.dept_id}"
        )

# from emplo import Employee

# class Logic:
#     def __init__(self):
#         self.employee=[]

#     def view_empno(self,empno):
#         empno_list=[]
#         for i in self.tasks:
#             if i.empno == empno:
#                 empno_list.append(i)
#         if empno_list:
#             return empno_list
#         else:
#             return False
            
#     def view_all(self):
#         return self.employee
    
#     def view_location(self,location):
#         locate=[]
#         for i in self.employee:
#             if i.location == location:
#                 locate.append(i)
#         if locate:
#             return locate
#         else:
#             return False
    
#     def update(self,empno,location):
#         for i in self.employee:
#             if i.empno==empno:
#                 i.location==location
#                 return True
#             else:
#                 return False
            
                
from db import Database
from emplo import Employee

class Logic:
    def __init__(self, db_name="employees1.db"):
        self.db = Database(db_name)

    def view_empno(self, empno):
        """View employee details by employee number."""
        self.db.cursor.execute("SELECT empno, empname, location, deptid FROM employees WHERE empno = ?", (empno,))
        row = self.db.cursor.fetchone()
        if row:
            return Employee(*row)
        else:
            return False

    def view_all(self):
        """View details of all employees."""
        self.db.cursor.execute("SELECT empno, empname, location, deptid FROM employees")
        rows = self.db.cursor.fetchall()
        employees = [Employee(empno, empname, location, deptid) for empno, empname, location, deptid in rows]

        return employees

    def view_location(self, location):
        """View employee details by location."""
        self.db.cursor.execute("SELECT empno, empname, location, deptid FROM employees WHERE location = ?", (location,))
        rows = self.db.cursor.fetchall()
        employees = [Employee(empno, empname, location, deptid) for empno, empname, location, deptid in rows]
        
        return employees

    def update(self, empno, location):
        """Update the location of an employee by employee number."""
        self.db.cursor.execute("UPDATE employees SET location = ? WHERE empno = ?", (location, empno))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def close(self):
        """Close the database connection."""
        return self.db.close()
from main import Main
from models import Employee

# Initialize the Logic manager
lo = Main()

# View all employees
va = lo.view_all()
print("All employees:")
for emp in va:
    print(emp)

# View employee based on empno
vs = lo.view_number(2)
print("Based on empno:")
if vs:
    print(vs)
else:
    print("No employees found with this empno")


# View employees based on location
vp = lo.view_location("Chennai")
print("Based on location:")
if vp:
    for emp in vp:
        print(emp)
else:
    print("No employees found at this location")

# Update the location of an employee
lu = lo.update_location(3, "Mumbai")
if lu:
    print("Empno is updated")
else:
    print("Empno is not found")








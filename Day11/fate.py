# from logic import Logic
# from emplo import Employee

# def fate():
#     print(f"Hello")
   
# if __name__ == "__main__":
#     #fate()

#     lo=Logic()

#     lu=lo.update(1,"Chennai")
#     if lu==True:
#         print("Empno is updated")
#     else:
#         print("Empno is not found")


#     va=lo.view_all()
#     print("All employees:")
#     for i in va:
#         print(i)

#     vp=lo.view_location("Chennai")
#     print("Based on location:")
#     for i in vp:
#         print(i)

#     vs=lo.view_empno(1)
#     print("Based on empno:")
#     for i in vs:
#         print(i)


from logic import Logic
from emplo import Employee

# Initialize the Logic manager
lo = Logic()

# Update the location of an employee
lu = lo.update(1, "Chennai")
if lu:
    print("Empno is updated")
else:
    print("Empno is not found")

# View all employees
va = lo.view_all()
print("All employees:")
for emp in va:
    print(emp)

# View employees based on location
vp = lo.view_location("Chennai")
print("Based on location:")
if vp:
    for emp in vp:
        print(emp)
else:
    print("No employees found at this location")

# View employee based on empno
vs = lo.view_empno(1)
print("Based on empno:")
if vs:
    for emp in vs:
        print(emp)
else:
    print("No employees found with this empno")

# Close the database connection
lo.close()
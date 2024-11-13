import csv

class Emp:

    def __init__(self,empno,deptid):
        self.empno=empno
        self.deptid=deptid

    
    def to_csv_row(self):
        return [self.empno,self.deptid]
    
    def __str__(self):
        return f"emp no:{self.empno}, dept id:{self.deptid}"
        
    @classmethod
    def from_csv_row(cls, row):
        empno,deptid=row
        return cls(int(empno),int(deptid))
        
    

    
def write_products_to_csv(emp_obj, filename='emp.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['empno','dept_id'])
        writer.writerow(emp_obj.to_csv_row())

def read_products_from_csv(filename='emp.csv'):
    emp=[]
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            emp_object= Emp.from_csv_row(row)
            emp.append(emp_detail)
        
    return emp

emp_obj_from_file=Emp(1,2)
print(emp_obj_from_file)
# emp_obj1=Emp(10,30)
# write_products_to_csv(emp_obj1)
class rect():
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        area=(self.l)*(self.b)
        return area

    
    def perimeter(self):
        perimeter=2*((self.l)+(self.b))
        return perimeter
    
r=rect(4,5)
r1=rect(5,6)
print(r.area())
print(r1.area())
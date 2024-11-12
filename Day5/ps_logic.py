from PS1_task import product

class Logic:
    def __init__(self):
        self.products=[]

    def add_product(self,ad):
        for i in self.products:
            if i.id==ad.id:
                return False
        self.products.append(ad)  
        return True
    
    def update(self,id,name,price):
        for i in self.products:
            if i.id==id:
                i.name==name
                i.price==price
                return True
            else:
                return False
            
    def view_all(self):
        return self.products
    
    def discount(self,percentage):
        for i in self.products:
            i.price=i.price-(i.price*percentage//100)
        return False


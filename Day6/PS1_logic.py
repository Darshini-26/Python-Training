# Importing necessary modules
from PS1_product import Product


class Logic:
    """A class to represent the operations done in a product Management System"""

    def __init__(self):
        """Initialize an empty list to store products."""
        self.products=[]
    
    def add_product(self,new_product):
        """Add a new product to the product list if it doesn't already exist."""
        for i in self.products:
            if i.id==new_product.id:
                return False
        self.products.append(new_product)  
        return True
    
    def update(self,updated_product):
        """Update the name and price of an existing product by its ID."""
        for i in self.products:
            if i.id==updated_product.id:
                i.price=updated_product.price
                return True
        return False
            
    def view_all(self):
        """Retrieve the list of all products."""
        return self.products
    
    def discount(self,percentage):
        """Apply a discount to the price of all products."""
        discount_applied=False
        for i in self.products:
            i.price=i.price-(i.price*percentage//100)
            discount_applied=True
        return discount_applied
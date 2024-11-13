#Importing necessary modules
from PS1_product import Product
import csv


class Logic:
    """A class to represent the operations done in a product Management System"""

    def __init__(self):
        """Initialize an empty list to store products."""
        self.products=[]

    def write_products_to_csv(self, filename='products.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file) #  we want the write function with respect to csv
        
            writer.writerow(['product_id', 'name', 'price'])
        
        # Write each product as a row in the CSV
            for i in self.products:
                writer.writerow(i.to_csv_row())  #writes the csv content you gave into the file
               
#write_products_to_csv(products)


#Read products from a CSV file and return a list of Product objects
    def read_products_from_csv(filename='products.csv'):
        products=[]
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            
            # Skip the header row
            next(reader)
            
            # Read each row and create a Product object
            for row in reader:
                product = Product.from_csv_row(row)# this row contains list of values separated by ,
                products.append(product)
        
        return products
    
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
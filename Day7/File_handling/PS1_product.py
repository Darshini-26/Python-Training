class Product:

    """Initialize the product with id,name and price"""
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def __str__(self):
        """Return a string representation of the  objects."""
        return f"id :{self.id} name :{self.name} price: {self.price}"
    
    def to_csv_row(self):
        return [self.id, self.name, self.price]

    # Class method to create a Product from a CSV row (to read from CSV)
    @classmethod
    def from_csv_row(cls, row):
        product_id, name, price = row
        return cls(int(product_id), name,float(price))
    

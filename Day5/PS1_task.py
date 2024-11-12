class Product:

    """Initialize the product with id,name and price"""
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def __str__(self):
        """Return a string representation of the  objects."""
        return f"id :{self.id} name :{self.name} price: {self.price}"
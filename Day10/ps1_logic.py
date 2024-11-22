from ps1_product import Product
from ps1_update import Update
from ps1_db import Database
import sqlite3

class Logic:
    """A class to represent the operations done in a product Management System"""
    def __init__(self):
        """Initialize the database connection."""
        self.db = Database()

    def add_product(self, product):
        """Add a new product to the database."""
        try:
            self.db.cursor.execute("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", 
                                (product.id, product.name, product.price))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def update_product(self, product):
        """Update the price of an existing product by its ID."""
        self.db.cursor.execute("UPDATE products SET price = ? WHERE id = ?", 
                            (product.price, product.id))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def view_all_products(self):
        """Retrieve the list of all products."""
        self.db.cursor.execute("SELECT * FROM products")
        products = self.db.cursor.fetchall()
        return [Product(*product) for product in products]

    def apply_discount(self, percentage):
        """Apply a discount to the price of all products."""
        self.db.cursor.execute("UPDATE products SET price = price - (price * ? / 100)", (percentage,))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def close(self):
        """Close the database connection."""
        self.db.conn.close()



    
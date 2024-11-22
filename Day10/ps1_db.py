import sqlite3


class Database:
    """A class to represent the database operations."""

    def __init__(self, db_name="ps1_products.db"):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

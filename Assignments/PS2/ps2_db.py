import sqlite3

class Database:
    def __init__(self, db_name="orders.db"):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                products TEXT,
                total REAL
            )
        ''')
        self.conn.commit()
    
    def close(self):
        """Close the database connection."""
        self.conn.close()


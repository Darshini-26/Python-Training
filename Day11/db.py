import sqlite3

class Database:
    def __init__(self, db_name="employees1.db"):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the employees table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                empno INTEGER PRIMARY KEY,
                empname TEXT NOT NULL,
                location TEXT NOT NULL,
                deptid INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()
        return True
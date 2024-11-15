import sqlite3

# Connect to the SQLite database (it will create the database file if it doesn't exist)
connection = sqlite3.connect('my_database.db')  # 'my_database.db' is the database file

#prove that you have got connection

# Create a cursor object to execute SQL commands
cursor = connection.cursor()


# Create a table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Name is {self.name} age is {self.age}"

#user_obj=User("sarah",7)

# Insert a record into the table
def query(user_obj):
    insert_query = 'INSERT INTO users (name, age) VALUES (?, ?)'
    cursor.execute(insert_query, (user_obj.name,user_obj.age))

# Commit the transaction to save changes to the database
connection.commit()

# Query to retrieve all records from the users table
cursor.execute('SELECT * FROM users')

# Fetch all rows from the executed query
rows = cursor.fetchall()

new_list=[]
for i in rows:
    user=User("Sara",30)
    new_list.append(user)

for u in new_list:
    print(user)


# Print the data
# print("Data in users table:")
# for row in rows:
#     print(row)

# Close the cursor and connection
cursor.close()
connection.close()
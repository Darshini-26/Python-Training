import sqlite3
from sqlite3 import IntegrityError

# Establish database connection and cursor
connection = sqlite3.connect('medical_db.db')
cursor = connection.cursor()

# Create the patients table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob TEXT,
    phone_number TEXT,
    email TEXT UNIQUE
)
''')

def insert_patient(first_name, last_name, dob, phone_number, email):
    """Inserts a new patient into the database."""
    try:
        cursor.execute('''
        INSERT INTO patients (first_name, last_name, dob, phone_number, email)
        VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, dob, phone_number, email))
        connection.commit()
        return f"Patient {first_name} {last_name} added successfully."
    except IntegrityError as e:
        return f"Error: {e}"

def update_patient(patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
    """Updates an existing patient's details in the database."""
    try:
        cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        patient = cursor.fetchone()
        
        if patient:
            update_query = "UPDATE patients SET"
            values = []
            
            if first_name:
                update_query += " first_name = ?,"
                values.append(first_name)
            if last_name:
                update_query += " last_name = ?,"
                values.append(last_name)
            if dob:
                update_query += " dob = ?,"
                values.append(dob)
            if phone_number:
                update_query += " phone_number = ?,"
                values.append(phone_number)
            if email:
                update_query += " email = ?,"
                values.append(email)
                
            update_query = update_query.rstrip(',')
            update_query += " WHERE patient_id = ?"
            values.append(patient_id)
            
            cursor.execute(update_query, tuple(values))
            connection.commit()
            return f"Patient ID {patient_id} updated successfully."
        else:
            return f"Error: Patient with ID {patient_id} not found."
    except Exception as e:
        return f"Error: {e}"

def select_patient_by_id(patient_id):
    """Selects a patient by their ID."""
    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    return cursor.fetchone()

def select_patient_by_phone(phone_number):
    """Selects a patient by their phone number."""
    cursor.execute("SELECT * FROM patients WHERE phone_number = ?", (phone_number,))
    return cursor.fetchall()

def close_connection():
    """Closes the database connection."""
    cursor.close()
    connection.close()

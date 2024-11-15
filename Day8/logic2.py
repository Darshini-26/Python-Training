from db2 import insert_patient, update_patient, select_patient_by_id, select_patient_by_phone, close_connection

def add_patient(first_name, last_name, dob, phone_number, email):
    """Wrapper function to add a new patient."""
    return insert_patient(first_name, last_name, dob, phone_number, email)

def modify_patient(patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
    """Wrapper function to update an existing patient."""
    return update_patient(patient_id, first_name, last_name, dob, phone_number, email)

def find_patient_by_id(patient_id):
    """Wrapper function to find a patient by ID."""
    patient = select_patient_by_id(patient_id)
    return f"Patient Found: {patient}" if patient else f"Error: No patient found with ID {patient_id}."

def find_patient_by_phone(phone_number):
    """Wrapper function to find a patient by phone number."""
    patients = select_patient_by_phone(phone_number)
    if patients:
        result = "Patients Found:\n" + "\n".join(str(patient) for patient in patients)
        return result
    else:
        return f"Error: No patient found with phone number {phone_number}."

def close_db():
    """Wrapper function to close the database connection."""
    close_connection()

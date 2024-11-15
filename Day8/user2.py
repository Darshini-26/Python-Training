import logic2 as logic2

# Insert test data
print(logic2.add_patient('a', 'b', '1985-06-15', '123-456-7890', 'a@poc.com'))
print(logic2.add_patient('c', 'd', '1992-02-20', '987-654-3210', 'de@poc.com'))
print(logic2.add_patient('e', 'f', '1975-08-25', '555-444-3333', 're@poc.com'))

# Attempt to insert a patient with a duplicate email
print(logic2.add_patient('abc', 'def', '1990-10-10', '123-123-1234', 'abcdef@poc.com'))

# Update a patient with ID 1
print(logic2.modify_patient(1, phone_number='111-222-3333', email='freak@poc.com'))

# Attempt to update a non-existent patient
print(logic2.modify_patient(999, phone_number='000-000-0000'))

# Select patients by ID
print(logic2.find_patient_by_id(1))
print(logic2.find_patient_by_id(999))

# Select patients by phone number
print(logic2.find_patient_by_phone('987-654-3210'))
print(logic2.find_patient_by_phone('000-000-0000'))

# Close the database connection
logic2.close_db()

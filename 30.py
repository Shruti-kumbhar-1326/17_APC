# 30. Patient records

patients = (
    (101, "Amit", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Rahul", 28, "O+"),
    (104, "Priya", 22, "A+")
)

# Display all records
print("All Patient Records:")

for patient in patients:
    print(patient)

# Search patient by ID
patient_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient Found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if not found:
    print("Patient not found")

# Count total patients
print("\nTotal number of patients:", len(patients))

# Display patients with specific blood group
blood_group = input("\nEnter blood group: ")

print("Patients with", blood_group, "blood group:")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
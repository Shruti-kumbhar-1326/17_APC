# Open the file in read mode
file = open("students.txt", "r")

# Read all records
records = file.readlines()

# Close the file
file.close()

# Remove the header
records = records[1:]

# Variables
total_marks = 0
highest_marks = -1
highest_student = ""

print("All Student Records:")
print("--------------------")

# Process each record
for record in records:
    roll_no, name, marks = record.strip().split(",")

    marks = int(marks)

    # Display record
    print("Roll No:", roll_no, "Name:", name, "Marks:", marks)

    # Calculate total marks
    total_marks += marks

    # Find highest marks
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

# Calculate average
average = total_marks / len(records)

print("\nStudent with Highest Marks:")
print("Name:", highest_student)
print("Marks:", highest_marks)

print("\nAverage Marks:", average)

# Display students scoring more than 80
print("\nStudents who scored more than 80:")
for record in records:
    roll_no, name, marks = record.strip().split(",")
    marks = int(marks)

    if marks > 80:
        print(name, "-", marks)
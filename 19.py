# Function to read attendance records
def read_records():
    file = open("attendance.txt", "r")
    records = file.readlines()
    file.close()

    students = []

    # Skip the header
    for record in records[1:]:
        roll_no, name, present, total = record.strip().split(",")

        student = {
            "roll_no": roll_no,
            "name": name,
            "present": int(present),
            "total": int(total)
        }

        students.append(student)

    return students


# Function to calculate attendance percentage
def attendance_percentage(student):
    return (student["present"] / student["total"]) * 100


# Function to display students below 75%
def below_75(students):
    print("Students having attendance below 75%:")
    print("---------------------------------------")

    for student in students:
        percentage = attendance_percentage(student)

        if percentage < 75:
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Attendance:", percentage, "%")
            print()


# Main program
students = read_records()

# Display attendance percentage of all students
print("Attendance Percentage:")
print("----------------------")

for student in students:
    percentage = attendance_percentage(student)
    print(student["name"], ":", percentage, "%")

print()

# Display students below 75%
below_75(students)
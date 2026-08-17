# 4. Update student marks

marks = {
    "Amit": 75,
    "Sneha": 85,
    "Rahul": 70,
    "Priya": 90
}

name = input("Enter student name: ")

if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
    print("Updated dictionary:", marks)
else:
    print("Student not found")
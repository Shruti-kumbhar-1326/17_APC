# 10. Accept five student names and marks

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks

print("Student dictionary:")
print(students)
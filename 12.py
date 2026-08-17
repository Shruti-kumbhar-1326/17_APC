# 12. Find student with lowest marks

students = {
    "Amit": 75,
    "Sneha": 92,
    "Rahul": 60,
    "Priya": 88
}

lowest_student = ""
lowest_marks = None

for name, marks in students.items():
    if lowest_marks is None or marks < lowest_marks:
        lowest_marks = marks
        lowest_student = name

print("Lowest marks:", lowest_marks)
print("Student:", lowest_student)
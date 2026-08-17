# 11. Find student with highest marks

students = {
    "Amit": 75,
    "Sneha": 92,
    "Rahul": 80,
    "Priya": 88
}

highest_student = ""
highest_marks = 0

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

print("Highest marks:", highest_marks)
print("Student:", highest_student)
# 13. Calculate average marks

students = {
    "Amit": 75,
    "Sneha": 92,
    "Rahul": 80,
    "Priya": 88
}

total = 0

for marks in students.values():
    total = total + marks

average = total / len(students)

print("Average marks:", average)
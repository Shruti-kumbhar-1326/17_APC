# 15. Nested tuple containing student details

students = (
    (101, "Amit", 85),
    (102, "Sneha", 90),
    (103, "Rahul", 78)
)

for student in students:
    print("Roll No:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])
    print()
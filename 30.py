# 30. Group students according to department

students = {
    "Amit": "CSE",
    "Sneha": "IT",
    "Rahul": "CSE",
    "Priya": "ENTC",
    "Riya": "IT"
}

groups = {}

for name, department in students.items():

    if department not in groups:
        groups[department] = []

    groups[department].append(name)

print("Students grouped by department:")

for department, names in groups.items():
    print(department, ":", names)
# 26. Employee salary operations

employees = {
    "Amit": 45000,
    "Sneha": 60000,
    "Rahul": 55000,
    "Priya": 40000
}

highest = max(employees.values())
lowest = min(employees.values())

average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)
# 6. Check employee ID

employees = {
    101: "Amit",
    102: "Sneha",
    103: "Rahul",
    104: "Priya"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists")
    print("Name:", employees[emp_id])
else:
    print("Employee does not exist")
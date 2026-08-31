# Function to read employee records
def read_employees():
    file = open("employees.txt", "r")
    records = file.readlines()
    file.close()

    employees = []

    # Skip header
    for record in records[1:]:
        emp_id, name, department, salary = record.strip().split(",")

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": float(salary)
        }

        employees.append(employee)

    return employees


# Function to display all employees
def display_employees(employees):
    print("\nAll Employees:")
    for emp in employees:
        print(emp["id"], emp["name"], emp["department"], emp["salary"])


# Function to find highest-paid employee
def highest_paid(employees):
    highest = max(employees, key=lambda emp: emp["salary"])

    print("\nHighest-Paid Employee:")
    print("ID:", highest["id"])
    print("Name:", highest["name"])
    print("Department:", highest["department"])
    print("Salary:", highest["salary"])


# Function to calculate average salary
def average_salary(employees):
    total = 0

    for emp in employees:
        total += emp["salary"]

    average = total / len(employees)

    print("\nAverage Salary:", average)


# Function to display employees above given salary
def above_salary(employees, salary):
    print("\nEmployees earning above", salary, ":")

    for emp in employees:
        if emp["salary"] > salary:
            print(emp["name"], "-", emp["salary"])


# Main program
employees = read_employees()

display_employees(employees)

highest_paid(employees)

average_salary(employees)

salary = float(input("\nEnter salary limit: "))
above_salary(employees, salary)
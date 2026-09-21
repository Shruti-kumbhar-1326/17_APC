class Employee:
    def calculate_salary(self):
        print("Employee Salary")


class Manager(Employee):
    def calculate_salary(self):
        salary = 50000
        print("Manager Salary =", salary)


class Developer(Employee):
    def calculate_salary(self):
        salary = 40000
        print("Developer Salary =", salary)


class Tester(Employee):
    def calculate_salary(self):
        salary = 30000
        print("Tester Salary =", salary)


# Create objects
employees = [Manager(), Developer(), Tester()]

# Runtime Polymorphism
for employee in employees:
    employee.calculate_salary()
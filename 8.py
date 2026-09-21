class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


class Manager(Employee):
    def total_salary(self):
        return self.salary + self.salary * 0.30


class Developer(Employee):
    def total_salary(self):
        return self.salary + self.salary * 0.20


class Tester(Employee):
    def total_salary(self):
        return self.salary + self.salary * 0.10


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Sneha", 30000)

print("Manager Salary =", m.total_salary())
print("Developer Salary =", d.total_salary())
print("Tester Salary =", t.total_salary())
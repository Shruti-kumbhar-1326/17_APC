class Person:
    def display_role(self):
        print("Person")


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


# Store all objects in a list
people = [
    Student(),
    Faculty(),
    Administrator()
]

# Invoke the same method using a loop
for person in people:
    person.display_role()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name =", self.name)
        print("Age =", self.age)
        print("Roll No =", self.roll_no)
        print("Course =", self.course)
        print("Research Topic =", self.topic)
        print("Guide Name =", self.guide)


# Create object
r = ResearchStudent(
    "Rahul",
    21,
    101,
    "M.Tech",
    "Artificial Intelligence",
    "Dr. Sharma"
)

# Display details
r.display()
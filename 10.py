class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


# Create two students
s1 = Student("Rahul", 450)
s2 = Student("Amit", 400)

# Compare marks
if s1 > s2:
    print(s1.name, "has more marks than", s2.name)

if s1 < s2:
    print(s1.name, "has fewer marks than", s2.name)
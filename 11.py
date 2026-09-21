class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def percentage(self):
        return self.total() / 3

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A"
        elif p >= 75:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 40:
            return "D"
        else:
            return "F"


r = Result(101, "Rahul", "CSE", 80, 75, 90)

print("Roll No =", r.roll_no)
print("Name =", r.name)
print("Course =", r.course)
print("Total =", r.total())
print("Percentage =", r.percentage())
print("Grade =", r.grade())
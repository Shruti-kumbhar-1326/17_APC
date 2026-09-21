class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

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

    def __del__(self):
        print("Student Result Object Destroyed")


s = StudentResult("Rahul", [80, 75, 90, 85, 70])

print("Name =", s.name)
print("Total =", s.total())
print("Percentage =", s.percentage())
print("Grade =", s.grade())

del s
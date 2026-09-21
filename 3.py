class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        return self.marks + self.points


s = Student(80, 15)

print("Academic Marks =", s.marks)
print("Sports Points =", s.points)
print("Overall Performance =", s.performance())
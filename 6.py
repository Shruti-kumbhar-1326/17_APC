class Student:
    def calculate_grade(self, marks):
        print("Student Grade")


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            print("Engineering Student Grade = A")
        elif marks >= 60:
            print("Engineering Student Grade = B")
        else:
            print("Engineering Student Grade = C")


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            print("Medical Student Grade = A")
        elif marks >= 50:
            print("Medical Student Grade = B")
        else:
            print("Medical Student Grade = C")


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            print("Management Student Grade = A")
        elif marks >= 50:
            print("Management Student Grade = B")
        else:
            print("Management Student Grade = C")


# Create objects
students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

marks = 75

# Runtime Polymorphism
for student in students:
    student.calculate_grade(marks)
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print("----------------------")


# Creating objects for multiple students
s1 = Student(101, "Rahul", [80, 75, 90, 85, 70])
s2 = Student(102, "Amit", [70, 65, 80, 75, 85])
s3 = Student(103, "Sneha", [90, 85, 95, 88, 92])

# Displaying student details
s1.display()
s2.display()
s3.display()
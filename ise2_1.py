marks = []
n = int(input("Enter number of students: "))
for i in range(n):
    mark = float(input("Enter marks of student : "))
    marks.append(mark)
maximum = max(marks)
minimum = min(marks)
average = sum(marks) / n
above_average = sum(1 for mark in marks if mark > average)
print("Maximum marks:", maximum)
print("Minimum marks:", minimum)
print("Average marks:", average)
print("Number of students above average:", above_average)

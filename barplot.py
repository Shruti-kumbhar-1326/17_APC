import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "DBMS"]
marks = [80, 70, 85, 75]

plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
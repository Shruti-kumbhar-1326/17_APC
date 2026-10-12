import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "DBMS"]
marks = [80, 70, 85, 75]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()
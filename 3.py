#3.	Write a program to append additional student information to an existing file without deleting its previous contents
file = open("student.txt","a")
file.write("\nAdditional Information:\n")
file.write("Age: 20\n")
file.write("City: Kolhapur\n")
file.close()
print("Additional student information added successfully!")
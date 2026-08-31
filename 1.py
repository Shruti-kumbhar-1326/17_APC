#1.	Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.
file = open("student.txt","w")
file.write("Name: Shruti\n")
file.write("Roll No: 17\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semister: 5\n")
file.close()
print("Studdent details written sucessfully.")
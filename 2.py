#2.	Write a program to open a text file and display its complete contents.
file = open("student.txt","r")
content = file.read()
print(content)
file.close()
#5.	Write a program to count and display the total number of lines present in a text file.
file = open("student.txt","r")
count = 0
for line in file:
    count += 1
file.close
print("Total number of lines:",count)
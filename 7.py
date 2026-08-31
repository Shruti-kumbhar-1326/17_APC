#7.	Write a program to count the total number of characters in a text file, including spaces.
# Open the file in read mode
file = open("student.txt", "r")

# Read the complete file
content = file.read()

# Count total characters including spaces
count = len(content)

# Close the file
file.close()

print("Total number of characters:", count)
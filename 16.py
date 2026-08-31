#16.	Read a text file and create another file containing the same text in uppercase.
# Open the original file in read mode
file = open("student.txt", "r")

# Read the complete content
content = file.read()

# Close the original file
file.close()

# Convert content to uppercase
content = content.upper()

# Create a new file and write the uppercase content
new_file = open("uppercase_student.txt", "w")

new_file.write(content)

# Close the new file
new_file.close()

print("File converted to uppercase successfully.")
print("New file created: uppercase_student.txt")
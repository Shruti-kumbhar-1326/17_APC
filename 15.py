#15.	Read a Python source file and create another file after removing single-line comments
# Open the Python source file in read mode
file = open("14.py", "r")

# Create a new file for the modified code
new_file = open("without_comments.py", "w")

# Read the file line by line
for line in file:
    # Remove single-line comments
    if "#" in line:
        line = line.split("#")[0]

    # Write the remaining code
    new_file.write(line)

# Close both files
file.close()
new_file.close()

print("Single-line comments removed successfully.")
print("New file created: without_comments.py")
# Open the first file in read mode
file1 = open("file1.txt", "r")
content1 = file1.read()
file1.close()

# Open the second file in read mode
file2 = open("file2.txt", "r")
content2 = file2.read()
file2.close()

# Create the third file
file3 = open("file3.txt", "w")

# Write contents of both files
file3.write(content1)
file3.write("\n")
file3.write(content2)

# Close the third file
file3.close()

print("Contents of both files merged successfully.")
print("New file created: file3.txt")
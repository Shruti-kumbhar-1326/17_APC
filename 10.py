#10.	Read a text file and calculate the number of alphabets, digits, spaces, and special characters
# Open the file in read mode
file = open("student.txt", "r")

# Read the complete file
content = file.read()

# Initialize counters
alphabets = 0
digits = 0
spaces = 0
special = 0

# Check each character
for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special += 1

# Close the file
file.close()

# Display the results
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)
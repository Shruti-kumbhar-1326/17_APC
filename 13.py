#13.	Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
# Accept a word from the user
search_word = input("Enter a word to search: ")

# Open the file in read mode
file = open("student.txt", "r")

count = 0
line_numbers = []

# Read the file line by line
for line_number, line in enumerate(file, start=1):
    words = line.split()

    for word in words:
        if word.lower() == search_word.lower():
            count += 1
            if line_number not in line_numbers:
                line_numbers.append(line_number)

# Close the file
file.close()

# Display the result
print("Number of occurrences:", count)

if count > 0:
    print("Word found on line(s):", line_numbers)
else:
    print("Word not found in the file.")
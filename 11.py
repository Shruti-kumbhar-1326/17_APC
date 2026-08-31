#11.	Read a text file and find the longest word present in the file.
# Open the file in read mode
file = open("student.txt", "r")

# Read the complete file
content = file.read()

# Split content into words
words = content.split()

# Find the longest word
longest_word = max(words, key=len)

# Close the file
file.close()

# Display the result
print("Longest word:", longest_word)
print("Length:", len(longest_word))
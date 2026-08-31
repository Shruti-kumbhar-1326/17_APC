#12.	Read a text file and count how many times each word occurs. Display the result using a dictionary
# Open the file in read mode
file = open("student.txt", "r")

# Read the complete file
content = file.read()

# Convert content into words
words = content.split()

# Create an empty dictionary
word_count = {}

# Count each word
for word in words:
    word = word.lower()

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Close the file
file.close()

# Display the result
print("Word Frequency:")

for word, count in word_count.items():
    print(word, ":", count)
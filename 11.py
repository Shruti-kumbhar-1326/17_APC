# Program to count the number of words using ASCII value

string = input("Enter a sentence: ")

count = 1

for ch in string:
    if ord(ch) == 32:      # ASCII value of space is 32
        count += 1

print("Total number of words:", count)
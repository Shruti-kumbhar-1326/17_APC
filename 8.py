# Program to find the frequency of a character

string = input("Enter a string: ")
ch = input("Enter the character to find: ")

count = 0

for i in string:
    if i == ch:
        count += 1

print("Frequency of", ch, "is:", count)
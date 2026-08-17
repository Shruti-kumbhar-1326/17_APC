# Program to display ASCII value of each character in a string

string = input("Enter a string: ")

for ch in string:
    print(ch, "=", ord(ch))
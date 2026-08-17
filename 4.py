# Program to check whether a string is palindrome

string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")
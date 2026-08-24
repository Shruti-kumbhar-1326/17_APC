#11.	Write a function that accepts a string and returns its reverse
def reverse_string(string):
    return string[::-1]

string = input("Enter a string: ")

print("Reverse =", reverse_string(string))
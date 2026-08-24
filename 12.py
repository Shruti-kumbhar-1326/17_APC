#12.	Create a function that checks whether a given string or number is a palindrome
def is_palindrome(value):
    value = str(value)
    
    if value == value[::-1]:
        return True
    else:
        return False


value = input("Enter a string or number: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not a Palindrome")
#31.	Check whether a string is a palindrome using recursion.
def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


string = input("Enter a string: ")

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")
# Program to count uppercase and lowercase letters

string = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in string:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
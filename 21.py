#Password Validator
password = input("Enter Password: ")

upper = lower = digit = special = 0

if len(password) >= 8:

    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        else:
            special += 1

    if upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Password must be at least 8 characters long")
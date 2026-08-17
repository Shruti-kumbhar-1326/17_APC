# Program to print duplicate characters in a string

string = input("Enter a string: ")

print("Duplicate characters are:")

for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            count += 1

    if count > 1:
        printed = False
        for k in range(i):
            if string[i] == string[k]:
                printed = True
                break

        if not printed:
            print(string[i])
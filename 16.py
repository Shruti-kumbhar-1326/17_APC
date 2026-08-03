# Program to display the frequency of every character

string = input("Enter a string: ")

for i in range(len(string)):
    count = 0
    printed = False

    # Check if character is already printed
    for k in range(i):
        if string[i] == string[k]:
            printed = True
            break

    if not printed:
        # Count frequency
        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1

        print(string[i], "=", count)
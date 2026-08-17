#substring search
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in main_string:
    print("Substring found.")
else:
    print("Substring not found.")
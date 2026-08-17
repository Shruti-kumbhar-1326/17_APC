# Remove duplicate character
str1 = input("Enter a string: ")

result = ""

for ch in str1:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)
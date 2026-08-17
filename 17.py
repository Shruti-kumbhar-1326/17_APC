str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert to lowercase
str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")
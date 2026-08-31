#9.	Read a text file and count the number of vowels and consonants present in the file.
file = open("student.txt","r")
content = file.read()
vowels = 0
consonants = 0
for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
file.close()
print("Total vowels:",vowels)
print("Total consonants:",consonants)
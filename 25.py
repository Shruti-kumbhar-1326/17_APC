#second most freqent character 
string = input("Enter a string: ")

max1 = 0
max2 = 0
char1 = ""
char2 = ""

for ch in string:
    count = string.count(ch)

    if count > max1:
        max2 = max1
        char2 = char1

        max1 = count
        char1 = ch

    elif count > max2 and ch != char1:
        max2 = count
        char2 = ch

print("Second most frequent character:", char2)
print("Frequency:", max2)
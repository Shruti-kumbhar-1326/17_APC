#most freqent character 
string = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in string:
    count = string.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)
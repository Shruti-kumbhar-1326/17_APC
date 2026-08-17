# 33. First non-repeated character

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

found = False

for char in text:
    if frequency[char] == 1:
        print("First non-repeated character:", char)
        found = True
        break

if not found:
    print("No non-repeated character")
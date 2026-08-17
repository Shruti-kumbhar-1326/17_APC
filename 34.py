# 35. Count words according to their length

paragraph = input("Enter a paragraph: ")

words = paragraph.split()

length_count = {}

for word in words:

    length = len(word)

    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1

print("Word length : Number of words")

for length, count in length_count.items():
    print(length, ":", count)
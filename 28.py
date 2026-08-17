#28.	Word Frequency Dictionary 
#	Count the frequency of every word in a paragraph. 

paragraph = input("Enter a paragraph: ")

words = paragraph.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
for word in freq:
    print(word, ":", freq[word])

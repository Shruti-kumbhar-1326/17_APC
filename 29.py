#29.	Sentence Reversal 
#	Reverse the order of words in a sentence without changing the words themselves. 
#	Example:
#	Input: Python is easy
#Output: easy is Python
sentence = input("Enter a sentence: ")

words = sentence.split()

reverse_sentence = ""

for i in range(len(words)-1, -1, -1):
    reverse_sentence += words[i] + " "

print("Reversed Sentence:", reverse_sentence.strip())

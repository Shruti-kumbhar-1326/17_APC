file = open("student.txt", "r")

content = file.read()

file.close()

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

modified_content = content.replace(old_word, new_word)

new_file = open("modified_student.txt", "w")

new_file.write(modified_content)

new_file.close()

print("Word replaced successfully.")
print("Modified file saved as modified_student.txt")
#8.	Store 15 integers in a list. Count how many numbers are:
#•	Even 
#•	Odd
numbers = []

for i in range(15):
    num = int(input("Enter a number: "))
    numbers.append(num)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("List:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)
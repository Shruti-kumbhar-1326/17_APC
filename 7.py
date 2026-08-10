#7.	Accept 10 numbers from the user and store them in a list. Calculate:
#•	Sum 
#•	Average 
numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

sum = 0
for num in numbers:
    sum = sum + num

average = sum / 10

print("List:", numbers)
print("Sum:", sum)
print("Average:", average)


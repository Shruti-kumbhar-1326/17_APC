#6.	Write a program to find the largest and smallest number in a list without using max() or min().
# Find largest and smallest number in a list

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)



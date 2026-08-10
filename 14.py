#14.	Create a list containing duplicate values and display only unique elements.
numbers = [10, 20, 10, 30, 20, 40, 30, 50, 10]

unique = list(set(numbers))

print("Original list:", numbers)
print("Unique elements:", unique)
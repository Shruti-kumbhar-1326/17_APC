#4.	Create a list of numbers. Add:
#•	One element at the end 
#•	One element at the beginning 
#•	One element at a specified position 
# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

print("Original number list:", numbers)

# Add one element at the end
numbers.append(60)
print("Add at end:", numbers)

# Add one element at the beginning
numbers.insert(0, 5)
print("Add at beginning:", numbers)

# Add one element at a specified position
position = int(input("Enter the position: "))
element = int(input("Enter the element: "))

numbers.insert(position, element)
print("After adding at specified position:", numbers)
#11.	Create a list of 10 numbers and display:
#	First 5 elements 
#•	Last 5 elements 
#•	Middle 4 elements 
#•	Alternate elements 
#•	Reverse list using slicing

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("List:", numbers)

# First 5 elements
print("First 5 elements:", numbers[:5])

# Last 5 elements
print("Last 5 elements:", numbers[5:])

# Middle 4 elements
print("Middle 4 elements:", numbers[3:7])

# Alternate elements
print("Alternate elements:", numbers[::2])

# Reverse list using slicing
print("Reverse list:", numbers[::-1])
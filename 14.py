import numpy as np

# Create an array containing duplicate values
arr = np.array([10, 20, 30, 20, 40, 10, 50, 30, 60, 40])

print("Original Array:")
print(arr)

# Find unique elements
unique_elements = np.unique(arr)

print("\nUnique Elements:")
print(unique_elements)
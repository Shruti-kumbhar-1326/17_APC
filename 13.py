import numpy as np

# Create an unsorted NumPy array
arr = np.array([50, 20, 80, 10, 40, 70, 30, 90])

print("Original Array:")
print(arr)

# Ascending order
ascending = np.sort(arr)

# Descending order
descending = np.sort(arr)[::-1]

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)
import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

# Sum of all elements
print("\nSum of all elements:", np.sum(arr))

# Sum of each layer
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))

# Sum along rows
print("Sum along rows:")
print(np.sum(arr, axis=2))

# Sum along columns
print("Sum along columns:")
print(np.sum(arr, axis=1))
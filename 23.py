



import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array:")
print(arr)

# Flatten the array
flat = arr.flatten()

print("\nFlattened Array:")
print(flat)
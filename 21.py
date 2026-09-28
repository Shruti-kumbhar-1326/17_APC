import numpy as np

# Create a random 3D array
arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Array:")
print(arr)

# Replace values greater than 50 with 0
arr[arr > 50] = 0

print("\nArray after replacement:")
print(arr)
import numpy as np

# Create random 3D array
arr = np.random.randint(1, 101, size=(3, 4, 5))

# Flatten the array
flat = arr.flatten()

print("3D Array:")
print(arr)

print("\nFlattened Array:")
print(flat)

# Average
average = np.mean(flat)

# Elements greater than 50
print("\nElements greater than 50:")
print(flat[flat > 50])

# Even numbers
print("\nEven numbers:")
print(flat[flat % 2 == 0])

# Elements less than average
print("\nElements less than average:")
print(flat[flat < average])
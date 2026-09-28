import numpy as np

# Create 3D array from 1 to 27
arr = np.arange(1, 28).reshape(3, 3, 3)

# Flatten the array
flat = arr.flatten()

print("Flattened Array:")
print(flat)

# Calculate values
print("\nSum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
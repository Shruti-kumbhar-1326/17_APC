import numpy as np

# Create a NumPy array from 1 to 20
arr = np.arange(1, 21)

# Boolean indexing for even numbers
even = arr[arr % 2 == 0]

# Boolean indexing for odd numbers
odd = arr[arr % 2 != 0]

# Display the results
print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)
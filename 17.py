import numpy as np

# Marks of 20 students
marks = np.array([
    65, 72, 88, 55, 90,
    76, 45, 82, 69, 95,
    60, 78, 85, 50, 73,
    92, 68, 80, 58, 87
])

# Calculate class average
average = np.mean(marks)

# Display class average
print("Class Average:", average)

# Find students who scored above average
above_average = marks[marks > average]

print("Marks above average:")
print(above_average)
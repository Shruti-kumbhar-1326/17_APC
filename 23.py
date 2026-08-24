#23.	Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def class_average(students):
    total_percentage = 0

    for student in students:
        total_percentage += student["percentage"]

    return total_percentage / len(students)


def highest_scorer(students):
    highest = students[0]

    for student in students:
        if student["percentage"] > highest["percentage"]:
            highest = student

    return highest


def lowest_scorer(students):
    lowest = students[0]

    for student in students:
        if student["percentage"] < lowest["percentage"]:
            lowest = student

    return lowest


# Student records
students = [
    {"name": "Shruti", "roll": 1, "marks": [85, 90, 78, 88, 92]},
    {"name": "Priya", "roll": 2, "marks": [75, 80, 70, 72, 78]},
    {"name": "Neha", "roll": 3, "marks": [65, 60, 72, 68, 70]}
]

# Calculate total, percentage and grade
for student in students:
    student["total"] = calculate_total(student["marks"])
    student["percentage"] = calculate_percentage(student["total"])
    student["grade"] = calculate_grade(student["percentage"])


# Display student details
print("----- STUDENT RECORDS -----")

for student in students:
    print("\nName:", student["name"])
    print("Roll Number:", student["roll"])
    print("Total:", student["total"])
    print("Percentage:", student["percentage"], "%")
    print("Grade:", student["grade"])


# Class average
print("\nClass Average =", class_average(students), "%")


# Highest scorer
highest = highest_scorer(students)
print("Highest Scorer:", highest["name"],
      "-", highest["percentage"], "%")


# Lowest scorer
lowest = lowest_scorer(students)
print("Lowest Scorer:", lowest["name"],
      "-", lowest["percentage"], "%")
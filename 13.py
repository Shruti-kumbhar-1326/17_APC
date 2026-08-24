#13.	Write a function that accepts a list of numbers and returns their average.
def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)
    return average


numbers = [10, 20, 30, 40, 50]

print("Average =", calculate_average(numbers))
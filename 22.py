#22.	Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def calculate_values(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

        total += num

    average = total / len(numbers)

    return minimum, maximum, total, average


numbers = [10, 25, 5, 40, 20]

minimum, maximum, total, average = calculate_values(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)
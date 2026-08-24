#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [10, 25, 7, 45, 18]

print("Largest element =", find_largest(numbers))
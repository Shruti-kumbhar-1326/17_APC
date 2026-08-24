#16.	Create a function to find the second-largest number in a list.
def second_largest(numbers):
    largest = numbers[0]
    second = None

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second


numbers = [10, 25, 7, 45, 18]

print("Second largest =", second_largest(numbers))
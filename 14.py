#14.	Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_element(my_list, element):
    count = 0

    for item in my_list:
        if item == element:
            count += 1

    return count


my_list = [10, 20, 10, 30, 10, 40]
element = 10

print("Number of occurrences =", count_element(my_list, element))
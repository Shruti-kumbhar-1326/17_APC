#15.	Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(my_list):
    unique = []

    for item in my_list:
        if item not in unique:
            unique.append(item)

    return unique


my_list = [10, 20, 10, 30, 20, 40, 30]

print("Unique elements =", unique_elements(my_list))
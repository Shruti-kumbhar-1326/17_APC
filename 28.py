# 28. Count frequency of each element

numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

checked = ()

for num in numbers:
    if num not in checked:
        print(num, "appears", numbers.count(num), "times")
        checked = checked + (num,)
# 32. Two sum using dictionary

numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target value: "))

seen = {}

for num in numbers:

    required = target - num

    if required in seen:
        print("Two numbers are:", required, "and", num)
        break

    seen[num] = True
else:
    print("No two numbers found")
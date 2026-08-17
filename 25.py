# 25. Calculate cricket runs

runs = (45, 67, 23, 89, 56, 72, 34, 91, 40, 65)

total = 0
highest = runs[0]
lowest = runs[0]

for run in runs:
    total = total + run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)
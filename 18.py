# 18. Find common values

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "X": 20,
    "Y": 40,
    "Z": 30
}

common = set(dict1.values()) & set(dict2.values())

print("Common values:", common)
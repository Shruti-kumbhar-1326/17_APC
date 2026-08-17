# 17. Find common keys

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "B": 40,
    "C": 50,
    "D": 60
}

common = set(dict1.keys()) & set(dict2.keys())

print("Common keys:", common)
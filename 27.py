# 27. Merge two tuples and remove duplicates

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

merged = tuple1 + tuple2

result = ()

for num in merged:
    if num not in result:
        result = result + (num,)

print("Merged tuple without duplicates:", result)
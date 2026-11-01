import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Sneha"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
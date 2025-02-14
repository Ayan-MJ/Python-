import pandas as pd

data = {
    "Name" : ["Alice", "Bob", "Charlie"],
    "Age" : [25, 30, 35],
    "City" : ["New York", "Paris", "Sydney"]
}

df = pd.DataFrame(data)
print(df)

# Selecting one column
names_only = df["Name"]
print(names_only)

# Filtering row where age is > 25
filtered_df = df[df["Age"] > 25]
print(filtered_df)

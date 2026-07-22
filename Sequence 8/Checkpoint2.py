import pandas as pd
import numpy as np

# Create the DataFrame
employees = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Bob"],
    "salary": [50000, np.nan, 60000, np.nan, 55000, 52000],
    "department": ["HR", "IT", "HR", "IT", "HR", "IT"]
}

df = pd.DataFrame(employees)

print("Original DataFrame:")
print(df)

# Replace missing salaries with the department average
df["salary"] = df["salary"].fillna(
    df.groupby("department")["salary"].transform("mean")
)

# Remove duplicate names (keeps the first occurrence)
df = df.drop_duplicates(subset="name")

print("\nUpdated DataFrame:")
print(df)
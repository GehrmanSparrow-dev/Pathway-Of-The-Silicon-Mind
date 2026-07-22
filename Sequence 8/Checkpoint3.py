import pandas as pd

# Create a Pandas Series
data = pd.Series([12, 15, 18, 20, 22, 24, 27, 30, 100])

print("Original Series:")
print(data)

# Calculate the mean and standard deviation
mean = data.mean()
std = data.std()

# Calculate Z-scores
z_scores = (data - mean) / std

# Filter out outliers (keep values within 3 standard deviations)
filtered_data = data[abs(z_scores) <= 3]

print("\nFiltered Series:")
print(filtered_data)
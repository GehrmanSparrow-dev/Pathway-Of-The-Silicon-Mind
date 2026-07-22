import numpy as np

# Input a 3x3 matrix
print("Enter the values for the 3x3 score matrix:")
matrix = []

for i in range(3):
    row = list(map(float, input(f"Enter 3 values for row {i + 1} (space-separated): ").split()))
    while len(row) != 3:
        print("Please enter exactly 3 values.")
        row = list(map(float, input(f"Enter 3 values for row {i + 1}: ").split()))
    matrix.append(row)

scores = np.array(matrix)

# Input the weight vector
weights = list(map(float, input("\nEnter 3 weights (space-separated): ").split()))
while len(weights) != 3:
    print("Please enter exactly 3 weights.")
    weights = list(map(float, input("Enter 3 weights: ").split()))

weights = np.array(weights)

# Multiply the matrix by the vector
result = np.dot(scores, weights)

# Convert to a column vector and get its transpose
column_vector = result.reshape(-1, 1)
transpose = column_vector.T

# Display results
print("\nScore Matrix:")
print(scores)

print("\nWeight Vector:")
print(weights)

print("\nResulting Vector:")
print(column_vector)

print("\nTranspose of the Resulting Vector:")
print(transpose)
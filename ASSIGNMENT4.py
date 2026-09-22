import numpy as np

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix2 = np.array([
    [7, 8, 9],
    [3, 2, 1]
])

result = matrix1 + matrix2

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nSum of the matrices:")
print(result)
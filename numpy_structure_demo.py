
import numpy as np


array_1d = np.array([10, 20, 30, 40])

# 2D Array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

print("1D Array:", array_1d)
print("2D Array:\n", array_2d)



print("\n1D Shape:", array_1d.shape)
print("1D Dimensions:", array_1d.ndim)

print("2D Shape:", array_2d.shape)
print("2D Dimensions:", array_2d.ndim)


# -----------------------------
# INDEXING
# -----------------------------
# 1D indexing
print("\nFirst element (1D):", array_1d[0])
print("Third element (1D):", array_1d[2])

# 2D indexing (row, column)
print("\nElement at row 0, col 1:", array_2d[0][1])
print("Element at row 1, col 2:", array_2d[1][2])
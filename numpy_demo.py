# -----------------------------
# IMPORT NUMPY
# -----------------------------
import numpy as np


# -----------------------------
# PYTHON LISTS
# -----------------------------
list_1d = [1, 2, 3, 4]
list_2d = [[1, 2, 3], [4, 5, 6]]


# -----------------------------
# CREATE NUMPY ARRAYS
# -----------------------------
array_1d = np.array(list_1d)
array_2d = np.array(list_2d)

print("1D Array:", array_1d)
print("2D Array:\n", array_2d)


# -----------------------------
# ARRAY INSPECTION
# -----------------------------
print("\nShape of 1D array:", array_1d.shape)
print("Shape of 2D array:", array_2d.shape)
print("Data type:", array_1d.dtype)


# -----------------------------
# SIMPLE ARRAY OPERATION
# -----------------------------
result = array_1d + 10   # element-wise addition

print("\nAfter adding 10:", result)
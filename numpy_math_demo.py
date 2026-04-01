# -----------------------------
# IMPORT NUMPY
# -----------------------------
import numpy as np


# -----------------------------
# CREATE ARRAYS
# -----------------------------
array1 = np.array([10, 20, 30])
array2 = np.array([1, 2, 3])

print("Array 1:", array1)
print("Array 2:", array2)


# -----------------------------
# ELEMENT-WISE OPERATIONS
# -----------------------------
print("\nAddition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)


# -----------------------------
# SCALAR OPERATIONS
# -----------------------------
print("\nAdd scalar (5):", array1 + 5)
print("Multiply scalar (2):", array1 * 2)


# -----------------------------
# SHAPE CHECK
# -----------------------------
print("\nShape of array1:", array1.shape)
print("Shape of array2:", array2.shape)
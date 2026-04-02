# -----------------------------
# IMPORT NUMPY
# -----------------------------
import numpy as np


# -----------------------------
# CREATE ARRAY
# -----------------------------
data = np.array([1, 2, 3, 4, 5])

print("Original Array:", data)


# -----------------------------
# LOOP-BASED APPROACH
# -----------------------------
loop_result = []

for num in data:
    loop_result.append(num * 2)

loop_result = np.array(loop_result)

print("\nLoop Result:", loop_result)


# -----------------------------
# VECTORIZED APPROACH
# -----------------------------
vector_result = data * 2

print("Vectorized Result:", vector_result)


# -----------------------------
# VERIFY RESULTS
# -----------------------------
print("\nAre both results equal?", np.array_equal(loop_result, vector_result))
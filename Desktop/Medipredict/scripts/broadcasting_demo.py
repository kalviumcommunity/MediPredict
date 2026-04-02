import numpy as np

print("===== SCALAR BROADCASTING =====")
arr = np.array([1, 2, 3])

print("Array:", arr)
print("Shape:", arr.shape)

result = arr + 5

print("Result (arr + 5):", result)
print("Shape after operation:", result.shape)


print("\n===== 1D to 2D BROADCASTING =====")
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6]])

arr1D = np.array([10, 20, 30])

print("2D Array:\n", arr2D)
print("Shape:", arr2D.shape)

print("1D Array:", arr1D)
print("Shape:", arr1D.shape)

result2 = arr2D + arr1D

print("Result (2D + 1D):\n", result2)
print("Shape after operation:", result2.shape)


print("\n===== BROADCASTING FAILURE EXAMPLE =====")
a = np.array([1, 2])
b = np.array([1, 2, 3])

print("Shape of a:", a.shape)
print("Shape of b:", b.shape)

try:
    print(a + b)
except Exception as e:
    print("Error:", e)
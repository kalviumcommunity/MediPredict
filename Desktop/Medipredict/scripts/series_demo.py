import pandas as pd
import numpy as np

print("=== Creating Series from List ===")
data_list = [10, 20, 30, 40]
series1 = pd.Series(data_list)

print(series1)
print("Index:", series1.index)
print("Values:", series1.values)


print("\n=== Creating Series from NumPy Array ===")
data_array = np.array([5, 15, 25, 35])
series2 = pd.Series(data_array)

print(series2)
print("Index:", series2.index)
print("Values:", series2.values)

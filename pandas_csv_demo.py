# -----------------------------
# IMPORT PANDAS
# -----------------------------
import pandas as pd


# -----------------------------
# LOAD CSV FILE
# -----------------------------
df = pd.read_csv("data/raw/patient_data.csv")

print("Data Loaded Successfully!\n")


# -----------------------------
# PREVIEW DATA
# -----------------------------
print("First 5 rows:")
print(df.head())


# -----------------------------
# INSPECT STRUCTURE
# -----------------------------
print("\nColumn Names:")
print(df.columns)

print("\nShape (rows, columns):")
print(df.shape)


# -----------------------------
# BASIC VERIFICATION
# -----------------------------
print("\nData Info:")
print(df.info())
# -----------------------------
# IMPORT PANDAS
# -----------------------------
import pandas as pd


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/raw/patient_data.csv")

print("Data Loaded Successfully!\n")


# -----------------------------
# PREVIEW DATA
# -----------------------------
print("First 5 Rows:")
print(df.head())


# -----------------------------
# DATA STRUCTURE INFO
# -----------------------------
print("\nData Info:")
df.info()


# -----------------------------
# NUMERICAL SUMMARY
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())
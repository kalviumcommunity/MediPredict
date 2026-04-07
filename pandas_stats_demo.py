# -----------------------------
# IMPORT PANDAS
# -----------------------------
import pandas as pd


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/raw/patient_data.csv")

print("Data Loaded!\n")


# -----------------------------
# SELECT NUMERIC COLUMNS
# -----------------------------
patients = df["patients"]
icu = df["icu"]


# -----------------------------
# COMPUTE STATISTICS
# -----------------------------
print("---- PATIENTS COLUMN ----")
print("Count:", patients.count())
print("Mean:", patients.mean())
print("Median:", patients.median())
print("Min:", patients.min())
print("Max:", patients.max())
print("Std Dev:", patients.std())


print("\n---- ICU COLUMN ----")
print("Count:", icu.count())
print("Mean:", icu.mean())
print("Median:", icu.median())
print("Min:", icu.min())
print("Max:", icu.max())
print("Std Dev:", icu.std())


# -----------------------------
# COMPARISON
# -----------------------------
print("\n---- COMPARISON ----")
print("Average patients:", patients.mean())
print("Average ICU beds:", icu.mean())
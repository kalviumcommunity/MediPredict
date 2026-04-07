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
# SELECT MULTIPLE COLUMNS
# -----------------------------
data = df[["patients", "icu"]]

print("Selected Columns:\n")
print(data.head())


# -----------------------------
# SUMMARY STATISTICS
# -----------------------------
print("\n---- SUMMARY STATISTICS ----")
print(data.describe())


# -----------------------------
# MANUAL COMPARISON
# -----------------------------
print("\n---- COMPARISON ----")

print("Patients Mean:", data["patients"].mean())
print("ICU Mean:", data["icu"].mean())

print("\nPatients Median:", data["patients"].median())
print("ICU Median:", data["icu"].median())

print("\nPatients Std Dev:", data["patients"].std())
print("ICU Std Dev:", data["icu"].std())

print("\nPatients Range:", data["patients"].max() - data["patients"].min())
print("ICU Range:", data["icu"].max() - data["icu"].min())
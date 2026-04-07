# -----------------------------
# IMPORT PANDAS
# -----------------------------
import pandas as pd


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/raw/messy_patient_data.csv")

print("---- BEFORE CLEANING ----")
print("Columns:", df.columns)
print(df.head())


# -----------------------------
# STANDARDIZE COLUMN NAMES
# -----------------------------
df.columns = (
    df.columns
    .str.strip()            # remove spaces
    .str.lower()            # lowercase
    .str.replace(" ", "_")  # replace spaces with _
    .str.replace("!", "")   # remove special characters
)

# -----------------------------
# STANDARDIZE DATA FORMAT
# -----------------------------
# Clean numeric columns (remove spaces and convert to int)
df["total_patients"] = df["total_patients"].astype(str).str.strip().astype(int)
df["icu_beds"] = df["icu_beds"].astype(str).str.strip().astype(int)

# Standardize date format
df["date_recorded"] = pd.to_datetime(df["date_recorded"], format="%d-%m-%Y")


# -----------------------------
# AFTER CLEANING
# -----------------------------
print("\n---- AFTER CLEANING ----")
print("Columns:", df.columns)
print(df.head())
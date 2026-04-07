import pandas as pd

# ================================
# 1. Creating DataFrame from Dictionary
# ================================
print("=== Creating DataFrame from Dictionary ===")

data = {
    "Name": ["Yashika", "Rahul", "Anu"],
    "Age": [19, 20, 21],
    "City": ["Chennai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

print(df)

print("\nColumns:", df.columns)
print("Shape:", df.shape)
print("Data Types:\n", df.dtypes)


# ================================
# 2. Loading DataFrame from CSV
# ================================
print("\n=== Loading DataFrame from CSV ===")

try:
    # Try this path first
    df_csv = pd.read_csv("data/raw/sample_data.csv")
except FileNotFoundError:
    # If error, try alternative path
    df_csv = pd.read_csv("../data/raw/sample_data.csv")

print(df_csv.head())

print("\nColumns:", df_csv.columns)
print("Shape:", df_csv.shape)
print("Data Types:\n", df_csv.dtypes)


# ================================
# 3. Why DataFrames are Useful
# ================================
print("\n=== Why DataFrames are Useful ===")
print("DataFrames organize data in rows and columns, similar to Excel.")
print("They make it easy to analyze, filter, and process data efficiently.")
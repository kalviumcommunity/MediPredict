import pandas as pd

# Read raw data
df = pd.read_csv("../data/raw/sample_data.csv")

# Clean data
df = df.dropna()

# Save processed data
df.to_csv("../data/processed/cleaned_data.csv", index=False)

print("Processed data saved!")
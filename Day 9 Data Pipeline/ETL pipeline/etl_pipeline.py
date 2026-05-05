import pandas as pd
from pathlib import Path

# Resolve paths from the script location
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

# -----------------------------
# EXTRACT
# -----------------------------

input_path = project_root / "raw data" / "product.csv"

df = pd.read_csv(input_path)

print("Raw Data:")
print(df)

# -----------------------------
# TRANSFORM
# -----------------------------

# Normalize prices between 0 and 1

min_price = df["price"].min()
max_price = df["price"].max()

df["normalized_price"] = (
    (df["price"] - min_price)
    / (max_price - min_price)
)

# Convert category names to uppercase

df["category"] = df["category"].str.upper()

print("\nTransformed Data:")
print(df)

# -----------------------------
# LOAD
# -----------------------------

output_path = project_root / "processed data" / "clean_products.csv"

df.to_csv(output_path, index=False)

print("\nCleaned data saved successfully.")
print(f"Output File: {output_path}")
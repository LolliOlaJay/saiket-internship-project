import pandas as pd

# Load the dataset (updated file name)
df = pd.read_csv("telecom_churn.csv.csv")

# Step 2: Display first 10 rows
print(" First 10 rows:")
print(df.head(10))

# Step 3: Column data types
print("\n Data Types:")
print(df.dtypes)

# Step 4: Check for missing values
print("\n Missing Values:")
print(df.isnull().sum())

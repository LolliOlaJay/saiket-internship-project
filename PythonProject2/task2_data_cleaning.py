import pandas as pd

# Load the dataset
df = pd.read_csv("telecom_churn.csv.csv")

# Step 1: Clean 'TotalCharges'
# First, check which rows can't be converted to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Print number of missing values after conversion
print("Missing 'TotalCharges' after conversion:", df['TotalCharges'].isnull().sum())

# Drop rows where 'TotalCharges' is still missing
df = df.dropna(subset=['TotalCharges'])

# Step 2: Remove duplicate rows
initial_shape = df.shape
df = df.drop_duplicates()
final_shape = df.shape

print(f"\n Duplicates removed: {initial_shape[0] - final_shape[0]} rows")

# Step 3: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\n Column names after standardizing:")
print(df.columns.tolist())

# Optional: Save the cleaned dataset for later tasks
df.to_csv("cleaned_telecom_churn.csv", index=False)
print("\n Dataset cleaned and saved as 'cleaned_telecom_churn.csv'")

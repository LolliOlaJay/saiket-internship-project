import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_telecom_churn.csv")

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Summary statistics
print("Summary Statistics:\n")
print(df.describe())

# Median
print("\n Median Monthly Charges:", df["monthlycharges"].median())
print("Mode Tenure:", df["tenure"].mode()[0])

# 2️⃣ Histograms
plt.figure(figsize=(8, 5))
sns.histplot(df["monthlycharges"], kde=True, color="skyblue")
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 3️⃣ Box plots
plt.figure(figsize=(8, 5))
sns.boxplot(x="churn", y="monthlycharges", data=df)
plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

# 4️⃣ Churn vs Non-Churn Proportions
churn_counts = df["churn"].value_counts()
print("\n Churn Value Counts:")
print(churn_counts)

plt.figure(figsize=(6, 6))
plt.pie(churn_counts, labels=churn_counts.index, autopct="%1.1f%%", startangle=140, colors=["#66b3ff", "#ff9999"])
plt.title("Churn vs Non-Churn Distribution")
plt.tight_layout()
plt.show()

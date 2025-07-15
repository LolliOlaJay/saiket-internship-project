import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_telecom_churn.csv")

# Convert 'churn' to numeric for calculations
df["churn_numeric"] = df["churn"].apply(lambda x: 1 if x.lower() == "yes" else 0)

# 1️⃣ Churn rate by tenure group
df["tenure_group"] = df["tenure"].apply(lambda x: "0–12" if x <= 12 else "13–36" if x <= 36 else "37+")

grouped = df.groupby("tenure_group").agg(
    avg_monthly_charge=("monthlycharges", "mean"),
    churn_rate=("churn_numeric", "mean"),
    customer_count=("churn_numeric", "count")
).reset_index()

print("📊 Churn Rate by Tenure Group:")
print(grouped)

# Plot churn rate by tenure group
plt.figure(figsize=(8, 5))
sns.barplot(x="tenure_group", y="churn_rate", data=grouped, palette="coolwarm")
plt.title("Churn Rate by Tenure Group")
plt.ylabel("Churn Rate")
plt.xlabel("Tenure Group")
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

# 2️⃣ Churn by demographics
def churn_barplot(column, title):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=column, y="churn_numeric", data=df, estimator=lambda x: sum(x)/len(x), palette="Set2")
    plt.title(f"Churn Rate by {title}")
    plt.ylabel("Churn Rate")
    plt.xlabel(title)
    plt.tight_layout()
    plt.show()

churn_barplot("gender", "Gender")
churn_barplot("seniorcitizen", "Senior Citizen Status")
churn_barplot("paymentmethod", "Payment Method")
churn_barplot("contract", "Contract Type")

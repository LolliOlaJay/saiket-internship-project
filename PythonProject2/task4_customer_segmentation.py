import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load cleaned dataset
df = pd.read_csv("cleaned_telecom_churn.csv")

# Step 1: Categorize tenure groups
def categorize_tenure(tenure):
    if tenure <= 12:
        return "0–12 months"
    elif tenure <= 36:
        return "13–36 months"
    else:
        return "37+ months"

df["tenure_group"] = df["tenure"].apply(categorize_tenure)

# Step 2: Pie/Donut chart – Customer distribution by tenure group
group_counts = df["tenure_group"].value_counts().reset_index()
group_counts.columns = ["Tenure Group", "Count"]

# Donut chart using Plotly
fig = px.pie(group_counts, values="Count", names="Tenure Group",
             hole=0.4, title="Customer Distribution by Tenure Group")
fig.show()

# Step 3: Clustered bar chart – Avg monthly charges by tenure group
avg_charges = df.groupby("tenure_group")["monthlycharges"].mean().reset_index()

# Bar chart using Matplotlib
plt.figure(figsize=(8, 6))
bars = plt.bar(avg_charges["tenure_group"], avg_charges["monthlycharges"], color=["#4CAF50", "#2196F3", "#FFC107"])
plt.title("Average Monthly Charges by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Average Monthly Charges")

# Step 4: Annotate each bar with value
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5), textcoords="offset points", ha="center", fontsize=10)

plt.tight_layout()
plt.show()

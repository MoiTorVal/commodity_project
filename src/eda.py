import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 

os.makedirs("outputs/eda", exist_ok=True)

df = pd.read_csv("data/processed/final_data.csv", parse_dates=["Date"])
df = df.set_index("Date")

# gold price over time
plt.figure(figsize=(12,4))
plt.plot(df["GLD"], color="gold")
plt.title("Gold Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("outputs/eda/gold_price_over_time.png")
plt.close()

# correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/eda/correlation_heatmap.png")
plt.close()

# basic stats 
print("Basic Statistics:\n")
print(df.describe())
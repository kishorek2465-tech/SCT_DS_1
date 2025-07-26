import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("india_gdp_by_state.csv")
df_sorted = df.sort_values(by="GSDP", ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(data=df_sorted.head(10), x="GSDP", y="State", palette="viridis")
plt.title("Top 10 Indian States by GDP (FY 2024-25)")
plt.xlabel("GSDP (₹ Lakh Crore)")
plt.ylabel("State")
plt.tight_layout()

plt.savefig("plots/gdp_bar_chart.png")
plt.show()

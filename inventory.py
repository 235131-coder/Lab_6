import pandas as pd
import matplotlib.pyplot as plt

# Dataset creation
data = {
    "Product": ["Cola", "Chips", "Milk", "Juice", "Biscuits", "Yogurt", "Soda", "Nuts", "Cheese", "Tea"],
    "Category": ["beverages ", "SNACKS", " Dairy", "beverages", "Snacks", "DAIRY", "beverages", "SNACKS", "Dairy", "beverages"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 150", "Rs. 200", "Rs. 80", "Rs. 300", "Rs. 600", "Rs. 1,800"],
    "Stock": [40, 120, 60, 80, 100, 50, 90, 70, 30, 25]
}

df = pd.DataFrame(data)

# (a) Clean Category text
df["Category"] = df["Category"].str.strip().str.title()

# (b) Clean and convert Price to numeric
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "").astype(float)

# (c) Label Encoding for Category
df["Category_Code"] = df["Category"].astype("category").cat.codes
print("Cleaned Inventory Data:")
print(df)

# (d) Subplots (1x2): Bar plot & Pie chart
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Avg Price per Category
avg_price = df.groupby("Category")["Price"].mean()
axes[0].bar(avg_price.index, avg_price.values, color=["#4C78A8", "#F58518", "#54A24B"])
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

# Share of Total Stock per Category
total_stock = df.groupby("Category")["Stock"].sum()
axes[1].pie(total_stock.values, labels=total_stock.index, autopct="%1.1f%%", colors=["#4C78A8", "#F58518", "#54A24B"])
axes[1].set_title("Stock Share by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()
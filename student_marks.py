
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Raw Data
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# Name clean karna
df["Name"] = df["Name"].str.strip().str.title()

# Marks ko number me convert karna aur "absent" ki jagah mean dalna
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean().round(1))

print("Cleaned Data:")
print(df)

# Graph banana aur save karna
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()


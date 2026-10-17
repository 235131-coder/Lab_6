import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset creation (7 days weather)
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temp_C": [25.0, 28.5, 22.0, 30.0, 27.5, 31.0, 26.0],
    "Humidity": [60, 55, 75, 50, 65, 45, 70],
    "Rainfall_mm": [0.0, 2.5, 12.0, 0.0, 1.0, 0.0, 5.5]
}

df = pd.DataFrame(data)

# Summary Statistics using Numpy & Pandas
print("--- Summary Statistics ---")
print(f"Mean Temp: {np.mean(df['Temp_C']):.2f} °C")
print(f"Max Humidity: {np.max(df['Humidity'])} %")
print(f"Total Rainfall: {np.sum(df['Rainfall_mm']):.2f} mm")

# 2x2 Grid Subplots Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Line Plot - Temperature
axes[0, 0].plot(df["Day"], df["Temp_C"], marker="o", color="tab:red", linewidth=2)
axes[0, 0].set_title("Daily Temperature (°C)")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].grid(True)

# 2. Bar Plot - Rainfall
axes[0, 1].bar(df["Day"], df["Rainfall_mm"], color="tab:blue")
axes[0, 1].set_title("Daily Rainfall (mm)")
axes[0, 1].set_ylabel("Rainfall (mm)")

# 3. Scatter Plot - Temp vs Humidity
axes[1, 0].scatter(df["Temp_C"], df["Humidity"], color="tab:green", s=100)
axes[1, 0].set_title("Temperature vs Humidity")
axes[1, 0].set_xlabel("Temperature (°C)")
axes[1, 0].set_ylabel("Humidity (%)")
axes[1, 0].grid(True)

# 4. Box Plot - Humidity Distribution
axes[1, 1].boxplot(df["Humidity"], patch_artist=True, boxprops=dict(facecolor="tab:purple"))
axes[1, 1].set_title("Humidity Distribution")
axes[1, 1].set_ylabel("Humidity (%)")

plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
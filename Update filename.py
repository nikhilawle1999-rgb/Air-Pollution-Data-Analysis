import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("weather.csv")

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Display first few rows
print("First few rows:")
print(data.head())

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Key metrics
avg_temp = data['Temperature'].mean()
max_temp = data['Temperature'].max()
rainy_days = data[data['Rainfall'] > 0].shape[0]

print(f"\nAverage Temperature: {avg_temp:.1f}°C")
print(f"Maximum Temperature: {max_temp}°C")
print(f"Total Rainy Days: {rainy_days}")

# Plot temperature trend
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Temperature', data=data, marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Plot humidity vs rainfall
fig, ax1 = plt.subplots(figsize=(10,5))
ax1.set_xlabel("Date")
ax1.set_ylabel("Humidity (%)", color='tab:blue')
ax1.plot(data['Date'], data['Humidity'], color='tab:blue', marker='o', label='Humidity')
ax2 = ax1.twinx()
ax2.set_ylabel("Rainfall (mm)", color='tab:green')
ax2.bar(data['Date'], data['Rainfall'], color='tab:green', alpha=0.4, label='Rainfall')
plt.title("Humidity and Rainfall Over Time")
plt.show()

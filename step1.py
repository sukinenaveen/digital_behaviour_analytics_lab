import matplotlib.pyplot as plt
import pandas as pd

x = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
values = [95, 120, 80, 140, 60, 170, 110]

print("Largest value:", max(values))

plt.figure(figsize=(10, 5))
plt.bar(x, values)
plt.title("My Screen Time by Day")
plt.xlabel("Day")
plt.ylabel("Value")
plt.show()

df = pd.read_csv("digital_behaviour.csv")

apps = [
    "Instagram_Minutes",
    "YouTube_Minutes",
    "WhatsApp_Minutes"
]

total_time = df[apps].sum()

plt.figure(figsize=(10, 5))
plt.bar(apps, total_time)
plt.title("Total Time by App")
plt.xlabel("App")
plt.ylabel("Minutes")
plt.show()
import matplotlib.pyplot as plt
import pandas as pd

x = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
values = [95, 120, 80, 140, 60, 170, 110]

print("Largest value:", max(values))

plt.figure(figsize=(5, 5))
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

plt.figure(figsize=(7, 7))
plt.bar(apps, total_time)
plt.title("Total Time by App")
plt.xlabel("App")
plt.ylabel("Minutes")
plt.show()

df["Total_Screen_Time"] = df[apps].sum(axis=1)

plt.figure(figsize=(8, 5))
plt.plot(df["Total_Screen_Time"], label="Screen Time", color="blue")
plt.plot(df["Study_Minutes"], label="Study Minutes", color="orange")
plt.title("Screen Time vs Study Time")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.legend()
plt.show()

plt.pie(total_time, labels=apps, autopct="%1.1f%%")
plt.title("Total Time by App")
plt.show()
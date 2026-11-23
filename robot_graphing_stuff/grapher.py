from pathlib import Path
import matplotlib.pyplot as plt
import random

data = Path("robot_graphing_stuff/robot_data/turret log.txt").read_text()
dataList = data.splitlines()
lines = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i, line in enumerate(lines):
    tempData = dataList[line].split(",")
    temp = []
    for rpm in tempData:
        temp.append(float(rpm))
    lines[i] = temp.copy()

times = dataList[1].split(",")
temp = []
for time in times:
    temp.append(float(time))
times = temp.copy()
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
for line in lines:
    ax.plot(times, line, color="red")

title = "RPM over time"
ax.set_title(title, fontsize=20)
ax.set_ylabel("RPM", fontsize=16)
ax.set_xlabel("time (seconds)", fontsize=16)

plt.show()
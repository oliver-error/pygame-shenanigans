from pathlib import Path
import matplotlib.pyplot as plt
import random

data = Path("robot_graphing_stuff/robot_data/log.txt").read_text()
dataList = data.splitlines()
RPMs = dataList[0].split(",")
times = dataList[1].split(",")

temp = []
for rpm in RPMs:
    temp.append(float(rpm))
RPMs = temp.copy()
temp = []
for time in times:
    temp.append(float(time))
times = temp.copy()
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(times, RPMs, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

title = "RPM over time"
ax.set_title(title, fontsize=20)
ax.set_ylabel("RPM", fontsize=16)
ax.set_xlabel("time (ms)", fontsize=16)

plt.show()
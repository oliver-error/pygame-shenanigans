import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")
input_values = []
squares = []
for i in range(1, 1001):
    squares.append(i ** 2)
    input_values.append(i)

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()


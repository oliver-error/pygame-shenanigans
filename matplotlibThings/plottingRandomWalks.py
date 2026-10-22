import matplotlib.pyplot as plt
import random
from randomWalk import RandomWalk

colorMaps = [plt.cm.YlOrRd, plt.cm.Blues, plt.cm.managua, plt.cm.autumn, plt.cm.YlGnBu]
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=random.choice(colorMaps), s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


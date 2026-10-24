import matplotlib.pyplot as plt
import random
from randomWalk import RandomWalk

colorMaps = [plt.cm.YlOrRd, plt.cm.Blues, plt.cm.managua, plt.cm.autumn, plt.cm.YlGnBu]
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')
    
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


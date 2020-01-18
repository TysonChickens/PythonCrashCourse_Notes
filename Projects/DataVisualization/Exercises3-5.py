# 15-3 Molecular Motion replace plt.scatter() with plt.plot() and simulate path of pollen grain.

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep generating new walks as long as the program is active.
while True:
    # Make a random walk of a pollen grain on the surface drop of water.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    
    # Color / Style the points in the walk.
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, zorder=2)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running != 'y':
        break

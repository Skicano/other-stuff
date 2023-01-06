import matplotlib.pyplot as plt
from random_walk_2 import RandomWalk


# Keep making new walks, as long as the program is active.
while True:

    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

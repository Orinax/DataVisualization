import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
                edgecolor='none', s=15)

# Something about this block doesn't work at all.
# No points are visible if this block is included.
#    # Remove the axes.
#    plt.axes().get_xaxis().set_visible(False)
#    plt.axes().get_yaxis().set_visible(False)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='blue', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
                s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

import numpy as np
import matplotlib.pyplot as plt


def scatter_plot(ax):
    x, y = np.random.normal(size=(2, 200))
    ax.plot(x, y, 'o')


def color_cycle_plot(ax):
    # sinusoidal lines with colors from default color cycle
    L = 2*np.pi
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.color_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), '-')
    ax.margins(0)
    ax.set_title("# lines = len(color_cycle)")


def bar_plot(ax):
    categories = ['a', 'b', 'c', 'd', 'e']
    x = np.arange(len(categories))
    n_modes = 3
    width = 0.25
    for i in range(n_modes):
        y = np.random.randint(1, 25, size=len(categories))
        x_offset = i * width
        ax.bar(x+x_offset, y, width, color=plt.rcParams['axes.color_cycle'][i])
    ax.set_xticks(x+width)
    ax.set_xticklabels(categories)


def circle_plot(ax):
    # circles with colors from default color cycle
    for i, color in enumerate(plt.rcParams['axes.color_cycle']):
        xy = np.random.normal(size=2)
        ax.add_patch(plt.Circle(xy, radius=0.3, color=color))
    ax.axis('equal')
    ax.margins(0)


fig, axes = plt.subplots(ncols=2, nrows=2)
axes = axes.flatten()  # Turn 2 x 2 array to a flat array for easier indexing.

scatter_plot(axes[0])
color_cycle_plot(axes[1])
bar_plot(axes[2])
circle_plot(axes[3])

plt.show()

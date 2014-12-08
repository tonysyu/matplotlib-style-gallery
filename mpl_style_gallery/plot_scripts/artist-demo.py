import numpy as np

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def legend_demo(ax):
    x = np.linspace(0, 1, 30)
    ax.plot(x, np.sin(2*np.pi*x), '-s', label='line')
    c = plt.Circle((0.25, 0), radius=0.1, label='patch')
    ax.add_patch(c)
    ax.grid()
    ax.legend()
    ax.set_title('legend')


def color_cycle_plot(ax):
    x = np.linspace(0, 10)
    ncolors = len(plt.rcParams['axes.color_cycle'])
    shift = np.linspace(0, 2*np.pi, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), '-')
    ax.set_title("# lines = len(color_cycle)")


def text_demo(ax):
    ax.text(0.5, 0.5, 'hello world', ha='center', va='center')
    ax.set_xlabel('x-label')
    ax.set_ylabel('y-label')
    ax.set_title('title')


def image_demo(fig, ax):
    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    xx, yy = np.meshgrid(x, y)
    z1 = mlab.bivariate_normal(xx, yy, 1.0, 1.0, 0.0, 0.0)
    z2 = mlab.bivariate_normal(xx, yy, 1.5, 0.5, 1, 1)
    image = z2-z1  # Difference of Gaussians
    img_plot = ax.imshow(image)
    ax.set_title('image')

    fig.tight_layout()
    # `colorbar` should be called after `tight_layout`.
    fig.colorbar(img_plot, ax=ax)


fig, axes = plt.subplots(ncols=2, nrows=2)
axes = axes.flatten()  # Turn 2 x 2 array to a flat array for easier indexing.

legend_demo(axes[0])
color_cycle_plot(axes[1])
text_demo(axes[2])
image_demo(fig, axes[3])

plt.show()

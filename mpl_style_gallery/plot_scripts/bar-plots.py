import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


np.random.seed(0)  # Set seed so plots look the same.


def histogram_demo(ax):
    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(10000)

    num_bins = 50

    # The histogram of the data.
    _, bins, _ = ax.hist(x, num_bins, normed=1, label='data')

    # Add a 'best fit' line.
    y = mlab.normpdf(bins, mu, sigma)
    ax.plot(bins, y, '-s', label='best fit')

    ax.legend()
    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability')
    ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')


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


fig, axes = plt.subplots(nrows=2)

histogram_demo(axes[0])
bar_plot(axes[1])

fig.tight_layout()
plt.show()

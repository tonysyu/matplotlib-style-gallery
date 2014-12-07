import numpy as np

import matplotlib.pyplot as plt


fig, axes = plt.subplots(2, 2)
axes = axes.ravel()

x = np.linspace(0, 1)
axes[0].plot(x, np.sin(2*np.pi*x), label='line')
c = plt.Circle((0.25, 0), radius=0.1, label='patch')
axes[0].add_patch(c)
axes[0].grid()
axes[0].legend()

img = axes[1].imshow(np.random.random(size=(20, 20)))
axes[1].set_title('image')

ncolors = len(plt.rcParams['axes.color_cycle'])
phi = np.linspace(0, 2*np.pi, ncolors + 1)[:-1]
for p in phi:
    axes[2].plot(x, np.sin(2*np.pi*x + p))
axes[2].set_title('color cycle')

axes[3].text(0, 0, 'hello world')
axes[3].set_xlabel('x-label')
axes[3].set_ylabel('y-label')
axes[3].set_title('title')

try:
    fig.tight_layout()
except AttributeError:
    pass
# `colorbar` should be called after `tight_layout`.
fig.colorbar(img, ax=axes[1])

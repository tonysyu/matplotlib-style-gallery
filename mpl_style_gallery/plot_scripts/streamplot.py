import numpy as np
import matplotlib.pyplot as plt

L = 3
Y, X = np.mgrid[-L:L:100j, -L:L:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)

plt.imshow(speed, extent=[-L, L, -L, L], alpha=0.5)
plt.colorbar(label='speed')

plt.streamplot(X, Y, U, V, linewidth=0.2*speed)

plt.title('Streamlines')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()

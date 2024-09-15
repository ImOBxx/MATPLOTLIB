import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2= np.array([6, 2, 7, 10])

plt.plot(x, y, x2, y2, lw = 20.5)

plt.show()
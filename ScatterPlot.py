import matplotlib.pyplot as plt
from pylab import randn

x = randn(200)

y = randn(200)

plt.scatter(x, y, s = 70, facecolors = 'none',  edgecolor = 'g')

plt.xlabel('x')

plt.ylabel('y')

plt.show()
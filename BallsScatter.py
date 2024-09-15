import math
import random
import matplotlib.pyplot as plt

nb = 25

x = [random.triangular() for i in range(nb)]
y = [random.gauss(0.5, 0.25) for i in range(nb)]
colors = [random.randint(1, 4) for i in range(nb)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(nb)]

plt.figure()

plt.scatter(x, y, s = areas, c = colors, alpha = 0.85)

plt.axis = ([0.0, 1.0, 0.0, 1.0])

plt.xlabel('x')

plt.ylabel('y')

plt.show()
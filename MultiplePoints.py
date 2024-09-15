import matplotlib.pyplot as plt
import numpy as np

xp = np.array([1, 2, 6, 8, 4])

yp = np.array([3, 8, 1, 10, 5])

plt.plot(xp, yp)

plt.xlabel("Average Label")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data", loc = 'left')

plt.grid(ls = ":", lw = 0.8, color = 'g')

plt.show()

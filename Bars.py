import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D"])

y = np.array([3, 8, 1, 10])

plt.barh(x, y, color = "red", width= 0.5)
plt.show()
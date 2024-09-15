import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([0, 6])

y = np.array([0, 250])

plt.plot(x, y, 'X:g', ms = 20, mfc = "red", mec = "blue")

plt.show()
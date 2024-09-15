import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
ml = ["Apples", "Bananas", "Cherries", "Dates"]
mex = [0, 0, 0.10, 0]
mc = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = ml, startangle = 280, explode = mex, shadow = True, colors = mc)
plt.legend(title = "Four Fruits: ")
plt.show() 
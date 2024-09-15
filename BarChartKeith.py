import matplotlib.pyplot as plt
import numpy as np

l = ['A', 'B', 'C']
v = [1, 4, 2]

bars = plt.bar(l, v)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

"""
bars[0].set_hatch('/')
bars[1].set_hatch('O')
bars[2].set_hatch('*')
"""
plt.figure(figsize = (6, 4))

plt.show()

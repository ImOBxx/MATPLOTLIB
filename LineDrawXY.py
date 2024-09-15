import matplotlib.pyplot as plt

x = range(1, 50)

y = [value * 3 for value in x]

plt.plot(x, y)

plt.xlabel('X-Axis')

plt.ylabel('Y-Axis')

plt.title('Draw A Line.')

plt.show()

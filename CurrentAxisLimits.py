import matplotlib.pyplot as plt

x = range(1, 50)

y = [value * 3 for value in x]

plt.plot(x, y)

plt.xlabel('X')

plt.ylabel('Y')

plt.title("Draw A line")

print(plt.axis())

plt.axis([0, 100, 0, 200])

plt.show()
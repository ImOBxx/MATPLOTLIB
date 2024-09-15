import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, pop, color = 'b')
fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, pop, color='r', edgecolor = 'blue')
        #color = ['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
        #color=(0.4, 0.6, 0.8, 1.0))

plt.xlabel("Languages")
plt.ylabel('Popularity')

plt.xticks(x_pos, x, rotation = 90)

y_pos = [0,1,4,7,9,10]

plt.bar(y_pos, pop)

plt.subplots_adjust(bottom=0.4, top=.8)

plt.minorticks_on()

plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%f' % float(height),
        ha='center', va='bottom')
autolabel(rects1)

plt.show()

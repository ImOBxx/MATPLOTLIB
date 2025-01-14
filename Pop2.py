import matplotlib.pyplot as plt

lan = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'

pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

explode = (0.1, 0, 0, 0, 0, .1)

plt.pie(pop, explode = explode, labels = lan, colors = colors, autopct = '%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')
print(fifa.head(5))

print(fifa['Preferred Foot'])

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
print(left)

right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
print(right)

labels = ['Left', 'Right']
colors = ['#abcdef', '#aabbcc']

plt.pie([left, right], labels = labels, colors = colors, autopct = '%.2f%%')

plt.title('Foot Preference Of FIFA Players')

plt.show()






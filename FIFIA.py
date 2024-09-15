import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv('fifa_data.csv')
print(fifa.head(5))

### Histogram

bins = [80, 90, 100]

#0, 10, 20, 30, 40, 50, 60, 70, 
plt.hist(fifa.Overall, bins = bins, color = 'r')

plt.xticks(bins)

plt.xlabel('Number Of Players')
plt.ylabel('Skill Level')
plt.title('Distribution Of Player Skills in FIFA 2018')

plt.show()
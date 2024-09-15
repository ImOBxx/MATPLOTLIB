import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


gas = pd.read_csv('gas_prices.csv')
print(gas)

plt.figure(figsize = (8, 5))

plt.title('Gas Prices Over Time (USD)', fontdict = {'fontweight': 'bold', 'fontsize' : 18})


plt.plot(gas['Year'], gas.USA, 'b.-')

plt.plot(gas['Year'], gas.Canada, 'r.-')

plt.plot(gas['Year'], gas['South Korea'], 'g.-')

plt.plot(gas['Year'], gas.Australia, 'y.-')


"""
ANOTHER WAY TO PLOT

countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']
for country in gas:
    if country in countries_to_look_at:
        plt.plot(gas.Year, gas[country], marker = '.', label = country)
"""


plt.xticks(gas.Year[::3].to_list() + [2011])

plt.xlabel('Year')

plt.ylabel('US Dollars')

plt.legend(bbox_to_anchor=(1, 1), loc='upper left')

plt.savefig('Gas_price_figure', dpi = 300)

plt.hist(gas.Overall)

plt.show()
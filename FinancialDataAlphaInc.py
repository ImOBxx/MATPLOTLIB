import pandas as pd
import matplotlib .pyplot as plt

df = pd.read_csv('GOOG.csv', sep = ',', parse_dates = True, index_col = 0)

df.plot()

plt.show()
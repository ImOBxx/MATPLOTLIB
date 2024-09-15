import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
fifa = pd.read_csv('fifa_data.csv')
print(fifa.head(5))

# Clean Weight column
fifa.Weight = fifa.Weight.str.replace('lbs', '').astype(float)

# Define weight categories
light = fifa[fifa.Weight < 125].shape[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].shape[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].shape[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].shape[0]
heavy = fifa[fifa.Weight >= 200].shape[0]

weights = [light, light_medium, medium, medium_heavy, heavy]

explode = (.4, .2, 0, 0, 4)
# Plot pie chart
plt.pie(weights, labels=['<125', '125-150', '150-175', '175-200', '200+'], autopct='%1.1f%%', explode = explode)
plt.title('Weight Distribution of FIFA Players')
plt.show()


#print(df_weight)


#plt.pie(df_weight)
#plt.show()


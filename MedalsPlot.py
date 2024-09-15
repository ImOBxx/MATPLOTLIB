import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('olympic-medals.csv')

# Extracting country and gold medal data
country_data = df['TEAM'][:5]  # Considering the top 5 countries
medal_data = df['Gold'][:5]

# Defining colors and explode configuration
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)

# Plotting the pie chart
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Adding title
plt.title("Gold Medal Achievements of Five Most Successful\nCountries in 2016 Summer Olympics")

# Display the plot
plt.show()


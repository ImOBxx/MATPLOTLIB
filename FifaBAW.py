import matplotlib.pyplot as plt
import pandas as pd

# Load data
fifa = pd.read_csv('fifa_data.csv')
print(fifa.head(5))

plt.figure(figure = (10, 10))

# Extract Overall ratings for each club
barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

# Labels for the boxplot
labels = ['FC Barcelona', 'Real Madrid', 'New England Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], labels = labels, patch_artist = True, medianprops= {'linewidth' : 2})

for box in boxes['boxes']:
    box.set(color = '#4286f4', linewidth = 2)

    box.set(facecolor = '#e0e0e0')

# Create boxplot
plt.boxplot([barcelona.dropna(), madrid.dropna(), revs.dropna()], labels=labels)

# Add title and labels
plt.title('Pro Football Comparison')
plt.ylabel('Fifa Overall Rating')

# Show plot
plt.show()
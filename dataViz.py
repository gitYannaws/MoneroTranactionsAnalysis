import seaborn
import pandas
import matplotlib.pyplot as plt

# res = seaborn.violinplot(x=csv['Age'])
# csv = pandas.read_csv('moneroDataCleaned.csv')
# res = seaborn.lineplot(y="num_txes", x="date", data=csv)
# res = seaborn.violinplot(x=csv['num_txes'])
# res = seaborn.histplot(data=csv, x="num_txes")
# plt.show()


import matplotlib.pyplot as plt
import datetime

# Data to plot
x = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
y = [1, 5, 9, 4, 12]

# Create the scatter plot
plt.scatter(x, y, s=100, c='red', marker='^')

# Add labels and a title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Scatter plot example')

# Show the plot
plt.show()



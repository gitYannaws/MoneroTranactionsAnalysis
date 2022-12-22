import seaborn as sns
import pandas
import matplotlib.pyplot as plt
# what time is less/empty blocks are happening?

df = pandas.read_csv('moneroDataCleaned.csv')

# res = seaborn.lineplot(y="num_txes", x="date", data=df)
res = sns.histplot(data=df, x="datehour")
# ax = seaborn.violinplot(y=df['num_txes'], data=df)

plt.show()




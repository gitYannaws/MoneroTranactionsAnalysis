import pandas as pd

df = pd.read_csv('moneroDataV2.csv')


df['date'] = pd.to_datetime(df['datetime'])
df = df.dropna()
df = df.drop_duplicates(subset=['block'], keep=False)


df.to_csv('moneroDataCleaned.csv')

print(df)

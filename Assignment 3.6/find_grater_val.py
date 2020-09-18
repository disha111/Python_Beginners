import pandas as pd
df = pd.read_csv('forestfires.csv')
Wind = df['wind']>2
print("wind values greater than 2.0 : \n",df.loc[Wind,['wind']])
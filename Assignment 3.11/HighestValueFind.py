import pandas as pd
df = pd.read_csv('ETH.csv')
filt1 = df['Date'].str.contains('2019')
filt2 = df['Date'].str.contains('2020')
print("highest value of column 'Open' for the year 2019 : ",df.loc[filt1,'Open'].max())
print("highest value of column 'Open' for the year 2020  : ",df.loc[filt2,'Open'].max())
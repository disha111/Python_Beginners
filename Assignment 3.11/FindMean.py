import pandas as pd
df = pd.read_csv('ETH.csv')
filt = df['Date'].str.contains('2018')
print("Calculate mean of column 'Close' for the year 2018 : ",df.loc[filt,'Close'].mean())
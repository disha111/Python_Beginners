import pandas as pd
df = pd.read_csv('ETH.csv')
# filt = df['Date'].str.contains('2018')
# print("Calculate mean of column 'Close' for the year 2018 : ",df.loc[filt,'Close'].mean())
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
# filt2 = (df['Date'] >= pd.to_datetime('2018-01-01')) & (df['Date'] < pd.to_datetime('2019-01-01'))
# print("Calculate mean of column 'Close' for the year 2018 : ",df.loc[filt2]['Close'].mean())
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d')
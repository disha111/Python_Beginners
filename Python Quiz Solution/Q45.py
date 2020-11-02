import pandas as pd
df = pd.read_csv('ETH.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
filt2 = (df['Date'] >= pd.to_datetime('2018-01-01')) & (df['Date'] < pd.to_datetime('2019-01-01'))
filter = df['Date']=='2018-01-01'
new = df.loc[filter,'Date']='2020-12-31'
print(new)
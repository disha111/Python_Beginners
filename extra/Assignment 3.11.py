import pandas as pd
import datetime
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH.csv',parse_dates=['Date'], date_parser=d_parser)

print(df.head(10))

filt = (df['Date'] >= pd.to_datetime('2018-01-01')) & (df['Date'] < pd.to_datetime('2019-01-01'))
print(df.loc[filt]['Close'].mean())

# df['Date1']=pd.to_datetime('2020-02-22')

# print(df.loc[0,'Date1'].day_name())


# filt1 = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
# print(df.loc[filt1]['High'].max())
# print(df.head(5))
# df.drop(columns=['Date1'],inplace=True)
# print(df.head(5))



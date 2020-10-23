import pandas as pd
df = pd.read_csv('ETH.csv')
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d %I-%p')
print("Calculate mean of column 'Close' for the year 2018 : ",df.groupby('Date').get_group('2018')['Close'].mean())
# filt = df['Date']=='2018'
# print(df.loc[filt,'Close'].mean())
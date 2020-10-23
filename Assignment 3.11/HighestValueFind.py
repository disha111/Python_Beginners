import pandas as pd
df = pd.read_csv('ETH.csv')
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d %I-%p')
print("highest value of column 'Open' for the year 2019 : ",df.groupby('Date').get_group('2019')['Open'].max())
print("highest value of column 'Open' for the year 2020  : ",df.groupby('Date').get_group('2020')['Open'].max())
import pandas as pd
df = pd.read_csv('ETH.csv')
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d %I-%p')
df['Day'] = df['Date'].dt.day_name()
filt = df['Date'] == '2020-02-21'
print("Display the day of the date 2020-02-21\n",df.loc[filt]['Day'])
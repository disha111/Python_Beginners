import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
filt = (df['Date']>=pd.to_datetime('2020-03-01')) & (df['Date']<=pd.to_datetime('2020-03-07'))
print(df.loc[filt,'Close'].mean())

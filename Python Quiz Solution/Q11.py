import pandas as pd
df = pd.read_csv('ETH.csv')
filt = (df['Date']>='2018'&(df['Date']<'2019'))
print(df.iloc[filt,['Close']].mean())
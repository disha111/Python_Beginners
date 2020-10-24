import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
df.set_index('Date', inplace=True)
print(df[{'Close':'Close'}].resample('W').mean())


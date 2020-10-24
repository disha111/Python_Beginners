import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
filt = df['Date'].str.contains('2020-01')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
df['Day'] = df['Date'].dt.day_name()
df.set_index('Date', inplace=True)
print(df.loc['2020-01'][{'High':'High','Day':'Day'}].resample('D').max())
# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# print("Calculate day wise max value of High column of January - 2020  ")
# for i in days:
#     grouped = df.groupby('Day').get_group(i)
#     print(i," : ",grouped.loc[filt,'High'].max())
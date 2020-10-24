import pandas as pd
import datetime
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH.csv',parse_dates=['Date'], date_parser=d_parser)

print(df['Date'].dt.day_name())
df['DayOfWeek'] = df['Date'].dt.day_name()
df.set_index('Date', inplace=True)

print("##################################################################################")

highs = df['High'].resample('D').max()
print(df['High'].resample('D').mean())  
print(df['High'].resample('W').mean())
print(highs.count())
print('##################################################################################')

# #
print("# Calculate day wise minimum value of High column,  maximum value of Open column, average value of Close column of dataframe using agg().")
print(df['Open'].resample('D').max())
print(df['Open'].resample('D').mean())
print(df['Close'].resample('D').max())
print(df['Close'].resample('D').mean())
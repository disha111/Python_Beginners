from numpy.core.fromnumeric import mean
import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
df['Day'] = df['Date'].dt.day_name()
df.set_index('Date', inplace=True)
print("\nminimum value of High column is : ")
print(df[{'High':'High','Day':'Day'}].resample('D').agg(min))
print("\nmaximum value of Open column is : ")
print(df[{'Open':'Open','Day':'Day'}].resample('D').agg(max))
print("\naverage value of Close column is : ")
print(df[{'Close':'Close','Day':'Day'}].resample('D').agg(mean))
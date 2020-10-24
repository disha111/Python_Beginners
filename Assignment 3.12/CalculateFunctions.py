from numpy.core.fromnumeric import mean
import pandas as pd
df = pd.read_csv("ETH.csv") #cd ..
filt = df['Date'].str.contains('2020-01')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
df['Day'] = df['Date'].dt.day_name()
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for i in days:
    grouped = df.groupby('Day').get_group(i)
    print("Minimum value of High column on ",i," is: ",grouped['High'].agg(min))
    print("Maximum value of Open column on ",i," is: ",grouped['Open'].agg(max))
    print("Average value of Close column on ",i," is: ",grouped['Close'].mean(),"\n")

df.set_index('Date', inplace=True)
print("\nminimum value of High column is : ")
print(df[{'High':'High','Day':'Day'}].resample('D').agg(min))
print("\nmaximum value of Open column is : ")
print(df[{'Open':'Open','Day':'Day'}].resample('D').agg(max))
print("\naverage value of Close column is : ")
print(df[{'Close':'Close','Day':'Day'}].resample('D').agg(mean))
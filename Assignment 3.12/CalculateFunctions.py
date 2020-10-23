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


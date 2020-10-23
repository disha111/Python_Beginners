import pandas as pd
df = pd.read_csv('ETH.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p') 
print("Convert type of column 'Date' into datetime = ",df['Date'].dtypes)
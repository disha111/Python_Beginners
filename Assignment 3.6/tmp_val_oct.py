import pandas as pd
df = pd.read_csv('forestfires.csv')
result = df[['temp']]
month = df['month']=='oct'
print("temp values of oct month : \n",df.loc[month,['temp']])
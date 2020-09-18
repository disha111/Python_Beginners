import pandas as pd
df = pd.read_csv('Thums up.csv',delimiter=';')
print("Maximum Quality : ",df.quality.max())
max = df['quality']==df.quality.max()
print(df[max])
import pandas as pd
df = pd.read_csv('Thums up.csv',delimiter=';')
df.reset_index(inplace = False) 
print(df)
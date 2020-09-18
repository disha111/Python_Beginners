import pandas as pd
df = pd.read_csv('Thums up.csv',delimiter=';')
print(df.set_index(['density']))
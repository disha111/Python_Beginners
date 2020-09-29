import pandas as pd
df = pd.read_csv('games.csv')
print(df[df['black_id'].str.startswith('sh')].head())
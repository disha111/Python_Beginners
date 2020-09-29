import pandas as pd
df = pd.read_csv('games.csv')
df = df.rename(columns={'moves':'game moves'})
print(df.columns)
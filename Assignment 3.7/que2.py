import pandas as pd
from pandas.core.algorithms import isin
df = pd.read_csv('games.csv')
print(df[df['white_id'].str.contains("daniel")] )
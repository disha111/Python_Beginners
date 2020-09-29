import pandas as pd
df = pd.read_csv('games.csv')
gp = df.groupby('victory_status')
print(gp.get_group('mate'))
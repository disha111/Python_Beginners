import pandas as pd
df = pd.read_csv("forestfires.csv")
grouped = df.groupby('month')['wind'].get_group('aug')
key=[]
[key.append(i) for i in df.groupby('month')['month'].get_group('aug')]
print("Display wind for 'aug' month :\n",pd.DataFrame({'Month':key,'wind':grouped}))
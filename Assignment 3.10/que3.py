import pandas as pd
df = pd.read_csv('forestfires.csv')
key,val = [],[]
[key.append(i) for i in df.groupby('month').groups]
[val.append(i) for i in df.groupby('month')['DC'].median()]
print("Calculate of column DC month wise:\n ",pd.DataFrame({'Month':key,'DC':val}))
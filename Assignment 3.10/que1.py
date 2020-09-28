import pandas as pd
df = pd.read_csv('forestfires.csv')
val,key = [],[]
[val.append(i) for i in df.groupby('month')['temp'].agg(max)]
[key.append(i) for i in df.groupby('month').groups]
print("Highest temperature of every month:\n ",pd.DataFrame({'Month':key,'Temp':val}))
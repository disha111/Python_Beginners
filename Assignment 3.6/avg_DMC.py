import pandas as pd
df = pd.read_csv('forestfires.csv')
print("average value of DMC : ",df.DMC.mean(axis=0))
# print("average value of DMC : ",df.DMC.mean(axis=0).round(2))
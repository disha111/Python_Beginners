import pandas as pd
df=pd.read_csv('forestfires.csv')
print("Average of DMC column :",df.DMC.mean(axis=0).round(2))
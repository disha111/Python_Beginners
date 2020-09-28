import pandas as pd
df = pd.read_csv('forestfires.csv')
key,median,mean,min,max = [],[],[],[],[]
[key.append(i) for i in df.groupby('month').groups]
[median.append(i) for i in df.groupby('month')['FFMC'].median()]
[mean.append(i) for i in df.groupby('month')['FFMC'].mean()]
[min.append(i) for i in df.groupby('month')['FFMC'].min()]
[max.append(i) for i in df.groupby('month')['FFMC'].max()]
print("Calculate median, mean, min, max of column FFMC month wise:\n ",pd.DataFrame({'Month':key,'FFMC(Median)':median,'FFMC(Mean)':mean,'FFMC(Max)':max,'FFMC(Min)':min}))
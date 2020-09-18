import pandas as pd
df = pd.read_csv('Thums up.csv',delimiter=';')
print("Minimum Dansity Level : ",df.density.min())
import pandas as pd
df = pd.Series([196,625,121])
print("Defalut DataFrame is :\n",df)
print("Data Filter using map methon in Pandas :\n",df.map({121:169}))
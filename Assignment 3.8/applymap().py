import pandas as pd
df = pd.DataFrame([[196,625],[9,49],[81,121]],columns=['D','J'])
print("Defalut DataFrame is :\n",df)
print("Division using apply methon in Pandas :\n",df.applymap(lambda x: x//2))
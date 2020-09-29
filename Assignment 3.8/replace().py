import pandas as pd
df = pd.DataFrame([[196,625],[121,49],[81,121]],columns=['D','J'])
print("Defalut DataFrame is :\n",df)
print("using replace methon in Pandas :\n",df.replace({'D':{121:144},'J':{121:169}}))
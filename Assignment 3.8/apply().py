import pandas as pd
import numpy as np
df = pd.DataFrame([[196,625],[9,49],[81,121]],columns=['D','J'])
print("Defalut DataFrame is :\n",df)
print("SquareRoot using apply methon in Pandas :\n",df.apply(np.sqrt))
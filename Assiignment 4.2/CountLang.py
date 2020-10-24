import pandas as pd
from collections import Counter

from pandas.core.algorithms import value_counts
df = pd.read_csv('data.csv')
lang = Counter()
for i in df['LanguagesWorkedWith']:
    # lang.update(i.split(';'))
    lang.update(value_counts(i.split(';')))

lan,count =[],[]
for i in lang.most_common(15):
    lan.append(i[0])
    count.append(i[1])
Data = pd.DataFrame({'Language':lan,'Count':count})
print(Data)
from collections import Counter 
import pandas as pd
df = pd.read_csv('data.csv')
lang = Counter()
[lang.update(i.split(';')) for i in df['LanguagesWorkedWith']]
lan,count =[],[]
[[lan.append(langC[0]),count.append(langC[1])]for langC in lang.most_common(len(lang))]
print(pd.DataFrame({'Language':lan,'Count':count}))
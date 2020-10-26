import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

df = pd.read_csv('data.csv')
lang = Counter()
[lang.update(i.split(';')) for i in df['LanguagesWorkedWith']]
lan,count =[],[]
[[lan.append(langC[0]),count.append(langC[1])]for langC in lang.most_common(len(lang))]
lan.reverse()
count.reverse()
plt.barh(lan,count)
plt.tight_layout()
plt.title("Popular languages")
plt.ylabel("Programming Languages")
plt.xlabel("Languages Count")
plt.show()
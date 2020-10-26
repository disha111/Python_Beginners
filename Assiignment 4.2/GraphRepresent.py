import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

df = pd.read_csv('data.csv')
lang = Counter()
for i in df['LanguagesWorkedWith']:
    lang.update(i.split(';'))
lan,count =[],[]
for i in lang.most_common(15):
    lan.append(i[0])
    count.append(i[1])
plt.plot(count,lan)
plt.tight_layout()
plt.title("Popular languages")
plt.ylabel("Programming Languages")
plt.xlabel("Languages Count")
plt.show()
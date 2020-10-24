import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
# print(language_counter)

for response in lang_responses:
    language_counter.update(response.split(';'))
    # print(language_counter)
print(language_counter)
languages = []
popularity = []
for letter, count in language_counter.most_common(25):
    print('%s: %7d' % (letter, count))
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
# plt.barh(languages, popularity)
plt.title("Most Popular Languages")
plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")
plt.tight_layout()
plt.show()
# import collections
# Tally occurrences of words in a list
# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#      cnt[word] += 1
# print(cnt)
# output:
# Counter({'blue': 3, 'red': 2, 'green': 1})
#
# # Find the ten most common words in Hamlet
# import re
# words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# Counter(words).most_common(10)
# [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
#  ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

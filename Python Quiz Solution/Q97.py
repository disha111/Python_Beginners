import re
from re import match
sentence = 'Start: a sentence: and then end bring it to an end'
pattern = re.compile(r'^S.*:')
matches = pattern.search(sentence)
print(matches)
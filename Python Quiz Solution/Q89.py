import re
from re import match
sentence = 'We are genius'
matched = re.match(r'(.*)(.*?)(.*)',sentence)
print(matched.groups())


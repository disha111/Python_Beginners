import re
from typing import Match
f=open("data.txt",'r')
result=f.read()
pattern = re.compile(r'\d{2}(SOECE)\d{5}')
file =  pattern.finditer(result)
e_no = []
for line in file:
    e_no.append(line)
for i in e_no:
    print(i)
f.close()


import re
from re import match
f=open("data.txt",'r')
result=f.read()
pattern = re.compile(r"https?://+[-\w.]+[.A-Za-z0-9]")
file =  pattern.finditer(result)
url=[]
for line in file:
    url.append(line)
for i in url:
    print(i[match])
f.close()

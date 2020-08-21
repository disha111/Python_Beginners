import re
f=open("data.txt",'r')
result=f.read()
pattern = re.compile(r"https?://+[-\w.]+[.A-Za-z0-9]")
file =  pattern.finditer(result)
dom=[]
for line in file:
    dom.append(line)
print("List of All Url")
for i in dom:
    print(i)

p = re.compile(r"https?://+[-\w.]+(com|in|edu)")
file = p.finditer(result)
dom=[]
for line in file:
    dom.append(line)
print("List of TOP Level Domain Url")
for i in dom:
    print(i)
f.close()

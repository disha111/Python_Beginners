import re
f=open("data.txt",'r')
result=f.read()
pattern = re.compile(r"M[.A-Za-z0-9-]+\D\S+")
file =  pattern.finditer(result)
name=[]
for line in file:
    name.append(line)
    #print(line)
for i in name:
    print(i)
f.close()

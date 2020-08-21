import re
f=open("data.txt",'r')
result=f.read()
#pattern = re.compile(r"\w\D.\w[a-zA-Z0-9]@\w+\S{4}_\D")
pattern = re.compile(r"[.A-Za-z0-9-]+@[A-Za-z.-]+[.A-Za-z0-9.-]")
file =  pattern.finditer(result)
email=[]
for line in file:
    email.append(line)
for i in email:
    print(i)
f.close()

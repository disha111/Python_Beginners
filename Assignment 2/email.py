import re
f=open("data.txt",'r')
result=f.read()
#pattern = re.compile(r"\w\D.\w[a-zA-Z0-9]@\w+\S{4}_\D")
pattern = re.compile(r"[.\w-]+@[\w.-]+[.\w.-]")
file =  pattern.finditer(result)
email=[]
for line in file:
    email.append(line)
for i in email:
    print(i.group())
f.close()

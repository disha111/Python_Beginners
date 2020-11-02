import re
p = re.compile('hello')
r = p.match('hello everyone')
print(r.group(0))
rr = p.match('hello','hello everyone')
print(rr.group(1))

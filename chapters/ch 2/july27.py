import re
search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
@#$%^&(*((^&)))
123.456.7896
563-658-7566
563--658--7566
456*254&2454
cat
mat 
pat
bat

Mr. Patel
Mr Doshi
Ms. Riya
Mrs. Tiya
Mr. T
18SOECE11017
18SOECE11018
18SOECE11019
+919797978457
+915689568948
+91 5689568948

mganandiya776@rku.edu
riya-patel@yahoo.com
SGHETIYA728@RKU.ac.in
jgarach002@rku.in
'''
sent = "this is a group of ce and it class."
print(r"\tRKU")#Row String to print special command like \n \t etc....
a=r"\tabc"#Row String
print(a)
#pattern = re.compile(r'\d{3}[-.]+\d{3}[-.]+\d{4}')
#pattern = re.compile(r'[^c]at')
#pattern = re.compile(r'^this')
#pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')//Name
#pattern = re.compile(r'\d{2}(SOECE)\d{5}')//ROLL NO
#pattern = re.compile(r'[+91]\d{10}') PHONE NUMBER
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z]+\.([a-z])\.[a-z]{2,3}+')
matched =  pattern.finditer(search)
list = []
for match in matched:
    list.append(match.group(0))
for i in list:
    print(i)

    """import re
from re import match
search = '''
mganandiya776@rku.edu
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
@#$%^&(*((^&)))
123.456.7896
563-658-7566
563--658--7566
456*254&2454
cat
mat 
pat
bat

Mr. Patel
Mr Doshi
Ms. Riya
Mrs. Tiya
Mr. T
18SOECE11017
18SOECE11018
18SOECE11019
+919797978457
+915689568948
+91 5689568948


riya-patel@yahoo.com
SGHETIYA728@RKU.ac.in
jgarach002@rku.in
'''
sent = "this is a group of ce and it class."
############ Match Function ###############
#match = re.match(r'\w+',sent)####### FINDING PATERN OF BEGINING OF THE STRING
#print(match)
############ Search Function ###############
#match = re.search(r'is',sent) #### Finding pattern in whole string
#print(match)
############ Findall Function ###############
#match = re.findall(r'is',sent)
#print(match)
match = re.findall(r'[a-zA-Z0-9-]+@[a-z]+\.[a-z]+\.?[a-z]+',search)
print(match)"""
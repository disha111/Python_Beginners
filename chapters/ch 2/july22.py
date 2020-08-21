import re
search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
@#$%^&(*((^&)))
123-456-7896
563-658-7566
456*254&2454
'''
print(r"\tRKU")#Row String to print special command like \n \t etc....
a=r"\tabc"#Row String
print(a)
########################## REGULAR EXPRATATION #############################
#pattern = re.compile(r'\W') special characters including \n all printed
#pattern = re.compile(r'\w')\w is stands for word include digits, capital and small alpha and _ underscore
# OR pattern = re.compile(r'\d') \d stands for digits 
#pattern = re.compile(r'.') . is stand for all characters accepts new line
#pattern = re.compile(r'\D')\D is stands for accepts digits all characters are displayed
#pattern = re.compile(r'\s') \s its print whitespace
#pattern = re.compile(r'\S')# it prints digits , alpha , underscore , non whitespaces
#pattern = re.compile(r'abc')
#pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matched =  pattern.finditer(search)
for match in matched:
    print(match)
print(search[1:4])
#uy5mchd
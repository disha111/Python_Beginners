f=open("file.txt",'r')
result=f.readlines()
for line in result:
    if(line[0]==line[-1]):
        print("The string is a palindrome" ,line)
    else:
        print("Not a palindrome",line)
f.close()

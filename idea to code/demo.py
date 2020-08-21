f=open("file.txt",'r')
result=f.readlines()
#print(result)
for line in result:
    string=result
    if(string[0]==string[-1]):
        print("The string is a palindrome" ,string)
    else:
        print("Not a palindrome",string)
f.close()
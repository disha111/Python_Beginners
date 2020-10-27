def myfun(msg1,msg2):
    list=[]
    for x in msg1:
        if x==" ":
            continue
        else:
            for y in msg2:
                if x == " ":
                    continue
                elif x == y:
                    if x in list:
                        break
                    else:
                        list.append(x)
                        break
    output="".join(list)
    if len(output)==0:
        return -1
    else:
        return output
print(myfun(input("Enter String1 : "),input("Enter String2 : ")))



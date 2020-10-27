def myfun(message): 
    msg = "" 
    i = 0
    while (i <= len(message)-1): 
        count = 1
        ch = message[i] 
        j = i 
        while (j < len(message)-1): 
            if (message[j] == message[j+1]): 
                count = count+1
                j = j+1
            else: 
                break
        msg=msg+str(count)+ch 
        i = j+1
    return msg 
msg=myfun(input()) 
print(msg) 


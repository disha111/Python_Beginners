def fizz_buzz(limit):
    for i in range(3,limit+1):
        if(i%3 == 0):
            print(i,end=' ')
        elif(i%5 == 0):
            print(i,end=' ')
no1 = int(input("Enter The Number : "))
fizz_buzz(no1)

def check(speed):
    if(speed<70):
        print("OK")
    else:
        limit = (speed-70)//5
        if(limit<=12):
            print("Points ",limit)
        else:
            print("License suspended")
speed = int(input("Enter Current Speed : "))
check(speed)

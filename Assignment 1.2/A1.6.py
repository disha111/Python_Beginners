def show_stars(rows):
    for i in range(1,rows+2):
        for j in range(1,i):
            print("*",end='')
        print("\n")
row = int(input("Enter Rows : "))
show_stars(row)

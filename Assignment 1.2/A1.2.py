def fizz_buzz(no1):
    if(no1%3 == 0 or no1%5 == 0):
        op1 = " "
        op2 = " "
        if(no1%3 == 0):
            op1 = "Fizz"
        if(no1%5 == 0):
            op2 = "Buzz"
        result = op1+op2
        return result
    else:
        return no1
no1 = int(input("Enter The Number : "))
result = fizz_buzz(no1)
print(result)
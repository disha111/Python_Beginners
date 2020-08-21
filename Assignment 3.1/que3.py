import numpy as np
ls = [] #List
size = int(input("Enter Size of List : "))
for i in range(0,size):
    ls.append(float(input()))
def display(ls):
    array = np.array(ls) # array.array = np.asfarray(ls)
    return array

arr_type = display(ls)
print("one-dimensional NumPy Array is :",arr_type)
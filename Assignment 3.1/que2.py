import numpy as np
ls =[]
print("Enter Element in Matrix : ")
for i in range(0,9):
    ls.append(int(input()))

def display(ls):
    array = np.array(ls).reshape(3,3) #two-dimensional NumPy array.
    return array
dim = display(ls)
print(dim)

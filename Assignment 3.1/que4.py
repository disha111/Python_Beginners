import numpy as np
ls = [] #List
tp = () #tuple
size = int(input("Enter Size of List and Tuple : "))
print("List input...")
for i in range(0,size):
    ls.append(int(input()))
tp = tuple(ls)
array_list = np.array(ls) #one-dimensional NumPy array from list.
array_tuple = np.array(tp) #one-dimensional NumPy array from tuple.
print("List is :",ls)
print("Tupple is :",tp)
print("one-dimensional NumPy Array From List :",array_list)
print("one-dimensional NumPy Array From Tuple :",array_tuple)
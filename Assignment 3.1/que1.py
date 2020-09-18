import numpy as np

class q1:
    def __init__(self):
        self.ls = [] #List
        self.size = int(input("Enter Size of List : "))
        for self.i in range(0,self.size):
            self.ls.append(int(input()))
        self.array = np.array(self.ls) #one-dimensional NumPy array.
        print("List is :",self.ls)
        print("one-dimensional NumPy Array is :",self.array)
q =q1()


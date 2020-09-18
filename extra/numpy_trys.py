import numpy as np
import re

# print(re.sub('morning', 'evening', 'good morning'))

# a = np.arange(100000,dtype=int)
# # print(a.size)

# import numpy as np
# ary = np.array([1,2,3,5,8])
# ary = ary + 1
# # print (ary[1])
# # print (ary[0])

# names = ['Ramesh', 'Rajesh', 'Roger', 'Ivan', 'Nico']
# print("\n".join(names))

# class test:
#       def __init__(self,a="Hello World"):
#             self.a=a

#       def display(self):
#            print(self.a)

# obj=test()
# obj.display()



# class Employee:
#     def __init__(self,first,last,pay): 
#         self.first = first
#         self.last = last
#         self.pay = pay

#     def __add__(self,other):
#         #missing code
#         return self.pay + other.pay

# emp1 = Employee("arjun","patel",700)
# emp2 = Employee("raj","joshi",900)

# print(emp1 + emp2)

# arr = np.array([
# [[1,2],
# [3,4]],

# [[5,6],
# [7,8]],

# [[5,6],
# [7,8]]

# ])
# print(arr[2,:,1])

# arr1 = np.array([1,2,3,4,5])

# arr1 + 5

# print(arr1)

# class Vegies:
#     def __init__(self, price):
#         self.price = price
# obj=Vegies(50)
 
# obj.quantity=10
# obj.bags=2
 
# print(obj.quantity+len(obj.__dict__))

# import sqlite3

# conn = sqlite3.connect(":memory:")

# class change:
#       def __init__(self, x, y, z):
#            self.a = x + y + z

# x = change(1,2,3)
# y = getattr(x, 'a')
# setattr(x, 'a', y+1)
# print(x.a) 

# arr = np.array([ [1,2,3,4,5], [6,7,8,9,10] ])
# arr[:,4] = 11
# #missing code

# print(arr)

class A:
    def one(self):
      return self.two()

    def two(self):
      return 'A'
class B(A):
    def two(self):
      return 'B'

obj1=A()
obj2=B()
print(obj2.two(),obj1.two())
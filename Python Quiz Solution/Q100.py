from matplotlib.pyplot import cla


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def __add__(self,other):
        return self.pay+other.pay
emp1 = Employee("arjun","patel",700)
emp2 = Employee("raj","joshi",900)
print(emp1+emp2)
"""def myfun():
    print("test file "+__name__)
class A:
    wheels =4
    def __init__(self):
        print("constructor is called")
    def config(self):
        print("Config fun is called...")
o1 = A()
print(o1.wheels)
o1.wheels = 2
A.wheels = 3
print(o1.wheels)
A.wheels = 30
print(A.wheels)"""
class A:
    def __init__(self):
        print("Constructor of class A")
    def fun(self):
        print("Function of class A")
class B(A):
    def __init__(self):
        super().__init__(self)
        print("Constructor of class B")
    def fun1(self):
        print("Function of class B")
if __name__ == "__main__":
    o2 = B()
    o2.fun()
    o2.fun1()
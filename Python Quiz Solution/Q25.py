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
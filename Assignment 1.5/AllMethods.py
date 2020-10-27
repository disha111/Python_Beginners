class MyClass:
    def method(self):
        return 'instance method is called'
    @classmethod
    def classmethod(cls):
        return 'class method is called'
    @staticmethod
    def staticmethod():
        return 'static method is called'
#instance
obj = MyClass()
print (obj.method())
#classmethod
print (MyClass.classmethod())
#staticmethod
print (MyClass.staticmethod())

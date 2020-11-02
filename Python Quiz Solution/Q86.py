class Test:
    def __init__(self):
        self.foo=10
        self._bar=20
        self.__baz=30
t =Test()
print(t.foo)
print(t._bar)
print(t._Test__baz)

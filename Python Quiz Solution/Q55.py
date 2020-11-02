class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo 's __new__ invoked")
    def __init__(self):
        print("Demo's __init__() invoked")
class Deerrived_Demo(Demo):
    def __new__(self):
        self.__init__(self)
        print("Deerrived_Demo 's __new__ invoked")
    def __init__(self):
        print("Deerrived_Demo's __init__() invoked")
def main():
    obj1 = Demo()
    obj2 = Deerrived_Demo()
main()
    
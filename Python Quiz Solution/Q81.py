class Test:
    def __init__(self):
        self.x=0
class Derrived_Test(Test):
    def __init__(self):
        self.y =1
def main():
    b=Derrived_Test()
    print(b.x,b.y)
main()
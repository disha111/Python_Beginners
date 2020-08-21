class A41:
    def __init__(self,path):
        self.path = path
    def r(self):
        f=open(self.path,'r')
        result=f.read()
        print(result.upper())
        f.close()
if __name__ == "__main__":
    read_file = A41('words.txt')
    read_file.r()

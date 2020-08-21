class A42:
    def __init__(self,path):
        self.path = path
    def r(self):
        f=open(self.path,'r')
        word=list()
        for line in f:
            words=line.split() 
            for n_word in words:
                if n_word not in word:
                    word.append(n_word)
        
        word.sort()
        print(word)
if __name__ == "__main__":
    Read_word = A42('text.txt')
    Read_word.r()

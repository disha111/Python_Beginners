f=open('text.txt','r')
word=list()
for line in f:
    words=line.split() 
    for n_word in words:
        if n_word not in word:
            word.append(n_word)
        
word.sort()
print(word)

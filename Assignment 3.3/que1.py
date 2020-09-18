import numpy as np
data = np.genfromtxt("Thums up.csv",skip_header=1,delimiter=';' )
result = data[:,11]
lst = []
for i in result:
    if i>5:
        lst.append(i)
w = np.savetxt('good_thumpsup.csv',lst,delimiter=',')
r = open('good_thumpsup.csv','r')
print("Data Having Quality above 5 : ")
print(r.read())
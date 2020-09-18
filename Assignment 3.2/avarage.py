import numpy as np
data = np.genfromtxt("Thums up.csv",skip_header=1,delimiter=';' )
print("Avarage of fixed acidity is : ",np.average(data[:,0]))
print("Avarage of volatile acidity is : ",np.average(data[:,1]))

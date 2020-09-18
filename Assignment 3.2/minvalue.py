import numpy as np
data = np.genfromtxt("Thums up.csv",skip_header=1,delimiter=';' )
print("Minimum Value of residual sugar is : ",np.min(data[:,3]))

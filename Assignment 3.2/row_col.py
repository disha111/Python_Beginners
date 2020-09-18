import numpy as np
row_col = np.genfromtxt("Thums up.csv",skip_header=1,delimiter=';' )
print("No of Row : ",len(row_col[:]))
print("No of Column : ",len(row_col[0,:]))
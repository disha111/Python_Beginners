import pandas as pd
data = {'fname':['raj','jay','brijesh','sanjay','rohit'],
'lname':['patel','joshi','patel','dave','patil'],
'email':['raj.patel@rku.ac.in','jay.patel@rku.ac.in','brijesh.patel@rku.ac.in','sanjay.patel@rku.ac.in','rohit.patel@rku.ac.in'],
'rank':[1,2,3,4,5]}
df = pd.DataFrame(data)
print(df.loc[~((df['fname']=='sanjay')|(df['lname']=='dave')),'email'])
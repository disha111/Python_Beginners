import pandas as pd
from pandas.core.indexes.base import Index
student = {
    'name': ['DJ', 'RJ', 'YP'], 
    'eno': ['19SOECE13021', '18SOECE11001', '19SOECE11011'], 
    'email': ['dvaghela001@rku.ac.in', 'xyz@email.com', 'pqr@email.com'],
    'year':[2019,2018,2019]
}

df = pd.DataFrame(student,index=[10,23,13])
print("Default DataFrame :\n",df)
df.sort_values('eno',inplace=True)
print("After Sorting by Values eno in DataFrame :\n",df)
df = df.sort_index()
print("After Sorting by Index eno in DataFrame :\n",df)
import pandas as pd
student = {
    'name': ['DJ', 'RJ', 'YJ'], 
    'eno': ['19SOECE13021', '18SOECE11001', '19SOECE11011'], 
    'email': ['dvaghela001@rku.ac.in', 'xyz@email.com', 'pqr@email.com']
}

df = pd.DataFrame(student)
print("Default DataFrame :\n",df)
df['sem'] = [5,3,4]
print("After adding semester column in DataFrame :\n",df)
df = df.append({'name': 'JP','sem':6}, ignore_index=True)
print("After adding row in DataFrame :\n",df)
df.drop(columns='email',inplace=True)
print("Remove Email column in DataFrame :\n",df)
df.drop(index=3,inplace=True)
print("Remove JP row in DataFrame :\n",df)
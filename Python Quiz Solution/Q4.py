import pandas as pd
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}
dummy_data2 = {
        'ID': ['1', '2', '3', '4', '5'],
        'f1': ['A', 'C', 'E', 'G', 'I'],
        'f2': ['B', 'D', 'F', 'H', 'J']}
df1 = pd.DataFrame(dummy_data1)
df2 = pd.DataFrame(dummy_data2)
df1=df1.append(df2,ignore_index=True)
print(df1)
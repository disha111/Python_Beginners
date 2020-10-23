import pandas as pd
import numpy as np

# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# # print(df.groupby('Year'), df.get_group(), df.agg(np.mean))
# filter = df['Team']=='Riders'
# df.loc[filter,'Team']='jiya'
# print(df)

# a = np.array([[1,2,3],[4,5,6]])

# for i in np.ndenumerate(a):

#     print(i)

from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0,0,0,0.1,0]

plt.pie(slices, labels = labels, explode = explode, autopct= '%1.1f%%', wedgeprops = {'edgecolor':'black'})

plt.title('My pie chart')
plt.show()
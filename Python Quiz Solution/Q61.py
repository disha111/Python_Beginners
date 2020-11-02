import pandas as pd
import numpy as np
from pandas.core import groupby
ipl_data = {'Team':['Riders','Devils','Devils','Kings','Kings','Riders','Riders'],
'Rank':[1,2,2,4,1,3,6],
'Year':[2020,2019,2020,2014,2014,2016,2015],
'Points':[1,2,3,4,5,6,7]}
df = pd.DataFrame(ipl_data)
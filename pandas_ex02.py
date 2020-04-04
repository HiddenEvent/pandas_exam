import numpy as np
import pandas as pd
import wget
from pandas import Series, DataFrame

# data from:
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)
h_index = df.groupby(["Team"])["Points"].sum()
print(h_index)
# print(h_index.unstack())

result = df.groupby('Team').filter(lambda x: x["Points"].sum() > 500)
print(result)
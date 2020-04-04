

import numpy as np
import pandas as pd
import wget
from pandas import Series, DataFrame

# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
# data_url = './housing.data' #Data URL
# #csv 타입 데이터 로드, separate는 빈공간으로 지정하고, Column은 없음
# df_data = pd.read_csv(data_url, sep='\s+', header = None)
# # print(df_data.head())
# # print(df_data)
# # values 는 값의 형태는 numpy 이다
# print(df_data.values)
# print(type(df_data.values))


# list_data = [1,2,3,4,5]
# example_obj = Series(data = list_data)
# print(example_obj)
# print(example_obj[0])


# Example from - https://chrisalbon.com/python/pandas_map_values_to_values.html

# wget.download('https://raw.githubusercontent.com/rstudio/Intro/master/data/wages.csv')

# s1 = Series(range(9))
# print(s1)
# result = s1.map(lambda x: x**2).head(5)
# print(result)

# z = {1: 'A', 2: 'B', 3: 'C'}
# result = s1.map(z)
# print(result)
#
#
# raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#         'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
#         'age': [42, 52, 36, 24, 73],
#         'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
# df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])

data_file = './wages.csv' #Data URL
df = pd.read_csv(data_file)
unique_list = df.race.unique()
unique_dic = np.array( dict( enumerate( unique_list ) ) )

unique_matrix = np.array( list( enumerate( unique_list ) ) )
print(unique_matrix)
# value = list( map(int, unique_matrix ) )
# print(value)
key = unique_matrix[:, 0].tolist()
value = unique_matrix[:,1].tolist()
print(key, value)
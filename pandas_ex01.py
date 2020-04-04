import pandas as pd

# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
data_url = './housing.data' #Data URL
#csv 타입 데이터 로드, separate는 빈공간으로 지정하고, Column은 없음
df_data = pd.read_csv(data_url, sep='\s+', header = None)
print(df_data)

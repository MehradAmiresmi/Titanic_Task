import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic_data_set = pd.read_csv(url, encoding='utf-8-sig')
"""
info, dtype, shape, sort, rank, describe, sum, mean, median, merge, 
min, max, std, var, cumsum, isnull, dropna, fillna, groupby, pivot, 

"""
print(f"{titanic_data_set.head()}\n, {titanic_data_set.info()}\n, {titanic_data_set.describe()}")
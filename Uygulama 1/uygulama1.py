import numpy as np

arr = np.array([3, 7, 10])

matrix = np.array([[3, 7, 10], [5, 12, 40]])

zero_matrix = np.zeros((3, 3))

sqrt_values = np.sqrt(arr)
log_values = np.log(arr)

mean_value = np.mean(arr)
transpose_matrix = np.transpose(matrix)

removed_element = np.delete(matrix, 1, axis=0)

import pandas as pd

series = pd.Series([15, 42, 28, 19], index=['x', 'y', 'z', 'w'])

selected_value = series.iloc[1]

row_deleted = series.drop(['x'])
column_deleted = series.drop(['y'], axis=0)

data_frame = pd.DataFrame({'Col1': [2, 4, 6], 'Col2': [5, 10, 15]})
df_info = data_frame.info()
df_stats = data_frame.describe()

print("Numpy Array:", arr)
print("Zero Matrix:\n", zero_matrix)
print("Mean Value:", mean_value)
print("Transposed Matrix:\n", transpose_matrix)
print("Pandas Series:\n", series)
print("DataFrame Info:", df_info)
print("Statistics:\n", df_stats)

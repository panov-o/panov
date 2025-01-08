# import pandas as pd
#
# # Чтение данных из CSV-файла
# data = pd.read_csv('data.csv')
#
# # Вывод первых пяти строк
# print(data.head())
#
# # Описание данных
# print(data.describe())

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
print(df.describe())

import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
print(np.mean(array))

import matplotlib.pyplot as plt

x = [1, 1, 4, 4, 1, 4]
y = [1, 4, 4, 1, 1, 4]
plt.plot(x, y)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Первый график')
plt.show()
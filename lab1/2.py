import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as scs

with open('input.txt', 'r') as f:
    file_content = f.read()
data = list(map(lambda x: float(x), file_content.replace('\n', ' ').replace(',', '.').split(' ')))

def average(arr):
    return sum(arr) / len(arr)

def vardis(arr):
    return sum((xi - average(arr)) ** 2 for xi in arr) / len(arr)

def deferr(arr):
    return np.std(arr)/np.sqrt(len(arr))

def mode(arr):
    return scs.mode(arr).mode[0]

def median(arr):
    return np.median(arr)

def quantile(arr):
    return [np.percentile(arr, 25), np.percentile(arr, 50), np.percentile(arr, 75)]

def box_with_mustache(arr):
    plt.boxplot(arr)
    plt.show()

def avdeviation(arr):
    return np.mean(arr)

def kurtosis(arr):
    return scs.kurtosis(arr)

print(average(data)) # Среднее значение выборки
print(vardis(data)) # Выборочная дисперсия
print(deferr(data)) # Стандартная ошибка
print(mode(data)) # Мода
print(median(data)) # Медиана
print(quantile(data)) # Квартили
print(avdeviation(data)) # Среднее отклонение
print(kurtosis(data)) # Эксцесс
print(min(data)) # Минимум
print(max(data)) # Максимум



box_with_mustache(data) # Усатый ящик https://habr.com/ru/post/267123/


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
    return np.std(arr) / np.sqrt(len(arr))


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


def assymetry(arr):
    return average(arr) * mode(arr) / avdeviation(arr)


print('Среднее значение выборки', average(data))
print('Выборочная дисперсия', vardis(data))
print('Стандартная ошибка', deferr(data))
print('Мода', mode(data))
print('Медиана', median(data))
print('Квартили', quantile(data))
print('Среднее отклонение', avdeviation(data))
print('Эксцесс', kurtosis(data))
print('Минимум', min(data))
print('Максимум', max(data))
print('Ассиметрия', assymetry(data))
box_with_mustache(data)  # 'Усатый ящик' https://habr.com/ru/post/267123/

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy
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


def stdev(nums):
    diffs = 0
    avg = sum(nums) / len(nums)
    for n in nums:
        diffs += (n - avg) ** (2)
    return (diffs / (len(nums) - 1)) ** (0.5)


def kurtosis(arr):
    return scs.kurtosis(arr)


def mn(arr, n): # Центральный эмпирический момент n-го порядка
    result = 0
    av = average(data)
    for x in arr:
        result += (x - av) ** n
    result /= len(arr)
    return result


def assymetry(arr):
    moment3 = 0
    avg = sum(arr) / len(arr)
    for i in arr:
        moment3 += (i - avg) ** 3
    moment3 /= len(arr)
    return moment3 ** 3 / stdev(arr) ** 3


print('Среднее значение выборки', average(data))
print('Выборочная дисперсия', vardis(data))
print('Стандартная ошибка', deferr(data))
print('Мода', mode(data))
print('Медиана', median(data))
print('Квантили', quantile(data))
print('Стандартное отклонение', stdev(data))
print('Эксцесс', kurtosis(data))
print('Минимум', min(data))
print('Максимум', max(data))
print('Ассиметрия', assymetry(data))
print(len(data))
print('m4', mn(data, 4))
print('m3', mn(data, 3))
box_with_mustache(data)  # 'Усатый ящик' https://habr.com/ru/post/267123/

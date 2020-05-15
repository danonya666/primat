import numpy as np
import scipy.stats

with open('input.txt', 'r') as f:
    file_content = f.read()

data = list(map(lambda x: float(x), file_content.replace('\n', ' ').replace(',', '.').split(' ')))


def stdev(nums):
    diffs = 0
    avg = sum(nums) / len(nums)
    for n in nums:
        diffs += (n - avg) ** (2)
    return (diffs / (len(nums) - 1)) ** (0.5)


def mean_confidence_interval(arr, confidence=0.95):  # по мат ожиданию
    a = 1.0 * np.array(arr)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)  # среднее арифметическое, standard error of the mean
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)  # ppf - quantile function p(n <= x)
    return m - h, m + h


def standard_deviation_confidence_interval(arr, confidence=0.95):
    n = len(arr)
    alpha = 0.025
    chisquare = 112.3934  # (83, 0.025)
    chisquare2 = 61.389  # (83, 0.975)
    tn = (((n - 1) * stdev(arr) ** 2) / chisquare) ** (1 / 2)  # случайная ошибка дисперсии нижней границы
    tb = (((n - 1) * stdev(arr) ** 2) / chisquare2) ** (1 / 2)  # случайная ошибка дисперсии верхней границы
    return [tn, tb]


print('Мат ожидание', mean_confidence_interval(data))
print('Среднеквадратичное отклонение', standard_deviation_confidence_interval(data))

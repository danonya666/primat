import numpy as np
import scipy.stats

with open('input.txt', 'r') as f:
    file_content = f.read()

data = list(map(lambda x: float(x), file_content.replace('\n', ' ').replace(',', '.').split(' ')))


def mean_confidence_interval(arr, confidence=0.95):
    a = 1.0 * np.array(arr)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a) # среднее арифметическое, standard error of the mean
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1) #
    return m, m - h, m + h


print(mean_confidence_interval(data))
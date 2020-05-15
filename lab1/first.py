import numpy
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab
from scipy.stats import cumfreq


with open('input.txt', 'r') as f:
    file_content = f.read()

data = list(map(lambda x: float(x), file_content.replace('\n', ' ').replace(',', '.').split(' ')))
# Hist
num_bins = 40
# n, bins, patches = plt.hist(data, num_bins, facecolor='blue', alpha=0.5)
import statsmodels.api as sm # recommended import according to the docs

sample = data
ecdf = sm.distributions.ECDF(sample)

x = np.linspace(min(sample), max(sample))
y = ecdf(x)
plt.step(x, y)
plt.show()

a = data # your array of numbers
num_bins = 20
counts, bin_edges = numpy.histogram(a, bins=num_bins, normed=True)
cdf = numpy.cumsum(counts)
# pylab.plot(bin_edges[1:], cdf)
plt.show()

print(sorted(data))

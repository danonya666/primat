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
num_bins = 20
n, bins, patches = plt.hist(data, num_bins, facecolor='blue', alpha=0.5)

a = data # your array of numbers
num_bins = 20
counts, bin_edges = numpy.histogram(a, bins=num_bins, normed=True)
cdf = numpy.cumsum(counts)
pylab.plot(bin_edges[1:], cdf)
plt.show()

print(sorted(data))

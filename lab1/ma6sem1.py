import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    file_content = f.read()

data = list(map(lambda x: float(x), file_content.replace('\n', ' ').replace(',', '.').split(' ')))

# Hist
num_bins = 20
n, bins, patches = plt.hist(data, num_bins, facecolor='blue', alpha=0.5)
# plt.show()

print(sorted(data))

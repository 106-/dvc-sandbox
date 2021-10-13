import numpy as np

data = np.loadtxt("raw_dataset.csv", delimiter=", ")

# 0から1に正規化する.
min_ = np.min(data, axis=0)
max_ = np.max(data, axis=0)
modified_data = (data - min_) / (max_ - min_)

np.savetxt("dataset.csv", modified_data, fmt="%g", delimiter=", ")

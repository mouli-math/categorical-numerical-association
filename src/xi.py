import numpy as np
from scipy.stats import rankdata

def xi_coefficient(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    ranks = rankdata(y, method="average")
    global_mean = np.mean(ranks)

    Dw = 0.0
    for cat in np.unique(x):
        idx = x == cat
        mean_k = np.mean(ranks[idx])
        Dw += np.sum(np.abs(ranks[idx] - mean_k))

    D = np.sum(np.abs(ranks - global_mean))
    return 0.0 if D == 0 else 1.0 - Dw / D

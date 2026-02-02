import numpy as np

def psi_score(x, y, bins=10):
    x = np.asarray(x)
    y = np.asarray(y)

    y_disc = np.digitize(y, np.histogram_bin_edges(y, bins=bins))

    def entropy(p):
        p = p[p > 0]
        return -np.sum(p * np.log(p))

    H_y = entropy(np.bincount(y_disc) / len(y_disc))
    if H_y == 0:
        return 0.0

    H_cond = 0.0
    for cat in np.unique(x):
        idx = x == cat
        p = np.bincount(y_disc[idx], minlength=y_disc.max()+1)
        p = p / np.sum(p)
        H_cond += (np.sum(idx) / len(x)) * entropy(p)

    return (H_y - H_cond) / H_y

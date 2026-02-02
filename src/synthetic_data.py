import numpy as np

def generate_synthetic_data(n=500, k=4, alpha=0.5, noise=1.0):
    x = np.random.choice(k, size=n)
    mu = np.linspace(0, 2, k)
    z = np.random.normal(size=n)
    eps = np.random.normal(scale=noise, size=n)
    y = mu[x] + alpha * z + eps
    return x, y

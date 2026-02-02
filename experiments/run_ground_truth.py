from src.synthetic_data import generate_synthetic_data
from src.xi import xi_coefficient
from src.psi import psi_score
import numpy as np

alphas = np.linspace(0, 1, 5)

for alpha in alphas:
    scores = []
    for _ in range(30):
        x, y = generate_synthetic_data(alpha=alpha)
        scores.append((xi_coefficient(x, y), psi_score(x, y)))
    print(alpha, np.mean(scores, axis=0))

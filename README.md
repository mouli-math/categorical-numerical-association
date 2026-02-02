# Bounded and Robust Measures of Association Between Categorical and Numerical Variables

This repository provides a **reference implementation** of the methods and
experiments presented in the manuscript:

> **Bounded and Robust Measures of Association Between Categorical and Numerical Variables**  

The code is released to support **reproducibility, transparency, and methodological clarity**.
It is intended as a **research reference implementation**, not as an optimized software library.

---

## 1. Overview

Quantifying association between categorical and numerical variables is a common
task in exploratory data analysis, feature relevance estimation, and statistical
diagnostics. Classical variance-based measures and modern dependence statistics
can exhibit instability, limited interpretability, or sensitivity to noise and
outliers, particularly in finite samples.

This repository implements two **bounded and robust descriptive association
measures** proposed in the paper:

- **Rank-Order Clustering Coefficient (ξ)**  
  A rank-based measure that quantifies ordinal clustering of numerical values
  within categories. It is invariant to monotonic transformations and robust to
  outliers.

- **Discretized Entropy Score (ψ)**  
  An entropy-based measure that captures normalized uncertainty reduction of a
  discretized numerical variable conditioned on a categorical variable. The
  discretization is treated as an explicit modeling choice.

Both measures are designed as **finite-sample descriptive association scores**,
not as hypothesis tests or estimators of a universal population dependence
functional.

---

## 2. Repository Structure

```
categorical-numerical-association/
│
├── src/                 # Core implementations
│   ├── xi.py             # Rank-Order Clustering Coefficient (ξ)
│   ├── psi.py            # Discretized Entropy Score (ψ)
│   ├── synthetic_data.py # Synthetic data generation
│   └── utils.py          # Utility functions
│
├── experiments/          # Scripts reproducing Section 6 experiments
│   ├── run_ground_truth.py
│   ├── run_outliers.py
│   ├── run_sample_size.py
│   ├── run_discretization.py
│   └── run_runtime.py
│
├── notebooks/
│   └── experiments_notebook.ipynb
│
├── figures/              # Generated figures corresponding to the manuscript
│
├── data/
│   └── README.md         # Explanation of synthetic data usage
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 3. Implementation Notes

- Implementations follow the definitions and algorithms described in the paper.
- Rank computation uses average ranking for ties.
- Entropy is computed using natural logarithms.
- No learning-based or neural estimators are included.

---

## 4. Installation

```bash
pip install -r requirements.txt
```

---

## 5. Reproducing Experiments

```bash
python experiments/run_ground_truth.py
python experiments/run_outliers.py
python experiments/run_sample_size.py
python experiments/run_discretization.py
python experiments/run_runtime.py
```

---

## 6. Synthetic Data

All experiments rely exclusively on synthetically generated data to ensure
controlled evaluation and reproducibility.

---

## 7. Reproducibility

- Experiments are repeated over multiple random seeds.
- Results are reported as mean ± standard deviation.
- Minor numerical differences may occur across platforms.

---

## 8. License

MIT License.

---

## 9. Citation

Please cite the corresponding paper after acceptance.

---

## 10. Contact

Refer to the manuscript for corresponding author contact details.

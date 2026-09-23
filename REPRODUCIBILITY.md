# Reproducing the Experiment

Run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_experiment.py
```

The script loads the wine dataset from scikit-learn, standardizes all 13 features, fits a two-component PCA model, and tests K-means with k from 2 through 6.

K-means uses `n_init=30` and `random_state=42`.

The selected k, silhouette score, explained-variance values, and sample count are written to `results/metrics.json`.

Package-version changes can affect small numerical details, so note your scikit-learn version when comparing runs.

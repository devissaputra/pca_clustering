# Reproducing the experiment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_experiment.py
```

Seed 42 is used for every K-means fit. Candidate cluster counts are 2 through 6.

Crucially, silhouette-based model selection is performed in the full 13-feature standardized space. PCA is fitted separately for a two-dimensional visualization. The known wine labels are used only afterward for Adjusted Rand Index and never for fitting or selecting `k`.

Outputs:

- `results/metrics.json`
- `results/figures/pca_clusters.png`
- `results/figures/silhouette_by_k.png`

Tests:

```bash
pip install pytest
pytest
```

GitHub Actions runs the tests automatically.

# PCA + Clustering: Scientific-Style Technical Report

**Status:** reproducible portfolio report, not peer reviewed.  
**Difficulty:** ★★★  
**Dataset:** UCI Wine Recognition dataset via scikit-learn

## Abstract
This project studies a concrete AI Engineering problem using a real public dataset and a fully inspectable pipeline. The project focuses on PCA, clustering, silhouette analysis, unsupervised learning. Its central engineering goal is to make data preparation, model fitting, evaluation, and limitations reproducible rather than treating the model as a black box.

## 1. Research objective
Discover latent structure in real chemical measurements using scaling, PCA, and K-means.

## 2. Data
The dataset is **UCI Wine Recognition dataset via scikit-learn**. Provenance and the original reference are documented in [`DATA.md`](../DATA.md).

## 3. Method
The implemented pipeline is:
1. Load real data
2. Scale
3. PCA
4. K-means
5. Cluster validation

## 4. Evaluation
**Primary metric(s):** Silhouette score.  
**Validation design:** unsupervised validation.  
The experiment saves machine-readable metrics and visual diagnostics so claims can be traced to an executable run.

## 5. Results
Generated metrics:
```json
{
  "best_k": 3,
  "silhouette": 0.5610505693103247,
  "pc1_variance": 0.3619884809992633,
  "pc2_variance": 0.19207490257008944,
  "n": 178
}
```

## 6. Limitations and validity
Key concern: cluster interpretation. Benchmark performance on one dataset does not imply universal performance. The project is intended to demonstrate research engineering discipline and to provide a base for stronger comparative studies.

## 7. Reproducibility
Run `python src/run_experiment.py` from the repository root after installing `requirements.txt`.

## 8. Next research extension
Add repeated cross-validation or temporal/external validation, stronger baselines, hyperparameter sensitivity, confidence intervals, and a domain-specific error analysis.

## References
- Dataset/reference page: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html

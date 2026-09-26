# PCA and K-Means Clustering

## Abstract

This experiment evaluates whether the 13 standardized chemical measurements in the Wine Recognition dataset contain unsupervised cluster structure. K-means model selection is performed in the full standardized feature space. A two-component PCA projection is used only for visualization. Known wine-class labels are withheld until after model selection, when Adjusted Rand Index is calculated as an external interpretation measure.

## Method

K-means is evaluated for k = 2 through 6 with 30 initializations and seed 42. The selected k maximizes silhouette score in the full 13-dimensional standardized space.

## Results

The selected solution has k = 3 and a full-space silhouette score of 0.2849. When the same cluster labels are viewed in the 2D PCA projection, the silhouette score is 0.5583. The first two components explain 55.41% of variance. Post-hoc ARI against the known classes is 0.8975.

## Interpretation

The stronger silhouette in the 2D projection shows why a visualization should not automatically become the modeling space. The high ARI indicates strong correspondence with known classes, but those labels did not influence clustering or k selection.

## Limitations

K-means assumes Euclidean, approximately spherical clusters. A stronger study would examine clustering stability, Gaussian mixtures, density-based methods, alternative embeddings, and resampling.


## Calculation definitions and evidence audit

Silhouette(i) = (b(i)-a(i))/max(a(i),b(i)); PCA variance share = eigenvalue / total.

a is within-cluster mean distance; b is the closest alternative-cluster mean distance. The two-dimensional silhouette is not the selection score. ARI uses known labels only after clustering and does not validate unseen-sample performance.

This unsupervised study separates clustering from visualization. K-means is selected using silhouette scores in all 13 standardized wine features, while a two-component PCA projection provides an interpretable view. The selected three-cluster solution has full-space silhouette 0.2849 and post-hoc adjusted Rand index 0.8975 against known labels; the much larger projected silhouette is explicitly not used as evidence that the full-space clusters are equally well separated.

The [calculation guide](../CALCULATIONS.md) provides exact evidence paths and a function-level implementation map.

![Study design](../assets/review_overview.svg)

![Calculation and selected evidence](../assets/review_calculations.svg)

### Selected evidence and interpretation

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| selected_k | 3 | unitless | `selected_k` |
| silhouette_full_space | 0.2848589191898987 | unitless | `silhouette_full_space` |
| silhouette_pca_view | 0.5583363740907525 | unitless | `silhouette_pca_view` |
| posthoc_adjusted_rand_index | 0.8974949815093207 | unitless | `posthoc_adjusted_rand_index` |

These values are read from `results/metrics.json`. They must be interpreted with the split, data status and limitations above. The complete data/model experiment was not rerun in this review.

### Reproduction and claim boundaries

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The figure generator can be checked with `python scripts/build_review_figures.py --check`. This verifies the displayed calculation evidence, not an independent replication of the complete scientific experiment. The manuscript is a working report, not a peer-reviewed publication.

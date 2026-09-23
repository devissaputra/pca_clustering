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

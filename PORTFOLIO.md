# PCA and K-Means Clustering

**Focus:** unsupervised model selection without letting the visualization choose the model.

K-means is fitted and evaluated in the full standardized 13-feature Wine Recognition space for k = 2 through 6. PCA is used only afterward to visualize the selected clusters in two dimensions.

The selected solution is k = 3 with a full-space silhouette score of 0.2849. The same assignments look substantially cleaner in the 2D PCA projection, where the silhouette is 0.5583, which is a useful warning about over-interpreting visual separation. Known wine labels are withheld until a post-hoc ARI check of 0.8975.

The repository includes deterministic experiment code, behavioural tests, CI, reproducibility notes, and a technical report.

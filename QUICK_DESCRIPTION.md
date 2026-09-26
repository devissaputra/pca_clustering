# PCA and K-Means Clustering

This unsupervised study separates clustering from visualization. K-means is selected using silhouette scores in all 13 standardized wine features, while a two-component PCA projection provides an interpretable view. The selected three-cluster solution has full-space silhouette 0.2849 and post-hoc adjusted Rand index 0.8975 against known labels; the much larger projected silhouette is explicitly not used as evidence that the full-space clusters are equally well separated.

See [CALCULATIONS.md](CALCULATIONS.md) for evidence and verification scope.

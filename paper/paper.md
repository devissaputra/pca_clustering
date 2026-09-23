# PCA and K-Means Clustering

## Question

Can a simple unsupervised pipeline reveal meaningful structure in real wine-chemistry measurements without using the known class labels?

## Data

I use the UCI Wine Recognition dataset through scikit-learn. It contains 178 samples and 13 numerical chemical measurements.

The supplied class labels are not used to fit PCA or K-means.

## Method

I standardize the 13 features, reduce the data to two principal components, and fit K-means for `k = 2` through `k = 6`.

For each value of `k`, I calculate the silhouette score. K-means uses `n_init=30` and `random_state=42`.

## Results

The first two principal components explain:

- PC1: 36.20%;
- PC2: 19.21%;
- combined: about 55.4%.

The strongest tested clustering used `k = 3` with a silhouette score of 0.5611.

## Interpretation

A three-cluster solution is reasonably well separated in the two-dimensional PCA representation.

That does not mean the clusters are automatically equivalent to the known wine classes. The method is unsupervised, so the cluster structure should be interpreted on its own first.

## Limitations

Only two principal components are used for clustering, so some information from the original 13 features is discarded. K-means also assumes roughly compact, Euclidean clusters.

A useful extension would test cluster stability, compare other dimensionality-reduction methods, and only then compare discovered clusters with the known labels as an external check.

## Reproduce

```bash
pip install -r requirements.txt
python src/run_experiment.py
```

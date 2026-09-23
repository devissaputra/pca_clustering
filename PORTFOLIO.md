# Portfolio Summary

## PCA and K-Means Clustering

I use PCA and K-means to explore structure in real wine-chemistry measurements without using the known class labels during fitting.

After standardization, the first two principal components retain about 55.4% of the variance. I compare k from 2 to 6 using the silhouette score.

### Images

![Project overview](assets/01_cover.svg)

![Processing pipeline](assets/02_data_pipeline.svg)

![PCA representation](assets/03_data_or_model.svg)

![Cluster evaluation](assets/04_evaluation_or_results.svg)

**Key result:** k = 3 produced the best tested silhouette score, 0.5611.

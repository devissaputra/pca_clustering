# PCA and K-Means Clustering

![Project overview](assets/01_cover.svg)

I built this project to practise unsupervised learning on a real dataset. The goal is to reduce a set of correlated chemical measurements to a simpler representation and then see whether clear groups appear without using the known class labels.

The experiment uses the UCI Wine Recognition data distributed with scikit-learn.

## Data

The dataset contains:

- 178 wine samples;
- 13 numerical chemical measurements.

I do not use the wine class labels when fitting PCA or K-means.

More detail is in [DATA.md](DATA.md).

## How the experiment works

![Processing pipeline](assets/02_data_pipeline.svg)

The workflow is straightforward:

1. standardize all 13 features;
2. reduce the data to two principal components;
3. fit K-means for `k = 2` through `k = 6`;
4. calculate the silhouette score for each value of `k`;
5. select the best internal clustering result.

I use `n_init=30` and `random_state=42` for K-means.

## Two-dimensional representation

![PCA representation](assets/03_data_or_model.svg)

The first two principal components explain:

- PC1: 36.20% of the variance;
- PC2: 19.21%;
- combined: about 55.4%.

This view is useful for seeing structure, but it is still a compressed version of the original 13-dimensional data.

## Results

![Cluster evaluation](assets/04_evaluation_or_results.svg)

The best tested solution was:

| Item | Result |
|---|---:|
| Selected number of clusters | 3 |
| Silhouette score | 0.5611 |
| Samples | 178 |

A silhouette score around 0.56 suggests reasonably separated groups in this two-dimensional PCA space.

Because this is an unsupervised experiment, I do not use the original labels to choose the number of clusters. A useful follow-up would compare the discovered groups with the known classes only after clustering, as an external interpretation step.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_experiment.py
```

On Windows, use `.venv\Scripts\activate`.

## Repository notes

- [DATA.md](DATA.md) explains the data source.
- [REPRODUCIBILITY.md](REPRODUCIBILITY.md) records the main settings.
- [paper/paper.md](paper/paper.md) contains the longer write-up.

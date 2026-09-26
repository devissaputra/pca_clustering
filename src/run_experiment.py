# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Silhouette(i) = (b(i)-a(i))/max(a(i),b(i)); PCA variance share = eigenvalue / total.
# a is within-cluster mean distance; b is the closest alternative-cluster mean distance. The two-dimensional silhouette is not the selection score. ARI uses known labels only after clustering and does not validate unseen-sample performance.

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler


SEED = 42
K_VALUES = tuple(range(2, 7))


def load_standardized():
    X, y = load_wine(return_X_y=True, as_frame=True)
    standardized = StandardScaler().fit_transform(X)
    return X, y, standardized


def evaluate_k_values(standardized, seed: int = SEED):
    scores = {}
    for k in K_VALUES:
        labels = KMeans(
            n_clusters=k,
            n_init=30,
            random_state=seed,
        ).fit_predict(standardized)
        scores[k] = float(silhouette_score(standardized, labels))
    return scores


def run_experiment(
    results_dir: str | Path = "results",
    seed: int = SEED,
    make_plots: bool = True,
):
    X, true_labels, standardized = load_standardized()
    silhouette_by_k = evaluate_k_values(standardized, seed)
    best_k = max(silhouette_by_k, key=silhouette_by_k.get)

    clusterer = KMeans(
        n_clusters=best_k,
        n_init=30,
        random_state=seed,
    )
    cluster_labels = clusterer.fit_predict(standardized)

    pca = PCA(n_components=2, random_state=seed)
    projection = pca.fit_transform(standardized)

    results = {
        "seed": int(seed),
        "n_samples": int(len(X)),
        "n_features": int(X.shape[1]),
        "selected_k": int(best_k),
        "silhouette_full_space": float(
            silhouette_score(standardized, cluster_labels)
        ),
        "silhouette_pca_view": float(
            silhouette_score(projection, cluster_labels)
        ),
        "posthoc_adjusted_rand_index": float(
            adjusted_rand_score(true_labels, cluster_labels)
        ),
        "pc1_variance": float(pca.explained_variance_ratio_[0]),
        "pc2_variance": float(pca.explained_variance_ratio_[1]),
        "silhouette_by_k": {
            str(k): score for k, score in silhouette_by_k.items()
        },
    }

    output = Path(results_dir)
    output.mkdir(parents=True, exist_ok=True)
    (output / "metrics.json").write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )

    if make_plots:
        figures = output / "figures"
        figures.mkdir(parents=True, exist_ok=True)

        plt.figure(figsize=(7, 5))
        plt.scatter(
            projection[:, 0],
            projection[:, 1],
            c=cluster_labels,
            s=35,
        )
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.title("PCA visualization of selected K-means clusters")
        plt.tight_layout()
        plt.savefig(figures / "pca_clusters.png", dpi=150)
        plt.close()

        plt.figure(figsize=(7, 5))
        plt.plot(
            list(silhouette_by_k.keys()),
            list(silhouette_by_k.values()),
            marker="o",
        )
        plt.xlabel("k")
        plt.ylabel("Silhouette score")
        plt.title("K-means validation in full standardized space")
        plt.tight_layout()
        plt.savefig(figures / "silhouette_by_k.png", dpi=150)
        plt.close()

    return results


def main() -> None:
    print(json.dumps(run_experiment(), indent=2))


if __name__ == "__main__":
    main()

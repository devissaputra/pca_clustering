# Calculation guide

## Question and evidence

Can unlabeled chemical measurements reveal wine groups?

178 wine observations and 13 standardized chemical features.

**Status:** RECORDED SMALL-SAMPLE BENCHMARK | see validation scope.

## Design

Select k=2…6 using full-space silhouette; project with PCA only for visualization; inspect known labels afterward.

## Calculation and interpretation

`Silhouette(i) = (b(i)-a(i))/max(a(i),b(i)); PCA variance share = eigenvalue / total.`

a is within-cluster mean distance; b is the closest alternative-cluster mean distance. The two-dimensional silhouette is not the selection score. ARI uses known labels only after clustering and does not validate unseen-sample performance.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| selected_k | 3 | unitless | `selected_k` |
| silhouette_full_space | 0.2848589191898987 | unitless | `silhouette_full_space` |
| silhouette_pca_view | 0.5583363740907525 | unitless | `silhouette_pca_view` |
| posthoc_adjusted_rand_index | 0.8974949815093207 | unitless | `posthoc_adjusted_rand_index` |

Source: [results/metrics.json](results/metrics.json). Values resolve directly from this file when figures are regenerated.

This unsupervised study separates clustering from visualization. K-means is selected using silhouette scores in all 13 standardized wine features, while a two-component PCA projection provides an interpretable view. The selected three-cluster solution has full-space silhouette 0.2849 and post-hoc adjusted Rand index 0.8975 against known labels; the much larger projected silhouette is explicitly not used as evidence that the full-space clusters are equally well separated.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The complete data/model experiment was not rerun in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`load_standardized`](src/run_experiment.py#L23) | Inspect the explicit implementation and its callers. |
| [`evaluate_k_values`](src/run_experiment.py#L29) | Inspect the explicit implementation and its callers. |
| [`run_experiment`](src/run_experiment.py#L41) | Inspect the explicit implementation and its callers. |
| [`main`](src/run_experiment.py#L122) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

a is within-cluster mean distance; b is the closest alternative-cluster mean distance. The two-dimensional silhouette is not the selection score. ARI uses known labels only after clustering and does not validate unseen-sample performance. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.

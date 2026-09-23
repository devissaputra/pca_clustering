from pathlib import Path

from src.run_experiment import evaluate_k_values, load_standardized, run_experiment


def test_model_selection_uses_full_feature_space():
    _, _, standardized = load_standardized()
    scores = evaluate_k_values(standardized)
    assert set(scores) == {2, 3, 4, 5, 6}
    assert max(scores, key=scores.get) == 3


def test_experiment_outputs_posthoc_label_check(tmp_path):
    result = run_experiment(tmp_path, make_plots=False)
    assert result["selected_k"] == 3
    assert result["n_features"] == 13
    assert 0.0 <= result["posthoc_adjusted_rand_index"] <= 1.0
    assert result["silhouette_full_space"] > 0.0
    assert (tmp_path / "metrics.json").exists()


def test_repository_structure():
    root = Path(__file__).resolve().parents[1]
    for relative_path in [
        "README.md",
        "DATA.md",
        "REPRODUCIBILITY.md",
        "src/run_experiment.py",
        "paper/paper.md",
        "assets/01_cover.svg",
        "assets/02_data_pipeline.svg",
        "assets/03_data_or_model.svg",
        "assets/04_evaluation_or_results.svg",
        ".github/workflows/ci.yml",
    ]:
        assert (root / relative_path).exists(), relative_path

"""
Unit tests for the modular k-NN classifier (Lab05/lab5.py).

Covers every module of A1 (encoding, imputation, distance, sorting,
neighbors, voting), the A2 weighted voting, and validates the full
classifier against sklearn's KNeighborsClassifier on the project data.
"""

import os

import numpy as np
import pandas as pd
import pytest
from scipy.spatial import distance as sd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import lab5

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lab Session Data.xlsx")


@pytest.fixture(scope="module")
def project_data():
    """Encoded and mean-imputed feature matrix and Response labels."""
    df = pd.read_excel(DATA_FILE, sheet_name="marketing_campaign")
    encoded = lab5.encode(df)
    imputed = lab5.impute(encoded, "mean")
    X = imputed.drop(columns=["Response"]).to_numpy(dtype=float)
    y = imputed["Response"].to_numpy()
    return X, y


# --- a. Encoding -------------------------------------------------------------

def test_label_encode_first_seen_order():
    assert lab5.label_encode(["b", "a", "b", "c", "a"]) == [0, 1, 0, 2, 1]


def test_one_hot_encode_columns_and_values():
    s = pd.Series(["a", "b", "a"], name="X")
    ohe = lab5.one_hot_encode(s)
    assert list(ohe.columns) == ["X_a", "X_b"]
    assert ohe.to_numpy().tolist() == [[1, 0], [0, 1], [1, 0]]


def test_encode_produces_only_numeric_columns():
    df = pd.read_excel(DATA_FILE, sheet_name="marketing_campaign")
    encoded = lab5.encode(df)
    assert encoded.select_dtypes(include="number").shape[1] == encoded.shape[1]
    assert "ID" not in encoded.columns
    assert "Marital_Status" not in encoded.columns
    assert "Year_Customer" in encoded.columns


# --- b. Imputation -----------------------------------------------------------

def test_impute_mean_matches_pandas():
    df = pd.DataFrame({"A": [1.0, 2.0, np.nan, 4.0], "B": [5.0, np.nan, 7.0, 8.0]})
    result = lab5.impute(df, "mean")
    expected = df.fillna(df.mean())
    assert np.allclose(result.to_numpy(dtype=float), expected.to_numpy(dtype=float))


def test_impute_median_matches_pandas():
    df = pd.DataFrame({"A": [1.0, 2.0, np.nan, 10.0], "B": [5.0, np.nan, 7.0, 8.0]})
    result = lab5.impute(df, "median")
    expected = df.fillna(df.median())
    assert np.allclose(result.to_numpy(dtype=float), expected.to_numpy(dtype=float))


def test_impute_mode_matches_pandas():
    df = pd.DataFrame({"A": [2.0, 2.0, np.nan, 1.0], "B": [5.0, np.nan, 7.0, 7.0]})
    result = lab5.impute(df, "mode")
    expected = df.fillna(df.mode().iloc[0])
    assert np.allclose(result.to_numpy(dtype=float), expected.to_numpy(dtype=float))


def test_impute_fills_all_missing_values():
    df = pd.DataFrame({"A": [1.0, np.nan, np.nan, 4.0]})
    result = lab5.impute(df, "mean")
    assert result.isna().sum().sum() == 0


def test_impute_income_has_no_missing_after_fill():
    df = pd.read_excel(DATA_FILE, sheet_name="marketing_campaign")
    encoded = lab5.encode(df)
    for strategy in ("mean", "median", "mode"):
        assert lab5.impute(encoded, strategy)["Income"].isna().sum() == 0


def test_mean_ignores_nan():
    assert lab5.mean([1.0, 2.0, float("nan")]) == pytest.approx(1.5)


def test_median_odd_and_even():
    assert lab5.median([3.0, 1.0, 2.0]) == pytest.approx(2.0)
    assert lab5.median([4.0, 1.0, 3.0, 2.0]) == pytest.approx(2.5)


def test_mode_tie_goes_to_smaller_value():
    assert lab5.mode([2.0, 1.0, 2.0, 1.0]) == 1.0


# --- c. Distance -------------------------------------------------------------

def test_euclidean_matches_numpy():
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 6.0, 3.0])
    assert lab5.euclidean(x, y) == pytest.approx(np.linalg.norm(x - y))


def test_manhattan_hand_computed():
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 6.0, 3.0])
    assert lab5.manhattan(x, y) == pytest.approx(7.0)


def test_minkowski_matches_scipy_random():
    rng = np.random.default_rng(7)
    x = rng.normal(size=8)
    y = rng.normal(size=8)
    for p in (1, 2, 4, 10):
        assert lab5.minkowski(x, y, p) == pytest.approx(sd.minkowski(x, y, p), rel=1e-9)


def test_distance_metric_dispatch():
    x = np.array([1.0, 2.0])
    y = np.array([4.0, 6.0])
    assert lab5.distance(x, y, "euclidean") == pytest.approx(lab5.euclidean(x, y))
    assert lab5.distance(x, y, "manhattan") == pytest.approx(lab5.manhattan(x, y))
    assert lab5.distance(x, y, "minkowski", p=3) == pytest.approx(lab5.minkowski(x, y, 3))


def test_distance_unknown_metric_raises():
    with pytest.raises(ValueError):
        lab5.distance([1.0], [2.0], "cosine")


# --- d. Sorting --------------------------------------------------------------

@pytest.mark.parametrize("algo", ["insertion", "merge", "quick", "heap"])
def test_sort_algorithms_match_sorted(algo):
    rng = np.random.default_rng(42)
    values = rng.integers(0, 20, size=60).tolist()
    assert lab5.SORT_ALGORITHMS[algo](values) == sorted(values)


@pytest.mark.parametrize("algo", ["insertion", "merge", "quick", "heap"])
def test_sort_algorithms_handle_floats_with_duplicates(algo):
    values = [3.5, 1.2, 2.7, 1.2, 0.9, 3.5, 2.7]
    assert lab5.SORT_ALGORITHMS[algo](values) == sorted(values)


@pytest.mark.parametrize("algo", ["insertion", "merge", "quick", "heap"])
def test_sort_algorithms_handle_empty_and_single(algo):
    assert lab5.SORT_ALGORITHMS[algo]([]) == []
    assert lab5.SORT_ALGORITHMS[algo]([7]) == [7]


def test_sort_by_distance_orders_pairs(algo="insertion"):
    distances = [3.5, 1.2, 2.7, 1.2, 0.9]
    result = lab5.sort_by_distance(distances, algo)
    assert result == [(0.9, 4), (1.2, 1), (1.2, 3), (2.7, 2), (3.5, 0)]


def test_sort_by_distance_unknown_algo_raises():
    with pytest.raises(ValueError):
        lab5.sort_by_distance([1.0, 2.0], "bogosort")


# --- e. Neighbors ------------------------------------------------------------

def test_find_neighbors_basic():
    distances = [3.0, 1.0, 4.0, 2.0]
    assert lab5.find_neighbors(distances, 2) == [1, 3]


def test_find_neighbors_keeps_all_ties_at_boundary():
    distances = [1.0, 2.0, 2.0, 2.0, 5.0]
    assert lab5.find_neighbors(distances, 2) == [0, 1, 2, 3]


def test_find_neighbors_k_larger_than_n_returns_all():
    distances = [1.0, 2.0, 3.0]
    assert lab5.find_neighbors(distances, 10) == [0, 1, 2]


def test_find_neighbors_empty():
    assert lab5.find_neighbors([], 3) == []


# --- f. Voting ---------------------------------------------------------------

def test_majority_vote_clear_winner():
    assert lab5.majority_vote(["A", "B", "A"], [1.0, 2.0, 3.0]) == "A"


def test_majority_vote_tie_nearest_tied_class_wins():
    # 2 vs 2 tie; the nearest neighbor belongs to class A.
    assert lab5.majority_vote(["A", "B", "A", "B"], [1.0, 2.0, 3.0, 4.0]) == "A"


def test_majority_vote_empty_returns_none():
    assert lab5.majority_vote([], []) is None


def test_weighted_vote_zero_distance_gets_infinite_weight():
    assert lab5.weighted_majority_vote(["A", "B"], [0.0, 5.0]) == "A"


def test_weighted_vote_can_flip_majority_vote():
    labels = ["B", "A", "A", "B", "A", "B"]
    distances = [1.0, 1.05, 1.1, 1.15, 1.2, 1.25]
    assert lab5.majority_vote(labels, distances) == "B"      # 3 vs 3, nearest is B
    assert lab5.weighted_majority_vote(labels, distances) == "A"  # closer A cluster


# --- Full classifier vs sklearn ---------------------------------------------

def test_classify_matches_sklearn_on_project_data(project_data):
    X, y = project_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    for k in (1, 3, 5):
        mine = lab5.classify(X_train, y_train, X_test, k=k, sort_algo="merge")
        ref = KNeighborsClassifier(n_neighbors=k, algorithm="brute").fit(X_train, y_train).predict(X_test)
        for i, (m, r) in enumerate(zip(mine, ref.tolist())):
            if m != r:
                # lab5 keeps every neighbour tied at the k-th boundary while
                # sklearn takes exactly k, so only a boundary tie may differ.
                d = sorted(lab5.distance(X_test[i], tr) for tr in X_train)
                assert d[k - 1] == d[k], "unexplained disagreement at row %d" % i


def test_classify_manhattan_matches_sklearn(project_data):
    X, y = project_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    mine = lab5.classify(X_train, y_train, X_test, k=3, metric="manhattan", sort_algo="merge")
    ref = KNeighborsClassifier(n_neighbors=3, metric="manhattan").fit(X_train, y_train).predict(X_test)
    assert mine == ref.tolist()


def test_classify_all_sort_algorithms_agree(project_data):
    X, y = project_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    reference = lab5.classify(X_train, y_train, X_test, k=3, sort_algo="merge")
    for algo in ("insertion", "quick", "heap"):
        assert lab5.classify(X_train, y_train, X_test, k=3, sort_algo=algo) == reference


def test_weighted_classify_matches_sklearn_distance_weights(project_data):
    X, y = project_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    for k in (1, 3, 5):
        mine = lab5.classify(X_train, y_train, X_test, k=k, weighted=True, sort_algo="merge")
        ref = KNeighborsClassifier(n_neighbors=k, weights="distance", algorithm="brute").fit(X_train, y_train).predict(X_test)
        for i, (m, r) in enumerate(zip(mine, ref.tolist())):
            if m != r:
                d = sorted(lab5.distance(X_test[i], tr) for tr in X_train)
                assert d[k - 1] == d[k], "unexplained disagreement at row %d" % i


def test_classify_accuracy_on_project_data(project_data):
    X, y = project_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    preds = lab5.classify(X_train, y_train, X_test, k=3, sort_algo="merge")
    assert lab5.accuracy(y_test, preds) > 0.8

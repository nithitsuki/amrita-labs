import os
import sys
from contextlib import redirect_stdout
from io import StringIO

import pandas as pd

_LAB03_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Lab03")
_cwd = os.getcwd()
os.chdir(_LAB03_DIR)
sys.path.insert(0, _LAB03_DIR)
try:
    with redirect_stdout(StringIO()):
        import lab03
finally:
    sys.path.remove(_LAB03_DIR)
    os.chdir(_cwd)

label_encode = lab03.label_encode
one_hot_encode = lab03.one_hot_encode
minkowski = lab03.minkowski
mean = lab03.mean


def encode(data):
    encoded = data.copy()
    education_order = ["Basic", "2n Cycle", "Graduation", "Master", "PhD"]
    education_map = {level: i for i, level in enumerate(education_order)}
    encoded["Education"] = [education_map[v] for v in encoded["Education"]]
    marital = one_hot_encode(encoded["Marital_Status"])
    for column in marital.columns:
        encoded[column] = marital[column].values
    encoded = encoded.drop(columns=["Marital_Status"])
    encoded["Year_Customer"] = [pd.to_datetime(t).year for t in encoded["Dt_Customer"]]
    return encoded.drop(columns=["Dt_Customer", "ID"])


def median(values):
    values = sorted([v for v in values if v == v])
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2.0


def mode(values):
    values = [v for v in values if v == v]
    if not values:
        return float("nan")
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    best_value = None
    best_count = -1
    for v in sorted(counts):
        if counts[v] > best_count:
            best_value = v
            best_count = counts[v]
    return best_value


def impute(data, strategy="mean"):
    strategies = {"mean": mean, "median": median, "mode": mode}
    fill = strategies[strategy]
    imputed = data.copy()
    for column in imputed.select_dtypes(include="number").columns:
        if imputed[column].isna().any():
            imputed[column] = imputed[column].fillna(fill(imputed[column]))
    return imputed


def euclidean(x, y):
    return minkowski(x, y, 2)


def manhattan(x, y):
    return minkowski(x, y, 1)


def distance(x, y, metric="euclidean", p=2):
    if metric == "euclidean":
        return euclidean(x, y)
    if metric == "manhattan":
        return manhattan(x, y)
    if metric == "minkowski":
        return minkowski(x, y, p)
    raise ValueError("unknown metric: %r (use euclidean, manhattan or minkowski)" % metric)


def insertion_sort(items):
    result = list(items)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge_sort(items):
    n = len(items)
    if n <= 1:
        return list(items)
    mid = n // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items):
    n = len(items)
    if n <= 1:
        return list(items)
    pivot = items[-1]
    left = [x for x in items[:-1] if x <= pivot]
    right = [x for x in items[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def heap_sort(items):
    result = list(items)
    n = len(result)

    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size and result[left] > result[largest]:
            largest = left
        if right < size and result[right] > result[largest]:
            largest = right
        if largest != root:
            result[root], result[largest] = result[largest], result[root]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(i, 0)
    return result


SORT_ALGORITHMS = {
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
}


def sort_by_distance(distances, algo="insertion"):
    if algo not in SORT_ALGORITHMS:
        raise ValueError("unknown sort algorithm: %r" % algo)
    pairs = [(float(distances[i]), i) for i in range(len(distances))]
    return SORT_ALGORITHMS[algo](pairs)


def find_neighbors(distances, k, algo="insertion"):
    sorted_pairs = sort_by_distance(distances, algo)
    n = len(sorted_pairs)
    if n == 0:
        return []
    if k >= n:
        return [index for _, index in sorted_pairs]
    kth_distance = sorted_pairs[k - 1][0]
    return [index for dist, index in sorted_pairs if dist <= kth_distance]


def majority_vote(neighbor_labels, neighbor_distances):
    if not neighbor_labels:
        return None
    counts = {}
    for label in neighbor_labels:
        counts[label] = counts.get(label, 0) + 1
    highest = max(counts.values())
    tied_classes = [label for label, count in counts.items() if count == highest]
    if len(tied_classes) == 1:
        return tied_classes[0]
    for label, dist in zip(neighbor_labels, neighbor_distances):
        if label in tied_classes:
            return label
    return tied_classes[0]


def weighted_majority_vote(neighbor_labels, neighbor_distances):
    if not neighbor_labels:
        return None
    weights = {}
    for label, dist in zip(neighbor_labels, neighbor_distances):
        weight = float("inf") if dist == 0 else 1.0 / dist
        weights[label] = weights.get(label, 0.0) + weight
    highest = max(weights.values())
    tied_classes = [label for label, w in weights.items() if w == highest]
    if len(tied_classes) == 1:
        return tied_classes[0]
    for label, dist in zip(neighbor_labels, neighbor_distances):
        if label in tied_classes:
            return label
    return tied_classes[0]


def classify(X_train, y_train, X_test, k=3, metric="euclidean", p=2,
             sort_algo="insertion", weighted=False):
    predictions = []
    for test_row in X_test:
        distances = [distance(test_row, train_row, metric, p) for train_row in X_train]
        neighbors = find_neighbors(distances, k, sort_algo)
        neighbor_labels = [y_train[i] for i in neighbors]
        neighbor_distances = [distances[i] for i in neighbors]
        if weighted:
            predictions.append(weighted_majority_vote(neighbor_labels, neighbor_distances))
        else:
            predictions.append(majority_vote(neighbor_labels, neighbor_distances))
    return predictions


def accuracy(y_true, y_pred):
    correct = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    return correct / len(y_true)


if __name__ == "__main__":
    data = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")
    print("dataset rows, columns:", data.shape)

    encoded = encode(data)
    print("\nA1a. Encoding")
    print("  raw columns:", data.shape[1], "-> encoded columns:", encoded.shape[1])
    print("  all numeric after encoding:", encoded.dtypes.isin(["int64", "float64"]).all())

    print("\nA1b. Imputation (Income carries the missing values)")
    print("  missing before imputation:", int(data["Income"].isna().sum()))
    for strategy in ("mean", "median", "mode"):
        filled = impute(encoded, strategy)
        print("  strategy=%-6s missing after: %d" % (strategy, int(filled["Income"].isna().sum())))
    imputed = impute(encoded, "mean")

    row_a = imputed.iloc[0].drop("Response").to_numpy(dtype=float)
    row_b = imputed.iloc[1].drop("Response").to_numpy(dtype=float)
    print("\nA1c. Distance between the first two patterns")
    print("  euclidean       :", round(distance(row_a, row_b, "euclidean"), 4))
    print("  manhattan       :", round(distance(row_a, row_b, "manhattan"), 4))
    print("  minkowski p = 3 :", round(distance(row_a, row_b, "minkowski", p=3), 4))

    pairs = [(3.5, 0), (1.2, 1), (2.7, 2), (1.2, 3), (0.9, 4)]
    print("\nA1d. Sorting (distance, index) pairs, algorithm is a config parameter")
    for algo in ("insertion", "merge", "quick", "heap"):
        print("  sort_algo=%-9s -> %s" % (algo, sort_by_distance([d for d, _ in pairs], algo)))

    print("\nA1e. Neighbor identification (tie-breaking at the k-th boundary)")
    tie_distances = [1.0, 2.0, 2.0, 2.0, 5.0]
    print("  distances:", tie_distances, "k=2 -> neighbor indices:",
          find_neighbors(tie_distances, 2, "merge"))
    X = imputed.drop(columns=["Response"]).to_numpy(dtype=float)
    y = imputed["Response"].to_numpy()
    sample = [distance(X[0], X[i], "euclidean") for i in range(1, 6)]
    neighbors = find_neighbors(sample, 3, "merge")
    print("  first 5 training distances from pattern 0:",
          [round(d, 4) for d in sample])
    print("  k=3 -> neighbor (index, distance):",
          [(i, round(sample[i], 4)) for i in neighbors])

    print("\nA1f. Majority voting (tie-breaking by the nearest tied class)")
    tie_labels = ["A", "B", "A", "B"]
    tie_order = [1.0, 2.0, 3.0, 4.0]
    print("  labels (nearest first):", tie_labels,
          "-> vote:", majority_vote(tie_labels, tie_order))

    print("\nA2. Weighted k-NN (weight = 1 / distance)")
    w_labels = ["B", "A", "A", "B", "A", "B"]
    w_distances = [1.0, 1.05, 1.1, 1.15, 1.2, 1.25]
    print("  labels (nearest first):", w_labels)
    print("  majority voting  ->", majority_vote(w_labels, w_distances))
    print("  weighted voting  ->", weighted_majority_vote(w_labels, w_distances))

    split = int(0.7 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    print("\nFull pipeline: %d train, %d test patterns (k=3, euclidean)"
          % (len(X_train), len(X_test)))

    small_train, small_test = X_train[:500], X_test[:30]
    for algo in ("insertion", "merge", "quick", "heap"):
        preds = classify(small_train, y_train[:500], small_test, k=3, sort_algo=algo)
        print("  sort_algo=%-9s accuracy (subset): %.4f" % (algo, accuracy(y_test[:30], preds)))

    preds = classify(X_train, y_train, X_test, k=3)
    print("  majority voting (full test set) accuracy: %.4f" % accuracy(y_test, preds))
    preds_weighted = classify(X_train, y_train, X_test, k=3, weighted=True)
    print("  weighted voting (full test set) accuracy: %.4f" % accuracy(y_test, preds_weighted))

"""
LAB EVAL PRACTICE -- complete worked solution (fill-in reference).

Each step builds on the previous one. Read the comments, then the code.
Run it: `python lab_eval_practice.py` (from inside labeval-practice/).

Steps overview (in the order they build):
  Step 1: Load data                       (mark: 0)
  Step 2: Normalisation                   (mark: 1)
  Step 3: Distance                        (mark: 1)
  Step 4: kNN from scikit-learn           (mark: 2)
  Step 5: Performance metrics             (mark: 1)
  Step 6: KMeans from scratch             (mark: 3)
  Step 7: WCSS + elbow (KMeans with WCSS) (mark: 3)
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.cluster import KMeans as SklearnKMeans

DATA_PATH = "../Lab05/Lab Session Data.xlsx"


# ---------------------------------------------------------------------------
# Step 1: LOAD DATA (warm-up)
# ---------------------------------------------------------------------------
def load_data():
    return pd.read_excel(DATA_PATH, sheet_name="marketing_campaign")


def prepare_data(df):
    data = df.copy()

    # Education: ordinal map (Basic=0 ... PhD=4)
    education_order = ["Basic", "2n Cycle", "Graduation", "Master", "PhD"]
    education_map = {level: i for i, level in enumerate(education_order)}
    data["Education"] = [education_map[v] for v in data["Education"]]

    # Marital_Status: one-hot encode, then drop the original column
    marital = pd.get_dummies(data["Marital_Status"])
    for column in marital.columns:
        data[column] = marital[column].values
    data = data.drop(columns=["Marital_Status"])

    # Dates and IDs carry no class information: drop them
    data = data.drop(columns=["ID", "Dt_Customer"])

    # Impute Income with the column mean
    data["Income"] = data["Income"].fillna(data["Income"].mean())

    X = data.drop(columns=["Response"]).to_numpy(dtype=float)
    y = data["Response"].to_numpy()
    return X, y


# ---------------------------------------------------------------------------
# Step 2: NORMALISATION (1 mark)
# ---------------------------------------------------------------------------
# Without this, columns with big numbers (Income ~ 50000) dominate columns
# with small numbers (Age ~ 50) in both distance and mean computations.
def min_max_normalise(X):
    result = X.astype(float).copy()
    for column in range(result.shape[1]):
        col_min = result[:, column].min()
        col_max = result[:, column].max()
        if col_max > col_min:
            result[:, column] = (result[:, column] - col_min) / (col_max - col_min)
        else:
            result[:, column] = 0.0  # constant column -> no spread
    return result


def z_score_normalise(X):
    result = X.astype(float).copy()
    for column in range(result.shape[1]):
        col_mean = result[:, column].mean()
        col_std = result[:, column].std()
        if col_std > 0:
            result[:, column] = (result[:, column] - col_mean) / col_std
        else:
            result[:, column] = 0.0
    return result


# ---------------------------------------------------------------------------
# Step 3: DISTANCE (1 mark)
# ---------------------------------------------------------------------------
# General Minkowski: (sum(|x_i - y_i|^p))^(1/p)
#   p = 1 -> Manhattan,  p = 2 -> Euclidean
def euclidean(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


def manhattan(x, y):
    return np.sum(np.abs(x - y))


def minkowski(x, y, p):
    return np.sum(np.abs(x - y) ** p) ** (1.0 / p)


def distance(x, y, metric="euclidean", p=2):
    if metric == "euclidean":
        return euclidean(x, y)
    if metric == "manhattan":
        return manhattan(x, y)
    if metric == "minkowski":
        return minkowski(x, y, p)
    raise ValueError("unknown metric: %r" % metric)


# ---------------------------------------------------------------------------
# Step 4: kNN FROM SCIKIT-LEARN (2 marks)
# ---------------------------------------------------------------------------
def split_data(X, y):
    return train_test_split(X, y, test_size=0.3, random_state=42)


def train_knn(X_train, y_train, k, weights="uniform"):
    model = KNeighborsClassifier(n_neighbors=k, weights=weights)
    model.fit(X_train, y_train)
    return model


# ---------------------------------------------------------------------------
# Step 5: PERFORMANCE METRICS (1 mark)
# ---------------------------------------------------------------------------
def evaluate(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))

    accuracy = (tp + tn) / len(y_true)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": np.array([[tn, fp], [fn, tp]]),
    }


# ---------------------------------------------------------------------------
# Step 6: KMEANS FROM SCRATCH (3 marks)
# ---------------------------------------------------------------------------
def kmeans(X, k, max_iter=100):
    # 1. Initialise: first k rows as centroids
    centroids = X[:k].astype(float).copy()
    labels = np.zeros(len(X), dtype=int)

    for _ in range(max_iter):
        # 2. ASSIGN: each point goes to its nearest centroid
        labels = np.array([
            int(np.argmin([euclidean(point, centroid) for centroid in centroids]))
            for point in X
        ])

        # 3. UPDATE: centroid = mean of its cluster's points
        new_centroids = []
        for cluster_index in range(k):
            cluster_points = X[labels == cluster_index]
            if len(cluster_points) == 0:
                new_centroids.append(centroids[cluster_index])  # keep old
            else:
                new_centroids.append(cluster_points.mean(axis=0))
        new_centroids = np.array(new_centroids)

        # 4. Stop when centroids stop moving
        if np.array_equal(centroids, new_centroids):
            return new_centroids, labels
        centroids = new_centroids

    return centroids, labels


# ---------------------------------------------------------------------------
# Step 7: KMEANS WITH WCSS -- ELBOW METHOD (3 marks)
# ---------------------------------------------------------------------------
def wcss(X, centroids, labels):
    # For every point: squared distance to its own centroid, summed.
    return float(np.sum((X - centroids[labels]) ** 2))


def find_elbow(ks, wcss_values):
    # Knee = the k farthest from the straight line joining the first and
    # last (k, wcss) points -- the point where the curve bends hardest.
    x1, y1 = 1.0, wcss_values[0]
    x2, y2 = float(ks[-1]), wcss_values[-1]
    distances = []
    for k, w in zip(ks, wcss_values):
        numerator = abs((y2 - y1) * k - (x2 - x1) * w + x2 * y1 - y2 * x1)
        denominator = np.hypot(y2 - y1, x2 - x1)
        distances.append(numerator / denominator)
    return ks[int(np.argmax(distances))]


# ---------------------------------------------------------------------------
# MAIN -- everything prints here; functions stay print-free.
# ---------------------------------------------------------------------------
def main():
    # Step 1 ---------------------------------------------------------------
    df = load_data()
    print("loaded:", df.shape)

    X_raw, y = prepare_data(df)
    print("X:", X_raw.shape, "classes:", np.unique(y, return_counts=True))

    # Step 2 ---------------------------------------------------------------
    X = min_max_normalise(X_raw)
    Z = z_score_normalise(X_raw)
    print("\n[Step 2] normalisation")
    print("  raw    col0 min/max :", round(X_raw[:, 0].min(), 2), round(X_raw[:, 0].max(), 2))
    print("  minmax col0 min/max :", round(X[:, 0].min(), 2), round(X[:, 0].max(), 2))
    print("  zscore col0 mean/std:", round(Z[:, 0].mean(), 4), round(Z[:, 0].std(), 4))

    # Step 3 ---------------------------------------------------------------
    print("\n[Step 3] distance between rows 0 and 1")
    for metric in ("euclidean", "manhattan", "minkowski"):
        print("  %-9s: %.4f" % (metric, distance(X[0], X[1], metric)))
    print("  minkowski p=2 == euclidean:", round(minkowski(X[0], X[1], 2), 10) == round(euclidean(X[0], X[1]), 10))

    # Step 4 ---------------------------------------------------------------
    X_train, X_test, y_train, y_test = split_data(X, y)
    print("\n[Step 4] kNN over k (train=%d test=%d)" % (len(X_train), len(X_test)))

    ks = list(range(1, 16, 2))
    uniform_scores, weighted_scores = [], []
    for k in ks:
        uniform = train_knn(X_train, y_train, k, "uniform").score(X_test, y_test)
        weighted = train_knn(X_train, y_train, k, "distance").score(X_test, y_test)
        uniform_scores.append(uniform)
        weighted_scores.append(weighted)
        print("  k=%2d uniform=%.4f weighted=%.4f" % (k, uniform, weighted))

    plt.plot(ks, uniform_scores, marker="o", label="uniform")
    plt.plot(ks, weighted_scores, marker="s", label="weighted (distance)")
    plt.xlabel("k")
    plt.ylabel("accuracy")
    plt.legend()
    plt.grid()
    plt.savefig("knn_k_compare.png")
    print("  saved knn_k_compare.png")

    best_k = ks[int(np.argmax(uniform_scores))]
    print("  best k (uniform):", best_k)
    best_model = train_knn(X_train, y_train, best_k, "uniform")

    # Step 5 ---------------------------------------------------------------
    print("\n[Step 5] performance metrics (best k=%d)" % best_k)
    y_pred = best_model.predict(X_test)
    metrics = evaluate(y_test, y_pred)
    for name, value in metrics.items():
        if name == "confusion_matrix":
            print("  confusion matrix:\n", value)
        else:
            print("  %-15s: %.4f" % (name, value))

    print("  sklearn comparison:")
    print("    accuracy : %.4f" % accuracy_score(y_test, y_pred))
    print("    precision: %.4f" % precision_score(y_test, y_pred))
    print("    recall   : %.4f" % recall_score(y_test, y_pred))
    print("    f1       : %.4f" % f1_score(y_test, y_pred))
    print("    cm       :\n", confusion_matrix(y_test, y_pred))

    # Step 6 ---------------------------------------------------------------
    print("\n[Step 6] kmeans from scratch, k=3")
    centroids, labels = kmeans(X, 3)
    print("  centroids:\n", np.round(centroids, 3))
    sizes = [int(np.sum(labels == c)) for c in range(3)]
    print("  cluster sizes:", sizes)

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=10, alpha=0.7)
    plt.scatter(centroids[:, 0], centroids[:, 1], c="red", marker="x", s=120, label="centroids")
    plt.xlabel("feature 0")
    plt.ylabel("feature 1")
    plt.legend()
    plt.savefig("kmeans_clusters.png")
    print("  saved kmeans_clusters.png")

    # Step 7 ---------------------------------------------------------------
    print("\n[Step 7] WCSS elbow")
    k_range = list(range(1, 11))
    wcss_values = [wcss(X, *kmeans(X, k)) for k in k_range]
    for k, w in zip(k_range, wcss_values):
        print("  k=%2d  wcss=%.2f" % (k, w))

    plt.figure()
    plt.plot(k_range, wcss_values, marker="o")
    plt.xlabel("k")
    plt.ylabel("WCSS")
    plt.grid()
    plt.savefig("elbow.png")
    print("  saved elbow.png")

    elbow_k = find_elbow(k_range, wcss_values)
    print("  detected elbow k:", elbow_k)
    elbow_centroids, elbow_labels = kmeans(X, elbow_k)
    print("  elbow WCSS: %.2f" % wcss(X, elbow_centroids, elbow_labels))
    print("  elbow cluster sizes:", [int(np.sum(elbow_labels == c)) for c in range(elbow_k)])

    print("  sklearn KMeans inertia comparison:")
    for k in k_range:
        sklearn_kmeans = SklearnKMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
        print("    k=%2d  mine=%.2f  sklearn=%.2f" % (k, wcss_values[k - 1], sklearn_kmeans.inertia_))


if __name__ == "__main__":
    main()
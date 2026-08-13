import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import lab5

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")


def prepare():
    encoded = lab5.encode(df)
    imputed = lab5.impute(encoded, "mean")
    X = imputed.drop(columns=["Response"]).to_numpy(dtype=float)
    y = imputed["Response"].to_numpy()
    return X, y


def a1():
    print("\nA1. encoding and imputation")
    encoded = lab5.encode(df)
    print("raw columns:", df.shape[1], "encoded columns:", encoded.shape[1])
    print("all numeric after encoding:", encoded.select_dtypes(include="number").shape[1] == encoded.shape[1])
    print("missing before imputation:", int(encoded["Income"].isna().sum()))
    for strategy in ("mean", "median", "mode"):
        filled = lab5.impute(encoded, strategy)
        print("strategy=%-6s missing after: %d" % (strategy, int(filled["Income"].isna().sum())))


def a2():
    print("\nA2. distance, sorting, neighbors, voting")
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 6.0, 3.0])
    print("euclidean       :", round(lab5.distance(x, y, "euclidean"), 4))
    print("manhattan       :", round(lab5.distance(x, y, "manhattan"), 4))
    print("minkowski p = 3 :", round(lab5.distance(x, y, "minkowski", p=3), 4))
    pairs = [(3.5, 0), (1.2, 1), (2.7, 2), (1.2, 3), (0.9, 4)]
    for algo in ("insertion", "merge", "quick", "heap"):
        print("sort_algo=%-9s -> %s" % (algo, lab5.sort_by_distance([d for d, _ in pairs], algo)))
    tie_distances = [1.0, 2.0, 2.0, 2.0, 5.0]
    print("neighbors k=2 with ties:", lab5.find_neighbors(tie_distances, 2, "merge"))
    tie_labels = ["A", "B", "A", "B"]
    tie_order = [1.0, 2.0, 3.0, 4.0]
    print("majority vote  :", lab5.majority_vote(tie_labels, tie_order))
    print("weighted vote  :", lab5.weighted_majority_vote(tie_labels, tie_order))


def a3(X, y):
    print("\nA3. train-test split (sklearn)")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    print("train:", X_train.shape, "test:", X_test.shape)
    print("train class counts:", np.unique(y_train, return_counts=True))
    print("test class counts :", np.unique(y_test, return_counts=True))
    return X_train, X_test, y_train, y_test


def a4(X_train, y_train):
    print("\nA4. sklearn kNN k=3")
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X_train, y_train)
    print("fitted on %d patterns" % len(X_train))
    return neigh


def a5(neigh, X_test, y_test):
    print("\nA5. test accuracy")
    print("score:", round(neigh.score(X_test, y_test), 4))


def a6(neigh, X_test, y_test):
    print("\nA6. predict behavior")
    preds = neigh.predict(X_test)
    print("first 10 predictions:", preds[:10].tolist())
    print("first 10 actuals    :", y_test[:10].tolist())
    print("matches:", int((preds == y_test).sum()), "of", len(y_test))
    print("predicted class counts:", np.unique(preds, return_counts=True))


class KNN:
    def __init__(self, k=3, metric="euclidean", weighted=False, sort_algo="merge"):
        self.k = k
        self.metric = metric
        self.weighted = weighted
        self.sort_algo = sort_algo

    def fit(self, X_train, y_train):
        self.X_train = np.asarray(X_train, dtype=float)
        self.y_train = np.asarray(y_train)
        return self

    def predict(self, X_test):
        return lab5.classify(self.X_train, self.y_train, X_test, k=self.k,
                             metric=self.metric, weighted=self.weighted,
                             sort_algo=self.sort_algo)

    def score(self, X_test, y_test):
        return lab5.accuracy(np.asarray(y_test), self.predict(X_test))


def a7(X_train, X_test, y_train, y_test):
    print("\nA7. own Fit/Predict/Score")
    knn = KNN(k=3).fit(X_train, y_train)
    preds = knn.predict(X_test)
    print("first 10 predictions:", preds[:10])
    print("score:", round(knn.score(X_test, y_test), 4))
    return knn


def a8(X_train, X_test, y_train, y_test):
    print("\nA8. mine vs sklearn over k")
    ks = list(range(1, 16, 2))
    mine = []
    lib = []
    for k in ks:
        m = KNN(k=k).fit(X_train, y_train).score(X_test, y_test)
        s = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train).score(X_test, y_test)
        mine.append(m)
        lib.append(s)
        print("k=%2d mine=%.4f sklearn=%.4f" % (k, m, s))
    plt.plot(ks, mine, marker="o", label="mine")
    plt.plot(ks, lib, marker="s", label="sklearn")
    plt.xlabel("k")
    plt.ylabel("accuracy")
    plt.legend()
    plt.grid()
    plt.savefig("knn_compare.png")
    print("saved knn_compare.png")
    return ks, mine, lib


def a9(X_train, X_test, y_train, y_test, ks, mine, lib):
    print("\nA9. weighted kNN vs A8")
    mine_w = []
    lib_w = []
    for k in ks:
        m = KNN(k=k, weighted=True).fit(X_train, y_train).score(X_test, y_test)
        s = KNeighborsClassifier(n_neighbors=k, weights="distance").fit(X_train, y_train).score(X_test, y_test)
        mine_w.append(m)
        lib_w.append(s)
        print("k=%2d mine=%.4f sklearn=%.4f" % (k, m, s))
    plt.plot(ks, mine, marker="o", label="mine unweighted (A8)")
    plt.plot(ks, mine_w, marker="^", label="mine weighted")
    plt.plot(ks, lib_w, marker="s", label="sklearn weighted")
    plt.xlabel("k")
    plt.ylabel("accuracy")
    plt.legend()
    plt.grid()
    plt.savefig("knn_weighted_compare.png")
    print("saved knn_weighted_compare.png")


if __name__ == "__main__":
    print(df.shape)
    a1()
    a2()
    X, y = prepare()
    X_train, X_test, y_train, y_test = a3(X, y)
    neigh = a4(X_train, y_train)
    a5(neigh, X_test, y_test)
    a6(neigh, X_test, y_test)
    a7(X_train, X_test, y_train, y_test)
    ks, mine, lib = a8(X_train, X_test, y_train, y_test)
    a9(X_train, X_test, y_train, y_test, ks, mine, lib)

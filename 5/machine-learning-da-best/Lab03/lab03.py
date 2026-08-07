import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import distance as sd

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")
print(df.shape)


def a1():
    print("\nA1. feature types")
    for c in df.columns:
        n = df[c].nunique()
        t = "cat" if n < 20 else "num"
        print(c, df[c].dtype, n, t)


def label_encode(s):
    mp = {}
    res = []
    for v in s:
        if v not in mp:
            mp[v] = len(mp)
        res.append(mp[v])
    return res


def one_hot_encode(s):
    lev = []
    for v in s:
        if v not in lev:
            lev.append(v)
    rows = []
    for v in s:
        rows.append([1 if v == l else 0 for l in lev])
    return pd.DataFrame(rows, columns=["%s_%s" % (s.name, l) for l in lev])


def a2():
    print("\nA2. encoding")
    e = label_encode(df["Education"])
    print(dict(zip(df["Education"], e)))
    print(e[:5])
    o = one_hot_encode(df["Marital_Status"])
    print(list(o.columns))
    print(o.head())


def a3():
    print("\nA3. encoded dataset")
    d = df.copy()
    eord = ["Basic", "2n Cycle", "Graduation", "Master", "PhD"]
    em = {e: i for i, e in enumerate(eord)}
    d["Education"] = [em[v] for v in d["Education"]]
    o = one_hot_encode(d["Marital_Status"])
    for c in o.columns:
        d[c] = o[c].values
    d = d.drop(columns=["Marital_Status"])
    d["Year_Customer"] = [pd.to_datetime(t).year for t in d["Dt_Customer"]]
    d = d.drop(columns=["Dt_Customer", "ID"])
    print("before:", df.shape[1], "after:", d.shape[1])
    return d


def minkowski(x, y, p):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    tot = 0.0
    for i in range(len(x)):
        tot += abs(x[i] - y[i]) ** p
    return tot ** (1.0 / p)


def a4():
    print("\nA4. custom minkowski")
    x = np.array([1, 2, 3])
    y = np.array([4, 6, 3])
    print(minkowski(x, y, 1), minkowski(x, y, 2), minkowski(x, y, 3))


def a5(enc):
    print("\nA5. p from 1 to 10")
    num = enc.select_dtypes(include=np.number)
    x = num.iloc[0].to_numpy()
    y = num.iloc[1].to_numpy()
    ps = list(range(1, 11))
    ds = [minkowski(x, y, p) for p in ps]
    for p, dd in zip(ps, ds):
        print(p, round(dd, 4))
    plt.plot(ps, ds, marker="o")
    plt.xlabel("p")
    plt.ylabel("distance")
    plt.grid()
    plt.savefig("minkowski_plot.png")
    print("saved plot")
    return x, y, ps, ds


def a6(x, y, ps):
    print("\nA6. mine vs scipy")
    for p in ps:
        mine = minkowski(x, y, p)
        lib = sd.minkowski(x, y, p)
        print(p, round(mine, 6), round(lib, 6), abs(mine - lib))


def dot(a, b):
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s


def euc_len(a):
    s = 0
    for v in a:
        s += v * v
    return s ** 0.5


def a7():
    print("\nA7. dot and euclidean length")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("dot:", dot(a, b), "numpy:", np.dot(a, b))
    print("len a:", euc_len(a), "numpy:", np.linalg.norm(a))
    print("len b:", euc_len(b), "numpy:", np.linalg.norm(b))

def mean(s):
    s = [v for v in s if v == v]
    return sum(s)/len(s)

def variance(s):
    mu = mean(s)
    res = 0
    for v in s:
        res += (v-mu)**2
    return (res/len(s))

def std_dev(s):
    return variance(s)**0.5


def a8():
    print("\nA7. custom dot, variance, and std.deviation")
    a = mean(df["Income"])
    print(f"avg income: {a}")


def a9():
    print("\nA9. mine vs numpy on a few cols")
    cols = ["MntWines", "Recency", "MntMeatProducts"]
    x = df[cols].to_numpy()
    mm = [mean(x[:, i]) for i in range(x.shape[1])]
    ss = [std_dev(x[:, i]) for i in range(x.shape[1])]
    nm = x.mean(axis=0)
    ns = x.std(axis=0)
    for i, c in enumerate(cols):
        print(c, "mean", round(mm[i], 2), "vs", round(nm[i], 2), "| std", round(ss[i], 2), "vs", round(ns[i], 2))


def a10():
    print("\nA10. histogram of MntWines")
    f = df["MntWines"].to_numpy()
    cnt, bins = np.histogram(f, bins=10)
    for i in range(len(cnt)):
        print("%d-%d: %d" % (bins[i], bins[i + 1], cnt[i]))
    plt.hist(f, bins=10, edgecolor="black")
    plt.xlabel("MntWines")
    plt.ylabel("count")
    plt.grid()
    plt.savefig("hist_mntwines.png")
    print("mean:", round(mean(f), 2), "var:", round(variance(f), 2))

def a11(k, points):
    centroids = []
    for i in range(k):
        centroids.append(list(points[i]))
    # loop
    centroids_changed = True
    while centroids_changed:
        # step 1: assign every point to its nearest centroid
        clusters = []
        for _ in range(k):
            clusters.append([])
        for p in points:
            dists = []
            for c in centroids:
                diffs = []
                for a, b in zip(p, c):
                    diffs.append(a - b)
                dists.append(euc_len(diffs))
            nearest = dists.index(min(dists))
            clusters[nearest].append(p)

        # step 2: recompute each centroid as the mean of its cluster
        new_centroids = []
        for cluster in clusters:
            n = len(cluster)
            avg = []
            for i in range(len(cluster[0])):
                total = 0
                for v in cluster:
                    total += v[i]
                avg.append(total / n)
            new_centroids.append(avg)
        centroids_changed = centroids != new_centroids
        centroids = new_centroids
    # final
    print("Centroids: ", centroids)


if __name__ == "__main__":
    a1()
    a2()
    enc = a3()
    a4()
    x, y, ps, ds = a5(enc)
    a6(x, y, ps)
    a7()
    a8()
    a9()
    a10()
    points = [[0,1],[1,1],[2,2],[3,3],[-1,1],[0,-1],[-1,-1]]
    a11(3,points)

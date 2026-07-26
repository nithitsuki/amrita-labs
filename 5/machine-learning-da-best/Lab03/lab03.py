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


if __name__ == "__main__":
    a1()
    a2()
    enc = a3()
    a4()
    x, y, ps, ds = a5(enc)
    a6(x, y, ps)

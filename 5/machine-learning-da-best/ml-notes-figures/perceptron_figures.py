#!/usr/bin/env python3
"""Generate the figures used by the "Perceptron and Neural Networks" notes.

Run:
    uv run --with matplotlib --with numpy --with scikit-learn \
        python ml-notes-figures/perceptron_figures.py

Outputs (PNG) are written next to this script.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron

HERE = Path(__file__).resolve().parent

POS = "#1f77b4"   # class +1 / positive
NEG = "#d62728"   # class -1 / negative
LINE = "#2ca02c"  # decision boundary
NEUTRAL = "#7f7f7f"
GRID = "#cccccc"

plt.rcParams.update({
    "figure.dpi": 140,
    "savefig.bbox": "tight",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def save(fig, name):
    path = HERE / name
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path.relative_to(HERE.parent))


# ---------------------------------------------------------------------------
# Figure 1: activation functions
# ---------------------------------------------------------------------------
def activation_functions():
    z = np.linspace(-6, 6, 600)
    step = np.where(z >= 0, 1.0, 0.0)
    sigmoid = 1.0 / (1.0 + np.exp(-z))
    tanh = np.tanh(z)
    relu = np.maximum(0.0, z)

    fig, axes = plt.subplots(2, 2, figsize=(8.5, 6.0))
    for ax, y, title, color in [
        (axes[0, 0], step, "Step (Heaviside)", "#9467bd"),
        (axes[0, 1], sigmoid, "Sigmoid", "#1f77b4"),
        (axes[1, 0], tanh, "Tanh", "#2ca02c"),
        (axes[1, 1], relu, "ReLU", "#d62728"),
    ]:
        ax.plot(z, y, color=color, linewidth=2.4)
        if title.startswith("Step"):
            ax.plot([0], [0], marker="o", color=color, markerfacecolor="white")
            ax.plot([0], [1], marker="o", color=color)
            ax.set_ylim(-0.2, 1.2)
        ax.axhline(0, color=NEUTRAL, linewidth=0.8)
        ax.axvline(0, color=NEUTRAL, linewidth=0.8)
        ax.set_title(title)
        ax.set_xlabel("z")
        ax.set_ylabel("f(z)")
    fig.suptitle("Activation functions: output y = f(z)", fontweight="bold")
    fig.tight_layout()
    save(fig, "perceptron_activation_functions.png")


# ---------------------------------------------------------------------------
# Figure 2: AND / OR are linearly separable, XOR is not
# ---------------------------------------------------------------------------
def logic_gates():
    pts = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = {
        "AND": np.array([0, 0, 0, 1]),
        "OR": np.array([0, 0, 1, 1]),
        "XOR": np.array([0, 1, 1, 0]),
    }

    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.0))
    xg = np.linspace(-0.6, 1.6, 200)
    for ax, (name, y) in zip(axes, labels.items()):
        for p, cls in zip(pts, y):
            ax.scatter(
                p[0], p[1], s=180,
                color=POS if cls == 1 else NEG,
                edgecolor="black", linewidth=1.0, zorder=3,
            )
        ax.set_xlim(-0.6, 1.6)
        ax.set_ylim(-0.6, 1.6)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")

        if name == "AND":
            # w=(1,1), b=-1.5  ->  x1 + x2 = 1.5
            ax.plot(xg, 1.5 - xg, color=LINE, linewidth=2.2)
            ax.fill_between(xg, 1.5 - xg, 1.7, color=LINE, alpha=0.12)
            ax.set_title("AND: separable")
        elif name == "OR":
            # w=(1,1), b=-0.5  ->  x1 + x2 = 0.5
            ax.plot(xg, 0.5 - xg, color=LINE, linewidth=2.2)
            ax.fill_between(xg, 0.5 - xg, 1.7, color=LINE, alpha=0.12)
            ax.set_title("OR: separable")
        else:
            # No line can separate XOR. Show two failed candidates.
            ax.plot(xg, 0.5 - xg, color=NEUTRAL, linewidth=1.6,
                    linestyle="--", label="attempt 1")
            ax.plot(xg, 1.0 - xg, color=NEUTRAL, linewidth=1.6,
                    linestyle=":", label="attempt 2")
            ax.legend(fontsize=8, loc="lower left")
            ax.set_title("XOR: not separable")
    fig.suptitle(
        "A single perceptron draws one straight line "
        "(green = its decision boundary)",
        fontweight="bold",
    )
    fig.tight_layout()
    save(fig, "perceptron_logic_gates.png")


# ---------------------------------------------------------------------------
# Figure 3: XOR solved by two hidden units
# ---------------------------------------------------------------------------
def xor_solution():
    pts = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    xg = np.linspace(-0.6, 1.6, 200)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4))

    # (a) input space with the two hidden-unit lines
    for p, cls in zip(pts, y):
        ax1.scatter(p[0], p[1], s=190,
                    color=POS if cls == 1 else NEG,
                    edgecolor="black", linewidth=1.0, zorder=3)
    # h1 = OR: x1 + x2 = 0.5   ;   h2 = NAND: x1 + x2 = 1.5
    ax1.plot(xg, 0.5 - xg, color="#1f77b4", linewidth=2.2,
             label="$h_1$ = OR  ($x_1+x_2=0.5$)")
    ax1.plot(xg, 1.5 - xg, color="#ff7f0e", linewidth=2.2,
             label="$h_2$ = NAND  ($x_1+x_2=1.5$)")
    ax1.fill_between(xg, 0.5 - xg, 1.5 - xg, color=LINE, alpha=0.15,
                     label="both hidden units fire")
    ax1.set_xlim(-0.6, 1.6)
    ax1.set_ylim(-0.6, 1.6)
    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xlabel("$x_1$")
    ax1.set_ylabel("$x_2$")
    ax1.set_title("(a) Input space: two hidden lines")
    ax1.legend(fontsize=7.5, loc="lower left")

    # (b) hidden space (h1, h2): the classes become separable
    h1 = np.array([0, 1, 1, 1])   # OR
    h2 = np.array([1, 1, 1, 0])   # NAND
    for a, b, cls in zip(h1, h2, y):
        ax2.scatter(a, b, s=190,
                    color=POS if cls == 1 else NEG,
                    edgecolor="black", linewidth=1.0, zorder=3)
    hg = np.linspace(-0.6, 1.6, 200)
    ax2.plot(hg, 1.5 - hg, color=LINE, linewidth=2.2)
    ax2.set_xlim(-0.6, 1.6)
    ax2.set_ylim(-0.6, 1.6)
    ax2.set_xticks([0, 1])
    ax2.set_yticks([0, 1])
    ax2.set_xlabel("$h_1$ (OR)")
    ax2.set_ylabel("$h_2$ (NAND)")
    ax2.set_title("(b) Hidden space: now separable")
    ax2.annotate("output = AND$(h_1,h_2)$",
                 xy=(1.02, 0.55), xytext=(0.05, -0.42),
                 fontsize=9, color=LINE)

    fig.suptitle("XOR solved by a hidden layer that learns new features",
                 fontweight="bold")
    fig.tight_layout()
    save(fig, "perceptron_xor_solution.png")


# ---------------------------------------------------------------------------
# Figure 4: 2-2-1 network diagram for XOR
# ---------------------------------------------------------------------------
def xor_network():
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.axis("off")

    xs = {"x1": (0.0, 0.72), "x2": (0.0, 0.28)}
    hs = {"h1": (0.5, 0.78), "h2": (0.5, 0.22)}
    ys = {"y": (1.0, 0.5)}

    edges = [
        ("x1", "h1", 1, 0), ("x2", "h1", 1, 0),
        ("x1", "h2", -1, 0), ("x2", "h2", -1, 0),
        ("h1", "y", 1, 0), ("h2", "y", 1, 0),
    ]
    for a, b, w, _ in edges:
        (x0, y0), (x1, y1) = xs.get(a, hs.get(a)), hs.get(b, ys.get(b))
        color = POS if w > 0 else NEG
        ax.add_patch(FancyArrowPatch(
            (x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=12,
            color=color, linewidth=2.0, shrinkA=16, shrinkB=16))
        dy = {"h1": 0.045, "h2": -0.045, "y": 0.035}[b]
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + dy, f"{w:+d}",
                color=color, fontsize=10, ha="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))

    def node(x, y, label, color):
        ax.scatter([x], [y], s=1500, color=color, edgecolor="black",
                   linewidth=1.4, zorder=3)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=10, fontweight="bold", zorder=4)

    node(*xs["x1"], "$x_1$", "#c7d9ec")
    node(*xs["x2"], "$x_2$", "#c7d9ec")
    node(*hs["h1"], "$h_1$", "#d9ead3")
    node(*hs["h2"], "$h_2$", "#d9ead3")
    node(*ys["y"], "$y$", "#f4cccc")

    ax.text(0.5, 0.95, "hidden layer", ha="center", fontsize=10,
            style="italic", color="#555555")
    ax.text(0.5, 0.05, "bias:  $h_1$ = OR ($b=-0.5$)    "
                       "$h_2$ = NAND ($b=+1.5$)    $y$ = AND ($b=-1.5$)",
            ha="center", fontsize=9, color="#555555")
    ax.set_xlim(-0.15, 1.15)
    ax.set_ylim(0.0, 1.02)
    ax.set_title("XOR network: 2 inputs - 2 hidden neurons - 1 output",
                 fontweight="bold")
    save(fig, "perceptron_xor_network.png")


# ---------------------------------------------------------------------------
# Figure 5: single perceptron vs MLP on non-linear data
# ---------------------------------------------------------------------------
def nonlinear_boundary():
    X, y = make_moons(n_samples=300, noise=0.20, random_state=42)

    def draw(ax, model, title):
        model.fit(X, y)
        xx, yy = np.meshgrid(
            np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 400),
            np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 400),
        )
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        ax.contourf(xx, yy, Z, levels=[-0.5, 0.5, 1.5],
                    colors=["#fde0df", "#dbeafe"], alpha=0.8)
        ax.contour(xx, yy, Z, levels=[0.5], colors=[LINE], linewidths=2.2)
        ax.scatter(X[y == 0, 0], X[y == 0, 1], s=22, color=NEG,
                   edgecolor="white", linewidth=0.4)
        ax.scatter(X[y == 1, 0], X[y == 1, 1], s=22, color=POS,
                   edgecolor="white", linewidth=0.4)
        ax.set_title(title)
        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.6))
    draw(ax1, Perceptron(max_iter=1000, eta0=0.1, random_state=0),
         "Single perceptron: one straight line")
    draw(ax2, MLPClassifier(hidden_layer_sizes=(32, 32), activation="tanh",
                            max_iter=8000, random_state=0),
         "MLP (32+32 hidden): curved boundary")
    fig.suptitle("Why a straight line is not enough - and the fix",
                 fontweight="bold")
    fig.tight_layout()
    save(fig, "perceptron_nonlinear_boundary.png")


# ---------------------------------------------------------------------------
# Figure 6: universal approximation - sums of ridges
# ---------------------------------------------------------------------------
def universal_approximation():
    x = np.linspace(-1.0, 1.0, 600)
    target = np.sin(2 * np.pi * x) * 0.5 + 0.5
    gamma = 10.0

    # Nested, well-spread hidden-unit centers (van der Corput sequence in
    # [-1, 1]). A nested sequence guarantees that adding a hidden unit never
    # increases the error, so the error curve is monotone.
    def vdc(n, base=2):
        out = []
        for i in range(1, n + 1):
            f, r, k = 1.0, 0.0, i
            while k > 0:
                f /= base
                r += f * (k % base)
                k //= base
            out.append(r)
        return np.array(out)

    centers = 2.0 * vdc(64) - 1.0
    # sigmoid ridge basis (hidden layer with fixed weights)
    H = 1.0 / (1.0 + np.exp(-gamma * (x[:, None] - centers[None, :])))

    def fit_ridges(n_units):
        A = np.hstack([H[:, :n_units], np.ones((x.size, 1))])  # + output bias
        coef, *_ = np.linalg.lstsq(A, target, rcond=None)
        return A @ coef

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.4))

    ax1.plot(x, target, color="black", linewidth=2.6, label="target $f(x)$",
             zorder=5)
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, 3))
    for n, c in zip([2, 5, 20], colors):
        ax1.plot(x, fit_ridges(n), color=c, linewidth=1.8,
                 label=f"sum of {n} sigmoids")
    ax1.set_title("(a) Sum of hidden sigmoids fits the target")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$f(x)$")
    ax1.legend(fontsize=8)

    # (b) error falls as the number of hidden units grows
    sizes = [1, 2, 3, 5, 8, 12, 20, 40]
    errors = [np.sqrt(np.mean((fit_ridges(n) - target) ** 2)) for n in sizes]
    ax2.plot(sizes, errors, marker="o", color="#1f77b4", linewidth=2.0)
    ax2.set_yscale("log")
    ax2.set_xlabel("number of hidden units $N$")
    ax2.set_ylabel("RMSE")
    ax2.set_title("(b) Error drops as width grows")
    fig.suptitle("Universal approximation: enough hidden units approximate "
                 "any continuous function", fontweight="bold")
    fig.tight_layout()
    save(fig, "perceptron_uat_approximation.png")


if __name__ == "__main__":
    activation_functions()
    logic_gates()
    xor_solution()
    xor_network()
    nonlinear_boundary()
    universal_approximation()
    print("all figures generated")

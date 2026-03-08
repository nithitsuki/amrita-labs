### 1. Fundamental Probability

- [ ] **Axioms and Basic Probability:** Sample spaces, event definitions, and basic theoretical probability calculations (e.g., combinations, permutations, leap year logic)
- [ ] **Addition Rules**
    - [ ] Mutually exclusive events: $P(A \cup B) = P(A) + P(B)$
    - [ ] Non-mutually exclusive events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- [ ] **Multiplication Rules & Independence**
    - [ ] Sampling with replacement (independent) vs. without replacement (dependent)
    - [ ] Proving mathematical independence: $P(A \cap B) = P(A)P(B)$
- [ ] **Conditional Probability**
    - [ ] Applying the formula: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
    - [ ] Using probability tables to find conditional margins
- [ ] **Total Probability & Bayes' Theorem**
    - [ ] Calculating total probability across multiple branches (e.g., defect rates across multiple plants)
    - [ ] Calculating posterior probabilities given a prior observation (Bayes' Theorem)

### 2. 1D Random Variables

- [ ] **Discrete Random Variables (PMF)**
    - [ ] Verifying a valid PMF: $\sum_{x} p(x) = 1$
    - [ ] Calculating interval probabilities: $P(a \le X < b)$
- [ ] **Continuous Random Variables (PDF)**
    - [ ] Verifying a valid PDF: $\int_{-\infty}^{\infty} f(x) dx = 1$
    - [ ] Solving for unknown constants (e.g., finding $k$ in a PDF)
    - [ ] Calculating interval probabilities via integration
- [ ] **Cumulative Distribution Function (CDF)**
    - [ ] Constructing $F(x)$ from a PMF (step function) or integrating a PDF
    - [ ] Using the CDF to find point or interval probabilities: $P(X > a) = 1 - F(a)$

### 3. Expectation & Moments

- [ ] **Mathematical Expectation (Mean)**
    - [ ] Calculating $E(X) = \sum x \cdot p(x)$ (discrete)
    - [ ] Calculating $E(X) = \int x \cdot f(x) dx$ (continuous)
    - [ ] Expectation of functions: $E(g(X))$
- [ ] **Variance and Standard Deviation**
    - [ ] Calculating $V(X) = E(X^2) - [E(X)]^2$
    - [ ] Applying linear transformations: $V(aX + b) = a^2V(X)$
- [ ] **Moment Generating Functions (MGF)**
    - [ ] Calculating $M_X(t) = E(e^{tX})$
    - [ ] Deriving mean and variance strictly from the MGF (1st and 2nd derivatives evaluated at $t=0$)
- [ ] **Chebyshev's Inequality:** Finding upper bounds or lower bounds for probability distributions without knowing the exact distribution

### 4. Standard Distributions

You must know the PMF/PDF, MGF, Mean, and Variance formulas for all six.

- [ ] **Geometric Distribution**
    - [ ] Probability of first success on the $k$-th trial
    - [ ] Memoryless property (discrete)
- [ ] **Binomial Distribution**
    - [ ] Identifying fixed $n$ independent trials with probability of success $p$
    - [ ] Calculating exact, at least, or at most probabilities
- [ ] **Poisson Distribution**
    - [ ] Modeling events over a continuous interval (time, distance, volume) given an average rate $\lambda$
    - [ ] Poisson approximation to the Binomial distribution ($n$ is large, $p$ is small)
- [ ] **Uniform Distribution**
    - [ ] Identifying parameters $a$ and $b$ for constant probability over an interval
    - [ ] Calculating probabilities using length ratios
- [ ] **Exponential Distribution**
    - [ ] Modeling time until an event or failure time given parameter $\lambda$ or mean $\beta$
    - [ ] Applying the continuous memoryless property
- [ ] **Normal Distribution**
    - [ ] Standardizing $X$ to $Z$: $Z = \frac{X - \mu}{\sigma}$
    - [ ] Using the standard normal table to find probabilities or reverse-lookup for critical $z$-values/cutoffs

### 5. 2D Random Variables

- [ ] **Joint PMF (Discrete)**
    - [ ] Verifying $\sum \sum p(x,y) = 1$
    - [ ] Reading bivariate probability tables
- [ ] **Joint PDF (Continuous)**
    - [ ] Verifying $\int \int f(x,y) dx dy = 1$ over a defined 2D region
    - [ ] Setting up double integrals with dependent limits (e.g., integration bounds for $1 < x < y < 2$)
- [ ] **Marginal Probability**
    - [ ] Summing out columns/rows in JPMF
    - [ ] Integrating out the opposing variable in JPDF: $f_X(x) = \int f(x,y) dy$
- [ ] **Conditional Probability**
    - [ ] Calculating $f(x|y) = \frac{f(x,y)}{f_Y(y)}$
    - [ ] Calculating conditional expectation: $E(X|Y=y)$
- [ ] **Stochastic Independence:** Proving $f(x,y) = f_X(x)f_Y(y)$ for all $x$ and $y$
- [ ] **Covariance and Correlation**
    - [ ] Calculating $Cov(X,Y) = E(XY) - E(X)E(Y)$
    - [ ] Calculating the correlation coefficient
    - [ ] Variance of linear combinations: $V(aX \pm bY)$

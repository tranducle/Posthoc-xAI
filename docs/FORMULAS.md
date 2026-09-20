# Calculation formulas

Let (N=84) denote the final included-study corpus unless a different denominator is stated.

## Prevalence

For any mutually exclusive or binary category:

[
\text{Prevalence}(c) = \frac{n_c}{N}\times 100.
]

Percentages are rounded to one decimal place.

For sensitivity subsets, the denominator is the number of studies in that subset rather than 84.

## Multi-label method prevalence

xAI-method and model-family fields can contain more than one label per study. For a method (m):

[
n_m = \sum_{i=1}^{N} I(m \in M_i),
]

where (M_i) is the set of labels assigned to study (i). Multi-label counts can therefore sum to more than (N).

## Exact agreement

For two coding passes (A) and (B) over (n) studies:

[
P_o = \frac{1}{n}\sum_{i=1}^{n} I(A_i=B_i).
]

The reported reliability estimates use the 72-study holdout set after a 12-study calibration set.

## Cohen kappa

For nominal axes:

[
\kappa = \frac{P_o-P_e}{1-P_e},
]

where (P_e) is the chance agreement calculated from the two marginal label distributions.

Explanation role and mixed-purpose xAI use unweighted Cohen kappa.

## Quadratic-weighted Cohen kappa

For ordered axes, category agreement receives a quadratic weight based on category distance. With (k) ordered categories:

[
w_{ij}=1-\left(\frac{i-j}{k-1}\right)^2.
]

Weighted observed and expected agreement are inserted into the same kappa form:

[
\kappa_w=\frac{P_{o,w}-P_{e,w}}{1-P_{e,w}}.
]

Trust evidence, operational evidence, validation gate, reproducibility, and claim risk use quadratic weighting.

## Gwet AC1

For (q) labels, let (p_j) be the mean marginal probability of label (j) across the two coding passes:

[
p_j=\frac{n_{Aj}+n_{Bj}}{2n}.
]

The chance-agreement term is:

[
P_e^{AC1}=\frac{1}{q-1}\sum_{j=1}^{q} p_j(1-p_j).
]

Then:

[
AC1=\frac{P_o-P_e^{AC1}}{1-P_e^{AC1}}.
]

The released script implements these formulas directly from the two coding-pass columns.

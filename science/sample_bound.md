# Sampling, error allocation and clean return

This file combines the [weighted phase bound](weighted_error.md) and the [coherent stopping clock](coherent_stopping.md). Fix $0<\epsilon<1$ and a public floor $b>0$ with $p(x)\ge b$ on every address. The source is fixed and IID. All sample blocks below are fresh and mutually independent.

Use the notation

```math
a_j=2^{-j},\quad
J=\left\lceil\log_2\frac2b\right\rceil,\quad
L=J+1,\quad
R=\left\lceil\log_4\frac{16}{\epsilon}\right\rceil,
\quad K=RL.
```

There are $K$ forward detection stages and $K$ inverse stages. The central clock phase and the two-level Hadamards use no examples. The error allocation reserves $\epsilon/4$ for deterministic stopping error, $\epsilon/2$ for stochastic phase compilation and $\epsilon/4$ for finite gate synthesis.

## Local sampling cost on each ideal image

At stage $(r,j)$ the ideal phase has time $t_j=\pi/a_j$. Immediately after its first two-level Hadamard, the magnitude on the phase-controlled clock label is at most the magnitude of the previously active component. For a one-labeled address it is therefore bounded by

```math
4^{-r}\min\!\left\{1,\frac{a_j}{p(x)}\right\}.
```

The extra factor $1/\sqrt2$ could improve constants and is omitted. Zero-labeled addresses contribute no sampled phase error. Consequently the weighted estimate gives

```math
\nu_1=\max_x p(x)f(x)c_x\le4^{-r}a_j.
```

If this phase is compiled from $M$ examples, its encoded-input channel error is at most

```math
\frac{2t_j^2\nu_1}{M}
\le\frac{\kappa_{rj}}M,
\qquad
\kappa_{rj}=\frac{2\pi^2\,4^{-r}}{a_j}.
```

The input-image interpretation matters. The compiler does not apply a worst-case-workspace diamond bound at every stage. It applies the weighted bound on the actual ideal encoded input to that stage, uniformly over the original input and its reference.

## The middle comparison and the return path

Let $W=F(I\otimes|0\rangle)$ be the ideal forward detection isometry. The central clock phase obeys

```math
\|DW-WO_f\|\le2\cdot4^{-R}.
```

The corresponding channel change is at most $4\cdot4^{-R}\le\epsilon/4$. For the inverse-half comparison, replace $DW$ by $WO_f$. The remaining ideal inverse sequence now returns the clock exactly: $F^\dagger WO_f=(I\otimes|0\rangle)O_f$.

Before inverse stage $i$, the canonical comparison state is $O_f$ times the corresponding forward-prefix state. Address-wise signs commute with every clock operation. More explicitly, if $W_{i-1}$ is the forward prefix before $F_i=B_iP_iB_i$, then the canonical input to its inverse phase, after the first inverse $B_i$, is

```math
P_iB_iW_{i-1}O_f.
```

The phase $P_i$ does not alter the norm on its controlled clock label. Thus that norm equals its forward value, up to the irrelevant address-wise sign. The same coefficient $\kappa_{rj}$ therefore bounds the inverse streamed phase, which uses negative time and a fresh block of examples.

This argument does not assert that the imperfect physical middle reflection leaves the exact forward image. Its departure from that image has already been charged once by the middle channel change.

For completeness, the hybrid can be ordered so that every local stochastic estimate uses one of these canonical images. First replace the physical forward phase blocks by their ideal blocks, expanding each difference with an ideal prefix and an actual suffix. Next make the middle comparison $DW\mapsto WO_f$. Then replace inverse phase blocks in their execution order. Before every inverse replacement the earlier inverse blocks in its prefix are ideal; subsequent physical channels form a trace-norm-contracting suffix. The triangle inequality adds the local bounds. All estimates hold with an arbitrary reference, so this is an initialized-input diamond bound for the full output registers.

## Allocating integer sample counts

Let $\mathcal I$ index the $2K$ forward and inverse phase calls, and assign each its coefficient $\kappa_i=\kappa_{rj}$. Define the public scalar

```math
T=\sum_{i\in\mathcal I}\sqrt{\kappa_i}
=2\sqrt2\,\pi
\left(\sum_{r=0}^{R-1}2^{-r}\right)
\left(\sum_{j=0}^{J}a_j^{-1/2}\right).
```

The coefficients depend only on $b,\epsilon$ and the public stage indices. They do not depend on $p(x)$ or an address-to-frequency table. Choose

```math
M_i=\left\lceil\frac{2T\sqrt{\kappa_i}}{\epsilon}\right\rceil.
```

Every $M_i$ is a positive integer. Then

```math
\sum_{i\in\mathcal I}\frac{\kappa_i}{M_i}
\le\frac\epsilon{2T}
\sum_{i\in\mathcal I}\sqrt{\kappa_i}
=\frac\epsilon2,
```

and the total number of fresh examples satisfies

```math
M_{\mathrm{tot}}=\sum_iM_i
\le\frac{2T^2}{\epsilon}+2K.
```

The first geometric sum is at most two. Since $a_J>b/4$,

```math
\sum_{j=0}^{J}a_j^{-1/2}
\le\frac{a_J^{-1/2}}{1-2^{-1/2}}
<\frac{2}{(1-2^{-1/2})\sqrt b}.
```

It follows that

```math
T<\frac{8\sqrt2\,\pi}{(1-2^{-1/2})\sqrt b},
```

and therefore the explicit bound

```math
M_{\mathrm{tot}}
\le
\frac{256\pi^2}{(1-2^{-1/2})^2}\,
\frac1{b\epsilon}
+2\left(1+\left\lceil\log_2\frac2b\right\rceil\right)
\left\lceil\log_4\frac{16}{\epsilon}\right\rceil
```

is sufficient. These are conservative analytic constants. The main scaling is $O(1/(b\epsilon))$; the integer-ceiling term is displayed rather than silently discarded.

The attenuation $4^{-r}$ across completed ladders is retained in this allocation. Treating each ladder as if it started with full active amplitude would introduce an unnecessary $\log^2(1/\epsilon)$ sampling factor.

## Final initialized-channel guarantee

With exact elementary gates, stochastic error contributes at most $\epsilon/2$ and the middle comparison at most $\epsilon/4$. Thus the physical average channel, including the clock output, is within $3\epsilon/4$ of

```math
\rho\longmapsto
\bigl(O_f\rho O_f^\dagger\bigr)\otimes|0\rangle\langle0|.
```

For an input entangled with a reference, the identity channel acts on that reference throughout. The formula above abbreviates that complete statement rather than assuming an unentangled input.

A digital implementation may spend the remaining $\epsilon/4$ on gate synthesis. One sufficient rule is to allocate unhalved diamond error at most $\epsilon/(4G)$ to each of the $G$ elementary gates in a fixed decomposition. The channel triangle inequality then gives total error at most $\epsilon$. The relevant gate count includes all per-example address and clock controls, two-level clock operations, and their inverses. The [resource account](resources.md) gives the gate decomposition, workspace costs and computable rational sample allocation within this budget. Arbitrary rotations are not treated as free exact operations.

Coherent query control changes only the known controls of these gates. The [controlled phase and Boolean bit queries](coherent_stopping.md#coherent-control-and-a-bit-query) have the same initialized-clock diamond guarantee and sample count.

## Several queries use several fresh source blocks

Suppose an algorithm makes at most $Q$ phase, controlled-phase or bit queries. Compile each with tolerance $\epsilon/Q$ and independent fresh blocks. A channel hybrid, allowing arbitrary intervening quantum operations and retained references, gives total error at most $\epsilon$. The resulting sample bound is

```math
M_Q
\le
\frac{256\pi^2}{(1-2^{-1/2})^2}\,
\frac{Q^2}{b\epsilon}
+2Q\left(1+\left\lceil\log_2\frac2b\right\rceil\right)
\left\lceil\log_4\frac{16Q}{\epsilon}\right\rceil.
```

This is an achievable composition bound. It is not a universal $Q^2$ lower bound for Boolean labels, and it does not make a reusable oracle available after a single finite stream. Fresh-data use and the absence of record replay are part of the interface.

## Relation to the earlier unknown-marginal compiler

Zhao et al., [arXiv:2604.07639v2, Section D.4.3 and Lemma D.18](https://arxiv.org/html/2604.07639v2), compile phase access under unknown $p$ through a global spectral threshold. Their IID specialization gives

```math
O\!\left(
\frac{p_{\max}}{p_{\min}^2}
\frac{\log^2(1/\epsilon)}{\epsilon}
\right)
```

examples. The construction here inherits the streamed commuting-phase primitive and its scalar moment estimate. Its different error accounting follows the remaining active amplitude at each scale and then allocates fresh samples accordingly. It requires a known floor $b\le p_{\min}$, but neither $p_{\max}$ nor evaluation of $p(x)$. Its cost is governed by that supplied floor, which can be weaker than the actual minimum.

The resulting dependence on rarity matches the rare-address obstruction at fixed error. Matching the full accuracy dependence is a separate question: the upper bound here scales as $1/\epsilon$, whereas the elementary no-hit lower bound only supplies a logarithmic accuracy factor. Analogue weighted-evolution lower bounds that vary $p$ do not settle that Boolean-phase gap.

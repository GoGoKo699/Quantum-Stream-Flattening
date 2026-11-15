# Examples of marginal skew

The compiler accepts an arbitrary unknown fixed marginal with a supplied positive lower bound $`b`$. The examples below illustrate its sample dependence. They do not supply the compiler with the address-to-frequency map, and they do not assert a classical learning separation.

## A normalized dyadic heavy tail

Choose an integer $`h\ge1`$. There are $`2^j`$ addresses at level $`j`$, for $`j=0,\ldots,h`$, each with probability

```math
p_j=\frac{2^{-j}}{h+1}.
```

The total mass of every level is $`1/(h+1)`$, so the distribution is normalized. Its support size and extrema are

```math
N=\sum_{j=0}^h2^j=2^{h+1}-1,
\qquad p_{\max}=\frac1{h+1},
\qquad b=\frac{2^{-h}}{h+1}.
```

The level assignments may be permuted arbitrarily among addresses. The compiler does not receive those assignments or evaluate $`p(x)`$. Labels are any fixed Boolean function.

At a fixed channel tolerance, the new sample upper scales as

```math
\frac1b=2^h(h+1)=\Theta(N\log N).
```

For comparison, the marginal-dependent coefficient in the generic QSVT construction of [Zhao et al., Lemma D.18](../references/RELATED_WORK.md#the-nearest-phase-oracle-construction) is

```math
\frac{p_{\max}}{b^2}=4^h(h+1)
=\Theta(N^2\log N).
```

The ratio of these upper-bound coefficients is $`2^h=\Theta(N)`$. This compares two compiler bounds for the same passive unknown marginal. It is neither a lower bound against the earlier method nor an end-to-end speedup over classical learning.

| $`h`$ | Addresses $`N`$ | New coefficient $`1/b`$ | Earlier coefficient $`p_{\max}/b^2`$ | Ratio |
| --- | ---: | ---: | ---: | ---: |
| 3 | 15 | 32 | 256 | 8 |
| 7 | 255 | 1,024 | 131,072 | 128 |
| 11 | 4,095 | 24,576 | 50,331,648 | 2,048 |
| 15 | 65,535 | 524,288 | 17,179,869,184 | 32,768 |

These are asymptotic coefficients, **not numerical sample budgets**: hidden constants and the error parameter still have to be included. In particular, the analytical allocation is conservative and the table predicts no finite hardware crossover.

## A seven-address illustration

Take $`h=2`$, so one address has probability $`1/3`$, two have probability $`1/6`$, and four have probability $`1/12`$. Thus $`b=1/12`$. A possible Boolean label table is

```math
(f(1),\ldots,f(7))=(1,0,1,1,0,0,1),
```

but the same circuit prescription works for every table and every assignment of those frequencies. The eighth basis state of the three-qubit address register is padding and keeps phase $`+1`$.

For $`\epsilon=0.1`$, the prescribed parameters are

```math
J=\lceil\log_2 24\rceil=5,
\qquad R=\lceil\log_4 160\rceil=4,
\qquad K=24.
```

The detection clock therefore needs five qubits, in addition to the three address qubits, reusable comparison work and any outer control. These are logical registers, not a complete device count.

For an address with label one and frequency $`p`$, one detection ladder leaves active amplitude at most

```math
\frac{a_{J+1}}p=\frac{1}{64p}\le\frac3{16}\lt \frac14.
```

The uniform four-ladder bound is consequently at most $`4^{-4}=1/256`$. The associated ideal stopping/uncompute channel error is at most $`4/256=1/64\lt \epsilon/4`$. Samples and digital gate precision use the remaining budgets in [resources](resources.md). A label-zero address remains undetected exactly in the ideal circuit, regardless of its frequency.

The late stages do not pay for the high-frequency addresses as though their full amplitudes were still active. The cosine-product bound suppresses their residual amplitude, and that suppression enters the sample allocation. This is the source of the improved marginal dependence.

## Uniform data and rare addresses

For uniform data, $`b=1/N`$, and the sample upper becomes $`O(N/\epsilon)`$ plus the explicit clock/stage overhead. There is no marginal-skew factor to remove in that case; the new result recovers the familiar uniform scale.

A positive lower bound is necessary for the full-domain task. If an allowed address has probability $`b`$, two functions differing only there generate identical records until that address appears. A suitable coherent input, or an outer control, distinguishes their ideal phase operations. Thus constant channel error requires $`\Omega(1/b)`$ samples in the worst case. The stronger precision lower derived from this no-hit event is logarithmic in $`1/\epsilon`$; it does not match the upper bound's $`1/\epsilon`$ dependence.

These examples concern a query applied during the stream. Storing every observed label in an unrestricted classical cache changes the memory model and may produce a reusable exact oracle after enough samples. That is a different resource tradeoff from this compiler's small-workspace invocation.

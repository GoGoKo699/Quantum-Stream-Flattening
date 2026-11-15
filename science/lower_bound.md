# The rare-address cost and the remaining precision gap

The upper bound depends on the least supplied address frequency. This dependence is necessary even with unlimited computation and storage. The argument concerns the Boolean oracle itself and does not use a lower bound for a probability-weighted evolution.

## Two indistinguishable streams until one address appears

Assume $N\ge2$, and choose a feasible marginal with an address $x_*$ of probability $b$. For example, put $p(x_*)=b$ and distribute the remaining probability uniformly over the other addresses; the floor remains valid because $Nb\le1$. Choose $z\ne x_*$. Let $f_0$ vanish everywhere and let $f_1$ differ only at $x_*$.

Couple the two input streams using the same iid address sequence. On the event that none of the first $M$ samples visits $x_*$, all observed records are identical. That event has probability

```math
q=(1-b)^M.
```

Any common learner has identical operations and output on that event, including its internal randomness. On its complement the trace distance between the two outputs is at most two. The implemented output distance is therefore at most $2(1-q)$ for every common input.

Apply the ideal oracles to $|+_{*,z}\rangle=(|x_*\rangle+|z\rangle)/\sqrt2$. Their outputs are orthogonal, with unhalved trace distance two. If each implementation has diamond error at most $\epsilon$, the triangle inequality gives

```math
2-2\epsilon\le2(1-q),\qquad
(1-b)^M\le\epsilon.
```

Consequently

```math
M\ge\frac{\log(1/\epsilon)}{-\log(1-b)}.
```

In the small-$b$ regime this is $\Omega(b^{-1}\log(1/\epsilon))$. At every fixed $0<\epsilon<1$, the [sample upper bound](sample_bound.md) and this lower bound give worst-case order $\Theta(1/b)$. If the supplied floor is conservative for a particular stream, the same argument uses the chosen address's actual probability; the theorem is a minimax statement over streams obeying the supplied promise.

An ordinary one-dimensional phase is unobservable, so $N=1$ is excluded from this phase-channel comparison. The controlled or bit-oracle task makes the two labels distinguishable even for $N=1$.

## What is not matched

The upper bound grows as $1/\epsilon$ and the no-hit lower bound only as $\log(1/\epsilon)$. This leaves a precision gap. Likewise, assigning a local error budget to repeated fresh invocations gives a sufficient $Q^2$ query overhead, not a matching lower bound for this Boolean task.

Theorem D.14 of [Zhao et al., arXiv:2604.07639v2](https://arxiv.org/abs/2604.07639v2), lower-bounds simulation of $U_p(t)=\operatorname{diag}(e^{itp(x)f(x)})$ by varying nearby probability laws with $f$ identically one. The target $U_p(t)$ then changes, whereas the Boolean $O_f$ stays fixed. Its accuracy/query lower bound therefore cannot be transferred to the flattened target without another argument.

Unlimited storage also changes repeated-use comparisons: a complete classical function cache can support arbitrarily many later queries once learned, with its table storage and quantum-address lookup implementation charged. The present result uses small working space and fresh data during each query. It does not establish a complete sample–space–query frontier.

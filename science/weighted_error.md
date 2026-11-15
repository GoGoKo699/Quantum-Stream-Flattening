# Averaged phase error on a coherently encoded input

The stream provides independent classical pairs $(X_\ell,f(X_\ell))$, where $X_\ell$ has a fixed distribution $p$ on $[N]$ and $f:[N]\to\lbrace 0,1\rbrace $. The distribution is not evaluated by the compiler. Its diagonal mean is useful only for the analysis:

```math
H=\sum_{x=1}^N p(x)f(x)|x\rangle\langle x|.
```

The scalar calculation below is the commuting phase calculation underlying quantum oracle sketching in Zhao et al., [arXiv:2604.07639v2, Theorem D.12](https://arxiv.org/html/2604.07639v2). The additional bound keeps the amount of input amplitude on which each random phase actually acts. That dependence is needed for the coherent stopping construction.

## A sampled controlled phase

Let $C$ be a known orthogonal projector on a work register, let $t\in\mathbb R$, and let $M\ge1$ be an integer. For one block of $M$ fresh examples, implement

```math
V=\prod_{\ell=1}^M
\exp\!\left(
\frac{it}{M}f(X_\ell)|X_\ell\rangle\langle X_\ell|\otimes C
\right).
```

This product is formed by applying each gate as its example arrives. It does not require retaining the examples or their empirical frequencies. The ideal comparison unitary is

```math
U=\exp(itH\otimes C).
```

All sampled generators commute. Put $n_x=\sum_{\ell=1}^M\mathbf1\lbrace X_\ell=x\rbrace $. The phase on the active work subspace at address $x$ is

```math
v_x=\exp\!\left(\frac{it}{M}f(x)n_x\right),
\qquad
u_x=\exp\!\left(itp(x)f(x)\right).
```

Each $n_x$ individually has the binomial distribution with parameters $M,p(x)$. The different counts need not be independent.

If $f(x)=0$, then $v_x-u_x=0$ exactly. Otherwise center the random exponent and use

```math
|e^{iz}-1-iz|\le \frac{z^2}{2}
\qquad(z\in\mathbb R).
```

The centered variable has zero mean and variance $t^2p(x)(1-p(x))/M$. Consequently

```math
\left|\mathbb E v_x-u_x\right|
\le \frac{t^2}{2M}p(x)(1-p(x))f(x)
\le \frac{t^2}{2M}p(x)f(x).
```

The corresponding mean-square difference satisfies

```math
\begin{aligned}
\mathbb E|v_x-u_x|^2
&=2-2\mathrm{Re}\!\left(u_x^*\mathbb E v_x\right)\\
&\le 2\left|\mathbb E v_x-u_x\right|
\le \frac{t^2}{M}p(x)f(x).
\end{aligned}
```

These inequalities hold for every real $t$ and positive integer $M$. They impose no small-angle condition on an individual sampled gate.

## Weighted input-image bound

Let $Q$ denote any retained input workspace. An ideal encoding that preserves the address has the form

```math
W=\sum_x |x\rangle\langle x|\otimes W_x,
```

where each $W_x:Q\to Q\otimes B$ is an isometry. This operator formulation includes a coherently controlled query, as well as the simpler case that $W_x$ appends a single address-dependent clock state. Define

```math
c_x=\Vert CW_x\Vert \in[0,1],
\qquad
\nu_q=\max_x p(x)f(x)c_x^q
\quad(q=1,2).
```

The factor $f(x)$ is essential. A zero-labeled address can remain fully active even when its sampling probability is large, but none of its samples applies a phase.

**Lemma.** With unhalved diamond norm,

```math
\left\Vert 
\mathbb E\!\left[VW(\cdot)W^\dagger V^\dagger\right]
-UW(\cdot)W^\dagger U^\dagger
\right\Vert _\diamond
\le \frac{t^2}{M}(\nu_1+\nu_2)
\le \frac{2t^2}{M}\nu_1.
```

The domain of this channel is the original address and retained-workspace input. Its output includes the encoded work. Thus the statement permits an arbitrary reference entangled with the input, while making no unsupported assertion about arbitrary initial states of $B$.

**Proof.** Write $\Delta=V-U$ and $A=(\mathbb E\Delta)W$. Expanding the channel difference gives a completely positive term and two cross terms:

```math
\mathcal R(\rho)+A\rho(UW)^\dagger+UW\rho A^\dagger,
\qquad
\mathcal R(\rho)=\mathbb E[\Delta W\rho W^\dagger\Delta^\dagger].
```

Orthogonality of the address blocks and the scalar mean bound imply

```math
\Vert A\Vert 
=\max_x |\mathbb E v_x-u_x|\,\Vert CW_x\Vert 
\le \frac{t^2}{2M}\nu_1.
```

For a map $\rho\mapsto A\rho B^\dagger$, the diamond norm is at most $\Vert A\Vert \Vert B\Vert $: after adding any reference this follows from the trace-norm inequality $\Vert AXB\Vert _1\le\Vert A\Vert \Vert X\Vert _1\Vert B\Vert $. Since $UW$ is an isometry, the two cross terms therefore contribute at most $2\Vert A\Vert $.

A completely positive map has diamond norm $\Vert \mathcal R^\dagger(I)\Vert $. Here

```math
\begin{aligned}
\mathcal R^\dagger(I)
&=W^\dagger\mathbb E[\Delta^\dagger\Delta]W\\
&=\sum_x |x\rangle\langle x|\otimes
\mathbb E|v_x-u_x|^2\,W_x^\dagger CW_x.
\end{aligned}
```

Because $C$ is a projector, $\Vert W_x^\dagger CW_x\Vert =c_x^2$. The mean-square estimate consequently gives $\Vert \mathcal R\Vert _\diamond\le t^2\nu_2/M$. Adding the three terms proves the first inequality. The second follows from $c_x^2\le c_x$. $\square$

No exact support cutoff is used in this proof. A high-frequency address is allowed to retain a small active component; its contribution is weighted by that component. Replacing this estimate by the unrestricted maximum of $p(x)$ would discard the improvement.

## Why these averaged channels compose

Every block uses fresh independent examples. Averaging its sampled gates therefore produces a completely positive trace-preserving channel that is independent of earlier sample records. The input to a block can still be an arbitrary state produced by the preceding computation, with any retained entanglement.

For channels $\mathcal E_i$ and ideal operations $\mathcal U_i$, a telescoping expansion places the $i$th difference after the ideal prefix and before the actual suffix. The suffix cannot increase its diamond norm. Accordingly, a local bound that holds on the image of that ideal prefix is sufficient; a full-workspace bound for the local gate is unnecessary.

The prefixes used by the stopping circuit preserve the address and are isometries of the form above. The [return-path argument](sample_bound.md#the-middle-comparison-and-the-return-path) identifies the correct ideal prefixes for its inverse half. It does not assume that noisy work has remained exactly on an ideal image.

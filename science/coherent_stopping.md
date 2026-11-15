# A coherent stopping clock for unknown sampling frequencies

Assume a public positive floor $b$ satisfies $p(x)\ge b$ for every address. No upper calibration is required: every probability is at most one. This file constructs the ideal stopping unitary and proves the active-amplitude envelope. The [sample bound](sample_bound.md) replaces each ideal phase by a streamed implementation.

Set

```math
a_j=2^{-j},\qquad
J=\left\lceil\log_2\frac{2}{b}\right\rceil,
\qquad L=J+1.
```

The ladder uses stages $j=0,\ldots,J$, so

```math
\frac b4<a_J\le\frac b2.
```

Choose a positive number $R$ of complete ladders and let $K=RL$. A clock has basis states $|0\rangle,|1\rangle,\ldots,|K\rangle$. The state $|0\rangle$ means that no detection has occurred, and label $i\ge1$ identifies the first detection stage. It fits in $\lceil\log_2(K+1)\rceil$ qubits. Extra computational-basis states in this binary register are never populated from the initialized input.

## One stage is a two-level Hadamard test

For stage $(r,j)$, with $r=0,\ldots,R-1$ and $j=0,\ldots,J$, use the new clock label

```math
i=rL+j+1.
```

Let $B_i$ be the two-level Hadamard on the span of $|0\rangle,|i\rangle$, acting as the identity on every other clock state. Its nontrivial matrix is

```math
B_i\big|_{\{0,i\}}=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

With $H=\sum_xp(x)f(x)|x\rangle\langle x|$, define

```math
P_i=\exp\!\left(\frac{i\pi}{a_j}H\otimes|i\rangle\langle i|\right),
\qquad F_i=B_iP_iB_i.
```

These are full unitaries on the data and clock registers. Every previous detection label is fixed by $F_i$. At the start of the forward stage the new label $i$ has zero amplitude. If the active component at address $x$ has amplitude $\beta$, then, writing $\lambda=p(x)f(x)$, the stage maps it to

```math
\beta\left[
\frac{1+e^{i\pi\lambda/a_j}}2|0\rangle
+\frac{1-e^{i\pi\lambda/a_j}}2|i\rangle
\right].
```

The active amplitude is therefore multiplied by

```math
e^{i\pi\lambda/(2a_j)}
\cos\!\left(\frac{\pi\lambda}{2a_j}\right).
```

For a zero-labeled address $\lambda=0$, every stage fixes $|0\rangle$. For a one-labeled address, detection can happen at any scale. Early detection causes no error: the final target phase is $-1$ at every such address, regardless of its frequency.

The clock replaces many separate flags because only a zero record or one first-detection label is needed. Implementing a two-level operation specified by the binary stage counter does not require a table assigning addresses to frequencies.

## The dyadic envelope holds for every frequency

Fix $f(x)=1$ and write $p=p(x)$. Within a ladder, the magnitude of its active amplitude before stage $j$ is multiplied by

```math
c_j(p)=\prod_{\ell=0}^{j-1}
\left|\cos\!\left(\frac{\pi p}{2a_\ell}\right)\right|,
\qquad c_0(p)=1.
```

The product identity

```math
\prod_{\ell=0}^{j-1}\cos(2^\ell z)
=\frac{\sin(2^jz)}{2^j\sin z}
```

follows by iterating $\sin(2z)=2\sin z\cos z$. Here $z=\pi p/2\in(0,\pi/2]$, and concavity of sine on this interval gives $\sin z\ge2z/\pi=p$. Hence

```math
c_j(p)\le\min\!\left\{1,\frac{a_j}{p}\right\}.
```

No discrete-spectrum promise is involved. The frequency can lie anywhere in $[b,1]$. After all $L$ stages in one ladder,

```math
c_L(p)\le\frac{a_L}{p}
=\frac{a_J}{2p}\le\frac14.
```

Only the still-active component enters the next ladder. Therefore, just before stage $(r,j)$, its magnitude is at most

```math
4^{-r}\min\!\left\{1,\frac{a_j}{p}\right\}.
```

In particular, multiplication by $p$ gives the bound $4^{-r}a_j$ that drives the weighted sampling estimate. It remains valid even if a high-frequency address has not been detected exactly.

## Applying the phase and returning the clock

Let $F=F_K\cdots F_1$ be the ideal detection unitary and let

```math
W=F(I\otimes|0\rangle)
```

denote its initialized-clock isometry. Apply the known clock phase

```math
D=2|0\rangle\langle0|-I.
```

At a zero-labeled address, $W$ has clock state exactly $|0\rangle$ and $D$ acts as $+1$. At a one-labeled address, the undetected component has modulus at most $4^{-R}$. On its detected component $D$ acts as the desired $-1$. Thus, for

```math
O_f=\sum_x(-1)^{f(x)}|x\rangle\langle x|,
```

we have the operator-norm estimate

```math
\|DW-WO_f\|\le2\cdot4^{-R}.
```

Applying $F^\dagger$ gives

```math
\left\|
F^\dagger DF(I\otimes|0\rangle)
-(I\otimes|0\rangle)O_f
\right\|\le2\cdot4^{-R}.
```

This compares the entire output, including the returned clock, with the intended clean output. It is not merely a bound after discarding the clock. For two isometries $A,B$, expanding their channel difference as $(A-B)\rho A^\dagger+B\rho(A-B)^\dagger$ bounds its diamond norm by $2\|A-B\|$. The induced initialized-input channels here are therefore within $4\cdot4^{-R}$ in unhalved diamond norm, including any entangled input reference.

## Coherent control and a bit query

To implement the controlled phase oracle

```math
cO_f=|0\rangle\langle0|\otimes I
+|1\rangle\langle1|\otimes O_f,
```

control the two-level Hadamards, sampled phases and central $D$ by the outer query-control qubit. Its zero branch leaves the initialized clock at zero. Its one branch is the circuit above. Since the estimate is an operator estimate on the initialized isometry, it also bounds coherence between these two branches. In particular, the construction retains the global phase needed by a controlled query.

The Boolean bit query is

```math
U_f|x,z\rangle=|x,z\oplus f(x)\rangle.
```

Conjugating $cO_f$, with $z$ as its control, by Hadamards on $z$ implements $U_f$. This uses the same sample blocks and the same clock-return guarantee. The inverse of either Boolean query equals the query itself. Arbitrary initial states of the clock are outside the claim; the complete guarantee concerns its stated zero initialization and clean return.

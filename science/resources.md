# Resources and digital implementation

The compiler consumes a fresh classical sample stream while acting on a quantum input that is already present. This page prices that invocation, including controls, work registers, counters, finite precision and the reverse detection circuit. The proofs cover [weighted channel error](weighted_error.md), [coherent stopping](coherent_stopping.md) and the [sample bound](sample_bound.md); the source comparison is in [related work](../references/RELATED_WORK.md).

## Parameters and channel convention

Let $n=\lceil\log_2N\rceil$, let $0<b\le p(x)$ be a supplied lower bound, and take $0<\epsilon<1$. Using the public upper bound $p(x)\le1$ avoids any need to estimate $p_{\max}$. Define

$$
a_j=2^{-j},\qquad
J=\left\lceil\log_2\frac{2}{b}\right\rceil,
\qquad L=J+1,
$$

$$
R=\left\lceil\log_4\frac{16}{\epsilon}\right\rceil,
\qquad K=RL,\qquad
d=\left\lceil\log_2(K+1)\right\rceil.
$$

The clock has one active label and $K$ first-detection labels. The error is the **unhalved diamond norm** of the sample-averaged channel on the data input, with a clean initialized clock and other work registers. An arbitrary entangled reference is allowed. The ideal output returns that work clean. This statement concerns the initialized-input channel; it does not assert a bound on arbitrary uninitialized work states or on each sampled circuit separately.

If $N$ is not a power of two, the unused address states have zero streamed Hamiltonian and are assigned target phase $+1$. They require no extra samples.

## Samples and error allocation

List each forward and reverse controlled phase as a separate index $i$. Its stage is $(r,j)$, with $0\le r<R$ and $0\le j\le J$. Put

$$
\kappa_i=\frac{2\pi^2 4^{-r}}{a_j},
\qquad T=\sum_i\sqrt{\kappa_i},
\qquad
M_i=\left\lceil\frac{2T\sqrt{\kappa_i}}{\epsilon}\right\rceil.
$$

The weighted channel lemma gives local error at most $\kappa_i/M_i$ on the corresponding ideal encoded input. Therefore

$$
\sum_i\frac{\kappa_i}{M_i}\le\frac\epsilon2,
\qquad
M:=\sum_iM_i\le\frac{2T^2}{\epsilon}+2K.
$$

There are two copies of every stage in this list, one in each direction. Both sums in

$$
T=2\sqrt2\pi
\left(\sum_{r=0}^{R-1}2^{-r}\right)
\left(\sum_{j=0}^J a_j^{-1/2}\right)
$$

are geometric. Since $a_J>b/4$, they imply $T=O(b^{-1/2})$ and

$$
M=O\!\left(\frac1{b\epsilon}\right)+O(K).
$$

The full ideal detection circuit leaves undetected amplitude at most $4^{-R}$ on an address with $f(x)=1$. Its middle phase and exact reverse contribute channel error at most

$$
4\cdot4^{-R}\le\frac\epsilon4.
$$

The remaining $\epsilon/4$ is reserved below for digital gate approximation. Thus the three errors add to at most $\epsilon$. The integer ceilings are included in $2K$; no stage is assigned zero samples.

For a sequence of $Q$ oracle invocations, allocating error $\epsilon/Q$ to each fresh invocation gives the valid upper

$$
O\!\left(\frac{Q^2}{b\epsilon}\right)
+O\!\left(Q\log\frac1b\log\frac Q\epsilon\right).
$$

This is an upper bound from composition, without a matching universal claim about its dependence on $Q$ or $\epsilon$.

## What happens to each sample

A sample consists of a classical address $x$ and its deterministic Boolean label $f(x)$. When the label is one, that sample programs the phase

$$
\exp\!\left(\pm\frac{i\pi}{a_jM_i}
|x\rangle\langle x|\otimes|i\rangle\langle i|\right),
$$

where $|i\rangle$ is the current detection-clock label. A zero label programs the identity. The address is compared against the quantum address register, the phase is applied, and the comparison work is uncomputed. The classical record can then be discarded. It is never stored as a frequency table.

Reverse stages use the negative angle and **new independent samples**. They do not reverse the physical source, replay earlier records, or take an inverse of a random sampled circuit. Their channel error is bounded on the canonical ideal reverse path in the analytical proof.

If a coherent outer oracle control is required, it is included in these comparisons and in the detection/central-phase circuit. This constructs the controlled channel directly. Controlling an already compiled realization with an unspecified relative phase would be a different interface.

In particular, the middle predicate is **clock not zero**: apply phase minus one exactly when that predicate and the outer control are both true, then uncompute its workspace. Flipping only clock zero would implement the negative of the desired reflection; after coherent control that would require an extra controlled $Z$. The construction keeps this convention explicitly.

## Clock and comparison circuits

At stage $i$, a two-level Hadamard acts on $\mathrm{span}\lbrace |0\rangle,|i\rangle\rbrace$ of the $d$-qubit clock; all other clock labels are untouched. This can be decomposed along a Gray-code path into $O(d)$ multi-controlled single-qubit operations. A conservative implementation uses $O(d^2)$ elementary gates and $O(d)$ clean work qubits. The inverse follows the same path in reverse.

An address-and-clock equality test has $O(n+d)$ specified bits, including at most one outer-control bit. A Toffoli chain computes their conjunction using $O(n+d)$ Toffoli gates and $O(n+d)$ clean work qubits. After applying the one-qubit phase, reversing the chain restores all those work qubits. Negative controls require only additional single-qubit $X$ gates. These are ordinary gate constructions; the sample is classical control data, not a QRAM address query. See [Barenco et al.](../references/RELATED_WORK.md#gate-implementation).

Consequently, before compiling the continuous one-qubit phases, a safe gate bound is

$$
G_0=O\!\left(M(n+d)+Kd^2\right).
$$

The peak quantum width, including reusable comparison work and an outer control if used, is

$$
O(n+d)
=O\!\left(\log N+\log\log\frac1b+\log\log\frac1\epsilon\right).
$$

Constants and small-parameter floors are implicit in this asymptotic expression. The classical controller separately holds one sample, the public lower bound, stage indices, sample counts and numerical gate parameters. Its sample counter needs $O(\log M)$ bits; this counter is not a free quantum register or a retained dataset.

## Finite precision does not restore a skew penalty

All stage probabilities $a_j$ are exact powers of two. The programmed angle is a rational multiple of $\pi$:

$$
\theta_i=\pm\pi\frac{2^j}{M_i}.
$$

Before numerical approximation, reduce $2^j$ modulo $2M_i$ by integer arithmetic. This gives an equivalent angle in a bounded interval of length $2\pi$. Thus approximating $\pi$ is not multiplied by $2^j$; long evolution times do not demand exponentially many precision bits. Numerators, denominators and counters use $O(J+\log M)$ classical bits.

Choose a known upper bound $G\ge G_0$ on the number of primitive gate locations, and approximate every nonexact one-qubit gate to operator-norm accuracy

$$
\eta=\frac{\epsilon}{8G}.
$$

A telescoping product has operator-norm error at most $G\eta$. The induced channel error is at most $2G\eta\le\epsilon/4$, including entangled references. The comparison/outer-control construction is fixed before this approximation, so its relative-phase convention is preserved. Overall global phases common to the entire controlled circuit are immaterial.

It suffices to compute bounded-angle descriptions with

$$
O\!\left(\log\frac G\epsilon\right)
$$

fractional bits. Standard finite universal gate synthesis adds a factor polynomial in $\log(G/\epsilon)$ to $G_0$ and uses only constant-size gate-synthesis workspace; no optimal $T$-count is asserted here. [Dawson and Nielsen](../references/RELATED_WORK.md#gate-implementation) provide a constructive compilation reference.

The sample allocation also needs no exact-real arithmetic. For a stage $(r,j)$, choose the dyadic rational

$$
\overline w_i=5\,2^{\lceil j/2\rceil-r}.
$$

It satisfies $\sqrt{\kappa_i}\le\overline w_i<2\sqrt{\kappa_i}$. With $\overline T=\sum_i\overline w_i$, use the computable prescription

$$
\overline M_i=
\left\lceil\frac{2\overline T\,\overline w_i}{\epsilon}\right\rceil.
$$

Then $\sum_i\kappa_i/\overline M_i\le\epsilon/2$, while $\sum_i\overline M_i\le2\overline T^2/\epsilon+2K=O(1/(b\epsilon))+O(K)$. All quantities in this prescription are rational once the requested tolerance is represented by a rational lower approximation. Choosing such an approximation within a factor of two only changes constants. The valid public bound $b$ can likewise be rounded downward; it is never inferred from a finite sample stream.

## Charged interface and limits

The sample count, gate count, quantum workspace, controller precision and time spent holding the data input are distinct resources. The source must provide $M$ fresh examples and the data input must remain coherent throughout their processing. Physical source latency and hardware error correction are application-specific costs beyond this logical compiler bound.

The output is the transformed input state and approximately clean work. There is no reusable oracle object after the stream ends. Applying another oracle query consumes another sample block. The construction assumes iid sampling and deterministic labels, and makes no claim for a noisy or correlated source. It also makes no independent classical-task separation or application-level runtime claim.

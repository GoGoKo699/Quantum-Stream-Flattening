# From quantum channels to a flattened stream oracle

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. Its [author page](https://jhwatrous.github.io/books-and-courses.html) identifies the book and provides the author's manuscript; the [publisher record](https://www.cambridge.org/core/books/the-theory-of-quantum-information/AE4AA5638F808D2CFEB070C55431D897) fixes the edition. The sections below use that 2018 book. It supplies the channel and norm foundations, while this project's scientific files supply the streamed algorithm and its proof.

The result to understand is precise: iid classical examples of an arbitrary Boolean function can implement its clean coherent query, during the stream, without evaluating the unknown sampling probabilities. A supplied floor $`p(x)\ge b>0`$ is enough for sample upper $`O(1/(b\epsilon))`$ at unhalved diamond error $`\epsilon`$. This access primitive does not itself prove a downstream learning separation.

## The route through the anchor

| Verified book pointer | Foundation to carry into this project | Where it is used |
| --- | --- | --- |
| Sections 2.1 and 2.1.2 | Registers, density operators and subsystems | Separate the address, initialized clock, retained algorithmic work and inaccessible reference. |
| Sections 2.2.1 and 2.2.2 | CPTP maps and channel representations | Treat discarded sample randomness as a channel; describe an ideal coherent prefix by an isometry. |
| Section 2.3 | Measurements and their outcome probabilities | Distinguish coherent detection from measuring the unknown address. |
| Section 3.1 | Trace-norm state distinguishability | Understand the rare-address lower bound through two distinguishable ideal outputs. |
| Sections 3.3.2 and 3.3.3 | Completely bounded trace norm and channel discrimination | Include entangled references, control-branch coherence and the output clock in one error guarantee. |

These section pointers are to the author-hosted 2018 text. The gate-by-gate stopping clock, its weighted stochastic estimate and its sample allocation are additional project arguments, not statements attributed to the textbook. The [30 milestones](MILESTONES.md) turn this bridge into a sequential reading route.

## Translate the notation before following the proof

| Object | Meaning here | Connection to the anchor |
| --- | --- | --- |
| $`\rho`$ | A data/work input state, possibly correlated with a reference | A density operator of a compound register. |
| $`A^\dagger`$ | The adjoint of an operator | Watrous commonly writes $`A^*`$. |
| $`\Vert A\Vert`$ | Operator norm | Measures the largest amplification of a vector. |
| $`\Vert X\Vert _1`$ | Trace norm | Quantifies state distinguishability. |
| $`\Vert \Phi\Vert _\diamond`$ | Unhalved completely bounded trace norm | The book writes this norm using its triple-bar trace-norm notation. |
| $`W`$ | An ideal address-preserving isometry | $`W^\dagger W=I`$; it coherently appends or evolves initialized work. |
| $`\mathbb E\mathcal A`$ | Average of the sample-dependent channels | Discarded classical randomness is averaged at the channel level. |

In particular,

```math
\mathbb E[V\rho V^\dagger]
\ne (\mathbb EV)\rho(\mathbb EV)^\dagger
```

in general. The left side is the physical randomized operation. The average matrix on the right does not by itself specify that operation.

Appending zero work restricts the domain on which the compiler is promised to work. The channel output still contains that work: cleanup cannot be justified merely by tracing it away. The inaccessible reference is different; it is never touched, and the identity channel acts on it throughout the comparison.

## From a classical record to a coherent phase

Let $`f:[N]\to\lbrace 0,1\rbrace`$ be fixed. The source reveals only fresh pairs $`(X_\ell,f(X_\ell))`$, with $`X_\ell\sim p`$ iid and unknown $`p(x)\ge b`$. A classical record $`x`$ can program a known address-equality gate without measuring the address register on which that gate acts.

For a known clock projector $`C`$, one block of $`M`$ records applies

```math
V=\prod_{\ell=1}^M
\exp\!\left(\frac{it}{M}f(X_\ell)
|X_\ell\rangle\langle X_\ell|\otimes C\right).
```

The mean Hamiltonian is a proof device,

```math
H=\sum_x p(x)f(x)|x\rangle\langle x|,
\qquad U=\exp(itH\otimes C).
```

The compiler never evaluates its diagonal entries. It also does not acquire coherent source access: every source record is classical and processed once. The [model](../science/model.md) fixes this distinction and the complete target channel.

## Why the weighted channel estimate is the decisive step

The book's channel representations and norm inequalities allow the stochastic error to be separated into useful pieces. The extra calculation uses a centered binomial count for each address. It gives mean phase error of order $`t^2p(x)f(x)/M`$ and mean-square phase error of the same order.

Now suppose the ideal prefix has encoded the input through an isometry $`W`$ and only amplitude $`c_x`$ at address $`x`$ reaches the phase-controlled clock label. Write $`\Delta=V-U`$. Expanding the averaged channel difference yields

```math
\mathbb E[\Delta W\rho W^\dagger\Delta^\dagger]
+(\mathbb E\Delta)W\rho(UW)^\dagger
+UW\rho W^\dagger(\mathbb E\Delta)^\dagger.
```

The first term is completely positive, but need not preserve trace. Its norm depends on a second moment and carries $`c_x^2`$. The cross terms contain the centered mean error and carry $`c_x`$. Orthogonal address blocks turn their operator bounds into maxima over addresses. The resulting estimate is

```math
\Vert \mathbb E\mathcal V\circ\mathcal W
-\mathcal U\circ\mathcal W\Vert _\diamond
\le\frac{t^2}{M}(\nu_1+\nu_2)
\le\frac{2t^2}{M}\nu_1,
\qquad
\nu_q=\max_x p(x)f(x)c_x^q.
```

The factor $`f(x)`$ matters: a frequently sampled zero label causes no rotation. The factor $`c_x`$ matters too: a one-labeled address that has mostly stopped should not be charged as though its whole amplitude were still active. Neither factor requires knowing the address's probability in the physical circuit.

The domain of this estimate is the original input, followed by its specified ideal encoding $`W`$. It is not a claim about every dirty clock state. Because the estimate is a diamond bound on that domain, it already includes an arbitrary input reference. See [weighted error](../science/weighted_error.md) for the full operator proof, including retained input workspace.

## Coherent detection supplies the small active amplitudes

A clock label $`0`$ means still active. A nonzero label records the first stopping stage. At stage $`j`$, set $`a_j=2^{-j}`$ and coherently perform a Hadamard test of $`\exp(i\pi H/a_j)`$ on the active branch. No address or stopping time is measured.

For a one-labeled address of frequency $`p`$, the surviving amplitude after the first $`j`$ stages has magnitude

```math
c_j(p)=\prod_{\ell=0}^{j-1}|\cos(2^\ell z)|
=\left|\frac{\sin(2^jz)}{2^j\sin z}\right|
\le\min\lbrace 1,a_j/p\rbrace,
\qquad z=\pi p/2.
```

This follows by repeated sine doubling, with $`\sin(\pi p/2)\ge p`$. It holds for every real probability in $`[b,1]`$; there is no promise that probabilities equal the dyadic stage values.

Taking $`J=\lceil\log_2(2/b)\rceil`$ makes one complete ladder suppress the remaining active amplitude by at least $`1/4`$. Repeated ladders add a factor $`4^{-r}`$ before ladder $`r`$. Multiplication by $`p`$ now gives $`p c_x\le4^{-r}a_j`$, exactly the quantity needed in the weighted channel bound. The [stopping account](../science/coherent_stopping.md) gives the complete clock unitary and the binary first-detection encoding.

## A complete two-address example

Take $`p(1)=3/4`$, $`p(2)=1/4`$, $`f(1)=0`$ and $`f(2)=1`$, with supplied floor $`b=1/4`$. The target sends

```math
\frac{|1\rangle+|2\rangle}{\sqrt2}
\longmapsto
\frac{|1\rangle-|2\rangle}{\sqrt2}.
```

The high-frequency address 1 remains at clock label 0 because its label is zero. For address 2, the first three ideal stage phases are $`\pi/4`$, $`\pi/2`$ and $`\pi`$. Define

```math
u=\frac{1+e^{i\pi/4}}2,\qquad
v=\frac{1-e^{i\pi/4}}2.
```

After those stages its clock state is

```math
|w_2\rangle
=v|1\rangle
+u\frac{1-i}{2}|2\rangle
+u\frac{1+i}{2}|3\rangle.
```

The active label has zero amplitude: the third stage sends its entire residual component to label 3. The state is normalized, and all later stages leave it unchanged. For the ideal detection unitary $`F`$, this gives the entire forward action

```math
F\left(\frac{|1\rangle+|2\rangle}{\sqrt2}|0\rangle\right)
=\frac{|1\rangle|0\rangle+|2\rangle|w_2\rangle}{\sqrt2}.
```

Apply the clock phase $`D=2|0\rangle\langle0|-I`$, then the ideal inverse $`F^\dagger`$. Since $`|w_2\rangle`$ has no active component,

```math
F^\dagger DF\left(\frac{|1\rangle+|2\rangle}{\sqrt2}|0\rangle\right)
=\frac{|1\rangle-|2\rangle}{\sqrt2}|0\rangle.
```

The clock returns clean; it has not been discarded or postselected. This particular ideal example stops exactly. The theorem uses the uniform approximate stopping bound because an unknown general probability need not align with a stage.

For tolerance $`\epsilon=1/8`$, the public prescription uses $`J=3`$, $`L=4`$, $`R=4`$, $`K=16`$ and a five-qubit detection clock. Fresh sample counts and gate precision are then allocated by the theorem; the ideal example does not make those stochastic costs disappear.

The controlled relative phase can be observed directly. Prepare an outer control in $`|+\rangle`$ and fix the address to $`|2\rangle`$. Controlled $`O_f`$ returns $`|-\rangle|2\rangle`$, with clean work. A final Hadamard on the control returns bit 1. Replacing $`O_f`$ by $`-O_f`$ would leave the uncontrolled channel unchanged but return $`|+\rangle|2\rangle`$ here, hence bit 0. Therefore an uncontrolled channel estimate alone cannot certify a controlled query. This construction controls its known streamed gates from the beginning and proves the coherent-control estimate on the initialized input.

## Why fresh inverse blocks can still return the work

The implemented inverse uses fresh records and negative angles. It is not the exact inverse of the random forward realization. Clean return is consequently an error statement about the full channel, not exact sample-by-sample cancellation.

The comparison first replaces the physical forward blocks by ideal ones. At the middle, $`DW`$ is compared with $`WO_f`$, charging the small undetected amplitude once. On that canonical path, inverse prefixes are the corresponding forward-prefix states multiplied by the address-wise sign $`O_f`$. This sign changes no active norm, so the same weighted bound applies to each fresh inverse block. Actual later channels form a contracting suffix in the hybrid. This is why imperfect physical work need not stay exactly on an ideal image for the proof to remain valid. The [return-path proof](../science/sample_bound.md#the-middle-comparison-and-the-return-path) spells out the order of these replacements.

## From the stage bounds to the sample law

Each forward or reverse phase call at stage $`(r,j)`$ has error coefficient

```math
\kappa_{rj}=2\pi^2 4^{-r}/a_j.
```

With $`T=\sum_i\sqrt{\kappa_i}`$ and $`M_i=\lceil2T\sqrt{\kappa_i}/\epsilon\rceil`$, the stochastic errors sum to at most $`\epsilon/2`$, while

```math
M_{\rm tot}\le\frac{2T^2}{\epsilon}+2K,
\qquad
T=O\!\left[
\left(\sum_r2^{-r}\right)
\left(\sum_j2^{j/2}\right)\right]
=O(b^{-1/2}).
```

The resulting order is $`O(1/(b\epsilon))`$. Retaining attenuation across repeated ladders is necessary: paying the first-ladder cost afresh for every ladder would introduce a needless squared logarithm of accuracy. Deterministic stopping, stochastic compilation and digital synthesis receive error budgets $`\epsilon/4`$, $`\epsilon/2`$ and $`\epsilon/4`$. The [sample theorem](../science/sample_bound.md) keeps the integer ceilings and constants; [resources](../science/resources.md) gives a rational computable allocation and charges finite rotations, controls, counters and workspace.

## What this establishes and what remains open

The full-domain rarity cost is unavoidable. If two Boolean functions differ only at an address of probability $`b`$, their records agree until that address appears. The no-hit event has probability $`(1-b)^M`$, whereas suitable ideal oracle outputs are orthogonal. Trace-norm distinguishability therefore gives

```math
M\ge\frac{\log(1/\epsilon)}{-\log(1-b)}.
```

This matches $`1/b`$ dependence at fixed error, including unlimited classical computation and storage. It does not match the $`1/\epsilon`$ upper, and fresh-query composition is not a universal quadratic-query lower bound. See [the lower bound](../science/lower_bound.md).

Each invocation consumes fresh examples while the input remains coherent. It leaves approximately clean work, not a reusable stored oracle. Deterministic labels, iid records, fixed full support and a certified floor are assumptions of the result. Correlated or noisy sources, hardware thresholds and a complete sample–space–query frontier need separate arguments. The [scientific overview](../science/README.md) connects the canonical proofs, and [related work](../references/RELATED_WORK.md) identifies their inherited ingredients.

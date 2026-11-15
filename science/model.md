# Coherent access from an unknown sampling law

An ordinary data stream exposes addresses one at a time. A coherent Boolean query instead has to act on an arbitrary superposition of addresses without revealing which address was present. Uneven sampling makes a direct stream-driven phase accumulate at different rates on different addresses. The question here is whether that unknown rate profile must be learned before coherent access is possible.

The answer is negative for the model below. A public lower bound on address probabilities is sufficient. The construction removes the extra sampling-skew factor in the specified earlier unknown-marginal compiler while retaining small workspace. This is a statement about an access primitive; a downstream learning algorithm still pays its own query, output and implementation costs.

## Input, target and error

Let $`[N]=\lbrace 1,\ldots,N\rbrace`$ and let $`f:[N]\to\lbrace 0,1\rbrace`$ be an arbitrary fixed function. The only unknown-data access consists of fresh classical records

```math
(X_\ell,f(X_\ell)),\qquad X_\ell\overset{\mathrm{iid}}\sim p,
\qquad p(x)\ge b>0.
```

The floor $`b`$ is supplied and satisfies $`Nb\le1`$. The fixed distribution $`p`$ is unknown. No probability-evaluation oracle, proposal-sampling control, coherent state-preparation access, sample replay, function table or QRAM is supplied. Each record is processed once and then discarded. Known gates and fresh initialized work are available, with their sizes and precision charged in [resources](resources.md).

The target is the phase operation

```math
O_f=\sum_{x=1}^N(-1)^{f(x)}|x\rangle\langle x|.
```

The input address register is available while the stream is processed. It can be entangled with any inaccessible reference or retained algorithmic workspace. Work starts in a fixed zero state. Write $`\mathcal I_0`$ for appending that state and $`\mathcal O_{f,0}`$ for applying $`O_f`$ and appending the same zero state. The physical implementation averages over the discarded classical records. Its error requirement is the **unhalved** diamond norm

```math
\Vert \mathbb E[\mathcal A_{\boldsymbol X}]\mathcal I_0
-\mathcal O_{f,0}\Vert _\diamond\le\epsilon,
\qquad 0\lt \epsilon\lt 1.
```

Thus the guarantee includes the entire output work register and every input/reference coherence. It is an initialized-input channel guarantee, not a guarantee on arbitrary dirty clock inputs or on every fixed random record sequence. There is no postselection. After discarding the records, the averaged channel is the physical channel seen by the caller.

One extra external control gives controlled $`O_f`$ under the same convention, including its relative global phase. Hadamards on that control convert it to the bit query $`|x,z\rangle\mapsto|x,z\oplus f(x)\rangle`$. If $`N`$ is not a power of two, unused computational addresses are assigned the known value zero and bypass the update predicates.

## Main result

For every input above, a stream-driven circuit implements the clean controlled oracle with the stated diamond error using

```math
M=O\!\left(\frac1{b\epsilon}\right)
```

fresh classical records. The algorithm needs the floor $`b`$ but no upper probability bound beyond $`p(x)\le1`$. Its coherent detection register has logarithmic size in the number of stopping stages. Including the current record, reversible predicate work, public-parameter descriptions and loop counters gives total working bits and qubits

```math
O\!\left(\log(2N)+\log\frac1b+\log\frac1\epsilon\right).
```

Logical gate and rotation-precision overheads are polynomial in these logarithms. The [sample theorem](sample_bound.md) gives the actual finite allocation and constants; [resources](resources.md) accounts for gate synthesis and source latency. At fixed nontrivial accuracy, the worst-case $`1/b`$ sample dependence matches the [rare-address lower bound](lower_bound.md).

These storage bounds use concise certified descriptions of the public floor and tolerance. A supplied floor and tolerance can each be replaced by a downward dyadic approximation within a factor of two; the theorem then changes only by constant factors. Reading an arbitrarily padded numerical input description is a separate classical input cost.

For a $`Q`$-query circuit, fresh blocks with local accuracy $`\epsilon/Q`$ give the sufficient upper bound $`O(Q^2/(b\epsilon))`$. This is not asserted optimal in $`Q`$ or $`\epsilon`$. The construction is executed during each invocation; it leaves no reusable stored oracle after the stream ends.

## Mechanism and proof route

The inherited stream primitive targets $`\exp(itH_p)`$, where $`H_p=\mathrm{diag}(p(x)f(x))`$. It uses many small address-controlled rotations. A global error estimate depends on the largest address probability. Applying a global threshold at the smallest positive frequency then retains a skew penalty.

The [weighted error lemma](weighted_error.md) instead bounds the simulation only on the actual encoded incoming image. A high-frequency address that has mostly left the active clock label contributes proportionally less error. [Coherent stopping](coherent_stopping.md) constructs a dyadic sequence for which this attenuation is controlled by an exact sine-product identity. Later repeated ladders have geometrically smaller active amplitudes, so [sample allocation](sample_bound.md) keeps their total cost bounded without a squared logarithmic accuracy penalty. A middle phase and a separately justified inverse hybrid return the clock clean within the common error budget.

## Relationship to earlier access models

[Zhao et al., arXiv:2604.07639v2](https://arxiv.org/abs/2604.07639v2), Appendix D.2, supplies quantum oracle sketching and its scalar variance analysis. Appendix D.4.3, Lemma D.18, compiles the same unknown-marginal Boolean oracle by global QSVT thresholding. Its iid specialization has the sample upper bound

```math
O\!\left(\frac{p_{\max}}{p_{\min}^{\,2}}
\frac{\log^2(1/\epsilon)}{\epsilon}\right).
```

The result here replaces that specified upper bound by $`O(1/(b\epsilon))`$ without learning a frequency table. It credits the streamed rotations, scalar moment estimate and fresh-query composition, and adds the incoming-image variance argument with coherent stopping and its error allocation. [Related work](../references/RELATED_WORK.md) distinguishes these ingredients from general filtering and sample-based evolution.

## Scope

The labels are deterministic and the records are iid under a fixed full-support law. A positive floor is essential for a uniform whole-domain query guarantee. Correlated or drifting records, annotation noise, unknown support, optimal precision scaling, physical noise tolerance and a hardware crossover are outside this theorem. No new unconditional downstream quantum–classical learning separation follows merely from this access compiler. [Examples](examples.md) show its concrete effect on sampling-skew dependence.

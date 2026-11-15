# Related work and inherited ingredients

The contribution concerns a specific interface: fresh iid **classical** examples $(x,f(x))$ from a fixed unknown marginal, a supplied lower bound $p(x)\ge b>0$, and a clean Boolean phase-oracle channel acting on an arbitrary quantum input during the stream. No evaluation of $p(x)$, chosen sampling proposal, QRAM, or reusable oracle program is supplied. The analytical result improves the sample upper for that interface; it does not establish a new application-level quantum/classical separation.

## The nearest phase-oracle construction

**H. Zhao, A. Zlokapa, H. Neven, R. Babbush, J. Preskill, J. R. McClean and H.-Y. Huang.** [*Exponential quantum advantage in processing massive classical data*, arXiv:2604.07639v2](https://arxiv.org/abs/2604.07639v2), revised 1 October 2026.

Appendix D develops quantum oracle sketching: streamed samples program small diagonal rotations. Theorem D.12 supplies the scalar-moment/mixing foundation used here. For an unknown nonuniform marginal, Appendix D.4.c, Lemma D.18, Eq. (D124), constructs a clean phase oracle using QSVT with sample upper

$$
O\!\left(\frac{p_{\max}}{p_{\min}^2}
\frac{\log^2(1/\epsilon)}\epsilon\right).
$$

The present compiler retains the streamed rotations and averaged-channel framework. Its additional ingredients are a bound weighted by residual active amplitude, dyadic detection, and the resulting sample allocation. They give $O(1/(b\epsilon))$ samples plus integer stage overhead for the same generic unknown-marginal interface.

The source's Theorem D.14 concerns the weighted evolution $\exp(i t\mathrm{diag}(pf))$ and varies the analogue marginal even when $f\equiv1$. Our target Boolean phase is then independent of that marginal. Its lower bound therefore cannot be transferred as a matching precision or query lower bound here. This distinction concerns the target operation, not a defect in the source theorem.

## Importance weighting requires a different input

**A. Sepúlveda-Jiménez.** [*On the Optimality and Generalization of Quantum Oracle Sketching*](https://zenodo.org/records/19985473), May 2026.

Section 5, Eq. (14), samples from a chosen proposal $q$ and uses the likelihood ratio $p(x)/q(x)$ in each rotation. Its expected generator retains the weighted diagonal $\mathrm{diag}(pf)$. The passive stream here cannot choose $q$ or evaluate that ratio, and its target removes the marginal from the Boolean phase. We use this construction only to identify those access and target differences; its other claims are not needed by our proof.

If $p(x)$ were evaluable, direct inverse-probability compensation would already provide the familiar inverse-$p_{\min}$ variance scale. The present contribution is attaining that scale from passive samples without that evaluation interface.

## Coherent stopping and spectral filtering

**A. Ambainis.** [*Variable time amplitude amplification and quantum algorithms for linear algebra problems*](https://doi.org/10.4230/LIPIcs.STACS.2012.636), STACS 2012; [arXiv:1010.4458](https://arxiv.org/abs/1010.4458).

Coherent early stopping at different times is an established quantum algorithmic technique. Its use to improve condition-number dependence is a direct conceptual predecessor of removing stopped branches from later work. That theorem concerns amplification and query runtime; it does not itself give the passive-sample, residual-amplitude channel bound proved here. This compiler uses no amplitude amplification.

**L. Lin and Y. Tong.** [*Optimal polynomial based quantum eigenstate filtering with application to solving quantum linear systems*](https://quantum-journal.org/papers/q-2020-11-11-361/), Quantum **4**, 361 (2020).

Polynomial/QSP eigenstate filtering is an established way to separate spectral regions under operator access and a gap promise. Our zero-versus-positive spectral objective inherits this filtering perspective. The resource question differs: an operator query must itself be constructed from a passive classical stream, and its error cost changes with the remaining active amplitude.

## Sample-based simulation and samplization

**S. Kimmel, C. Y.-Y. Lin, G. H. Low, M. Ozols and T. J. Yoder.** [*Hamiltonian simulation with optimal sample complexity*](https://www.nature.com/articles/s41534-017-0013-7), npj Quantum Information **3**, 13 (2017).

This work studies Hamiltonian evolution supplied through copies of a quantum state and extends sample-based simulation to Hermitian polynomials. It supplies context for treating samples as a consumed programming resource. Its target evolution and quantum-copy input differ from a Boolean phase compiled from classical address samples.

**Q. Wang and Z. Zhang.** [*Time-Efficient Quantum Entropy Estimator via Samplizer*](https://doi.org/10.4230/LIPIcs.ESA.2024.101), ESA 2024.

Their samplizer converts a $Q$-query block-encoding algorithm into a diamond-close quantum sample algorithm using $\widetilde\Theta(Q^2/\delta)$ copies of a mixed state. This establishes a general query-to-sample framework. It does not directly yield the present inverse-$b$ dependence: the access model is quantum copies, and the generic conversion does not exploit the diagonal classical stream's weighted active amplitudes.

**B. Coyle et al.** [*Problem-aware sampling for bias and variance reduction in randomised Hamiltonian simulation*, arXiv:2610.31515](https://arxiv.org/abs/2610.31515), October 2026.

StateDRIFT adapts a chosen term-sampling distribution using the initial state and target observable. The present source distribution is fixed and unavailable for evaluation, while the guarantee covers every initialized data input and reference. Consequently, observable-specific variance optimization is useful context but does not provide this full-channel compiler.

## Gate implementation

**A. Barenco et al.** [*Elementary gates for quantum computation*](https://doi.org/10.1103/PhysRevA.52.3457), Physical Review A **52**, 3457 (1995); [arXiv:quant-ph/9503016](https://arxiv.org/abs/quant-ph/9503016).

Standard controlled-gate decompositions implement equality controls and two-level clock operations. The clean comparison work and its uncomputation are included in the [resource account](../science/resources.md).

**C. M. Dawson and M. A. Nielsen.** [*The Solovay–Kitaev algorithm*](https://arxiv.org/abs/quant-ph/0505030), Quantum Information & Computation **6**, 81–95 (2006).

A constructive finite-gate compilation result suffices for the conservative polylogarithmic synthesis overhead stated here. No optimal Clifford+$T$ synthesis count is required for the sample theorem.

## What is claimed beyond these ingredients

Streamed diagonal simulation, variance-sensitive error analysis, coherent stopping, spectral filtering and finite-gate compilation are inherited tools. The additional operational statement is a clean unknown-marginal Boolean oracle with sample upper $O(1/(b\epsilon))$, using the residual-amplitude channel estimate and dyadic allocation without a probability-evaluation oracle. The supplied lower bound matches inverse-$b$ dependence at fixed error. Dependence on precision, repeated queries, non-iid data and imperfect labels remains qualified in the scientific account.

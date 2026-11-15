# Thirty milestones for Quantum Stream Flattening

The story starts with a classical stream that reveals one labeled address at a time and ends with a coherent Boolean query that acts on an arbitrary input during that stream. The central distinction is between learning the unknown sampling frequencies and compensating for them coherently without a frequency table.

The map allocates **M01–M10 to background/preliminaries** and **M11–M30 to narrative/innovation**. Ten background milestones build the reference-aware channel framework and the statistical meaning of streamed phase rotations. Twenty narrative milestones then connect the weighted error estimate, stopping clock, clean return and sample allocation to the complete theorem. Each phase moves from individual objects to an integrated task or contribution. Specialist calculations remain in their authoritative scientific files.

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The author-hosted [book page](https://jhwatrous.github.io/books-and-courses.html) provides [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf) and [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf). The relevant foundations are §2.1.2, “Quantum states of registers”; §§2.2.1–2.2.2, channel definitions and representations; §2.3.1, measurement definitions; §3.1, state discrimination; §3.3.2, “The completely bounded trace norm”; and §3.3.3, “Distances between channels.” The [Watrous bridge](WATROUS_BRIDGE.md) translates those foundations into the project's notation. The book's completely bounded trace norm is the diamond norm used here. The streamed statistical calculation and coherent stopping argument are supplied by this project's scientific account, rather than attributed to the textbook.

Primary research citations in [related work](../references/RELATED_WORK.md) identify inherited ingredients and comparisons. They are research dependencies, not additional educational anchors.

## Phase I — Background and preliminaries

### M01 — Separate addresses, labels and sampling frequencies

- **Central question:** What information does one classical record reveal, and what remains unknown?
- **Understanding target:** Distinguish the address $x$, its deterministic label $f(x)$, the unknown probability $p(x)$ and the supplied floor $b$. Explain why observing a record does not provide an oracle for evaluating $p$ or choosing a different sampling law.
- **Dependencies and story role:** No earlier milestone is needed. This fixes the local data objects before any quantum operation is introduced.
- **Conceptual connection:** A classical record can serve as known control data while the distribution generating records remains unknown.
- **Source pointers:** [Input, target and error](../science/model.md#input-target-and-error); Watrous §2.1.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)) for the register language.

### M02 — Read a phase oracle as an operation on coherence

- **Central question:** What does a Boolean phase query do to a superposition?
- **Understanding target:** Explain $O_f|x\rangle=(-1)^{f(x)}|x\rangle$ and how relative signs alter interference even though computational-basis probabilities remain unchanged. Distinguish applying this operation from outputting a classical function table.
- **Dependencies and story role:** Uses M01. It adds the local quantum target to the classical input description.
- **Conceptual connection:** The label controls a relative phase on the data register; the caller's input amplitudes are not the sampling probabilities $p(x)$.
- **Source pointers:** [Input, target and error](../science/model.md#input-target-and-error); Watrous §§2.1.2 and 2.3.1 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)).

### M03 — Keep the input, work and reference distinct

- **Central question:** Which quantum systems must the compiler preserve or return?
- **Understanding target:** Identify the address register, retained algorithmic workspace, initialized clock and an inaccessible entangled reference. Explain an isometry that appends work without measuring the address.
- **Dependencies and story role:** Uses M02. The single-register target becomes a joint-system task with explicit input and output obligations.
- **Conceptual connection:** An operation can preserve basis-state behavior while damaging coherence with a reference; returning work is therefore part of the target channel.
- **Source pointers:** [Weighted input-image bound](../science/weighted_error.md#weighted-input-image-bound); Watrous §§2.1.2 and 2.2.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)).

### M04 — Turn discarded classical randomness into a physical channel

- **Central question:** What operation remains after the individual stream records are discarded?
- **Understanding target:** Explain why averaging sample-dependent unitary channels gives a completely positive trace-preserving channel. Distinguish this averaged physical channel from a guarantee for every fixed record sequence.
- **Dependencies and story role:** Uses M01 and M03. It connects the classical source to the joint quantum input/output description.
- **Conceptual connection:** Classical control followed by discarding its record is a channel representation, not postselection on a favorable stream.
- **Source pointers:** [Why these averaged channels compose](../science/weighted_error.md#why-these-averaged-channels-compose); [Input, target and error](../science/model.md#input-target-and-error); Watrous §§2.2.1–2.2.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)).

### M05 — Give trace distance an operational meaning

- **Central question:** How does a norm difference between output states limit distinguishability?
- **Understanding target:** Relate trace norm to changes in measurement statistics and state discrimination. Keep the unhalved norm convention separate from the conventional factor-one-half trace distance.
- **Dependencies and story role:** Uses M03–M04. It introduces an observable meaning for output error before comparing whole channels.
- **Conceptual connection:** The final task is judged by all possible measurements on the output, not by a selected expectation value.
- **Source pointers:** [The rare-address cost](../science/lower_bound.md#two-indistinguishable-streams-until-one-address-appears); Watrous §3.1 ([Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M06 — Formulate the initialized-input diamond guarantee

- **Central question:** How is a channel compared uniformly over quantum inputs and references?
- **Understanding target:** Explain the completely bounded trace norm and why its reference system matters. Distinguish the channel obtained after appending zero work from a stronger, unclaimed guarantee on arbitrary initial clock states.
- **Dependencies and story role:** Uses M03–M05. This integrates local state error into the framework required by a coherent subroutine.
- **Conceptual connection:** The compiler must approximate the transformed input and the returned work together, including their correlations with every reference.
- **Source pointers:** [Input, target and error](../science/model.md#input-target-and-error); [Weighted input-image bound](../science/weighted_error.md#weighted-input-image-bound); Watrous §§3.3.2–3.3.3 ([Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M07 — Retain the relative phase of a controlled query

- **Central question:** Why does a controlled phase oracle require more care than an ordinary phase channel?
- **Understanding target:** Explain how a global phase on one control branch becomes a relative phase of the joint input. Derive the bit-query relation by conjugating a controlled phase with Hadamards on its control.
- **Dependencies and story role:** Uses M02, M03 and M06. It fixes which coherent query interface the final theorem must supply.
- **Conceptual connection:** Controlling the specified circuit directly preserves a phase convention that would be lost by specifying only an uncontrolled channel up to global phase.
- **Source pointers:** [Coherent control and a bit query](../science/coherent_stopping.md#coherent-control-and-a-bit-query); Watrous §§2.1.2 and 2.2.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)).

### M08 — Connect empirical counts to weak diagonal rotations

- **Central question:** Why does a stream-driven phase accumulate at an address-dependent rate?
- **Understanding target:** Explain the binomial count $n_x$, its mean and variance, and the empirical phase produced by many small rotations. Identify the analysis operator $H=\mathrm{diag}(pf)$ without treating it as a supplied oracle.
- **Dependencies and story role:** Uses M01, M02 and M04. It supplies the statistical ingredient that will later determine sample cost.
- **Conceptual connection:** Classical randomness appears as uncertainty in a coherent phase; its mean rate depends on the unknown marginal.
- **Source pointers:** [A sampled controlled phase](../science/weighted_error.md#a-sampled-controlled-phase); Watrous §2.2.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)) for channels represented by randomized operations. The binomial calculation is supplied locally.

### M09 — Compose consumed-sample subroutines

- **Central question:** When can local averaged-channel errors be added through a quantum algorithm?
- **Understanding target:** Explain a channel hybrid with an ideal prefix and a physical suffix. Identify the role of fresh independent sample blocks and why subsequent channels cannot increase the error bound.
- **Dependencies and story role:** Uses M04–M06 and M08. It connects a single streamed rotation to a larger circuit.
- **Conceptual connection:** A proof may bound a gate only on the ideal incoming image, provided the hybrid uses that image and does not assume that noisy work remains there exactly.
- **Source pointers:** [Why these averaged channels compose](../science/weighted_error.md#why-these-averaged-channels-compose); Watrous §§2.2.1–2.2.2 and 3.3.2–3.3.3 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M10 — Assemble the full access problem

- **Central question:** What exactly must be achieved, from source records to a composable coherent query?
- **Understanding target:** State the fixed-IID, deterministic-label, full-support model; the public floor; the initialized-channel error; and the charged sample, gate, workspace and precision resources. Explain why the operation is executed during each invocation rather than stored as a reusable oracle after the stream ends.
- **Dependencies and story role:** Integrates M01–M09 and closes the background phase with the complete problem rather than another isolated prerequisite.
- **Conceptual connection:** Uniform coherent access can be a useful learning primitive without itself establishing an application-level quantum–classical separation.
- **Source pointers:** [Input model and main result](../science/model.md); [Charged interface and limits](../science/resources.md#charged-interface-and-limits); Watrous §§2.2 and 3.3 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

## Phase II — Narrative and innovation

### M11 — Extract the centered phase moments

- **Central question:** Which part of random phase error survives averaging?
- **Understanding target:** Use centering to cancel the linear term and obtain the mean-deviation and mean-square bounds from binomial variance. Explain why the argument does not require a small-angle assumption on each sampled gate.
- **Dependencies and story role:** Uses M08. This begins the proof locally, with the inherited scalar calculation that the new estimate will refine.
- **Conceptual connection:** Variance controls the averaged phase error even though the individual random unitary need not be close to its target.
- **Source pointers:** [A sampled controlled phase](../science/weighted_error.md#a-sampled-controlled-phase); research dependency: [Zhao et al., Theorem D.12](../references/RELATED_WORK.md#the-nearest-phase-oracle-construction). Watrous §2.2.2 supplies the channel-representation framework.

### M12 — Weight channel error by remaining active amplitude

- **Central question:** How can a small active branch reduce the cost of a sampled phase?
- **Understanding target:** Reconstruct the decomposition into a completely positive remainder and two cross maps. Explain why their bounds involve $p(x)f(x)c_x^2$ and $p(x)f(x)c_x$, respectively, and why the maximum is over address blocks rather than a sum over addresses.
- **Dependencies and story role:** Uses M03, M06 and M11. It establishes the central new local estimate before choosing a stopping circuit.
- **Conceptual connection:** The relevant error depends on the incoming encoded image. A zero-labeled branch contributes no phase error, and a mostly stopped one-labeled branch contributes little even if its frequency is large.
- **Source pointers:** [Weighted input-image bound](../science/weighted_error.md#weighted-input-image-bound); Watrous §§2.2.2 and 3.3.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M13 — Build one coherent detection stage

- **Central question:** What does a Hadamard test do to the still-active amplitude at one address?
- **Understanding target:** Derive the two-component output of one stage and its cosine factor. Explain why label zero remains undetected and why early detection of any label-one address is harmless.
- **Dependencies and story role:** Uses M02, M07 and M08. It supplies the local operation that can create the weighted images required by M12.
- **Conceptual connection:** Detection is stored coherently in work; no measurement of the unknown quantum address is performed.
- **Source pointers:** [One stage is a two-level Hadamard test](../science/coherent_stopping.md#one-stage-is-a-two-level-hadamard-test); Watrous §§2.1.2 and 2.2.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)).

### M14 — Compress the first-detection record into a clock

- **Central question:** Why can many potential stopping events fit into a logarithmic-size register?
- **Understanding target:** Explain the basis labels “active” and “first detected at stage $i$,” and the two-level Hadamard acting only on labels $0,i$. Show why earlier stopped labels bypass later stages and why the construction is a full unitary that can be reversed.
- **Dependencies and story role:** Uses M03 and M13. The single local detector becomes an implementable sequence without a growing collection of independent flag registers.
- **Conceptual connection:** The compiler stores a coherent detection time, not an address-to-frequency table or a transcript of the stream.
- **Source pointers:** [Clock definition and stage unitary](../science/coherent_stopping.md); [Clock and comparison circuits](../science/resources.md#clock-and-comparison-circuits); Watrous §2.2.2 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf)).

### M15 — Derive a dyadic envelope for arbitrary frequencies

- **Central question:** How can fixed scales control a frequency that is neither known nor on a discrete grid?
- **Understanding target:** Derive the sine-product identity for dyadic cosine factors and use $\sin(\pi p/2)\ge p$ to obtain $c_j(p)\le\min\lbrace 1,a_j/p\rbrace$. Explain why no exact-level or calibrated $p_{\max}$ promise is needed.
- **Dependencies and story role:** Uses M13–M14. The detector sequence now yields a quantitative image bound for every allowed marginal.
- **Conceptual connection:** Unknown frequency controls where amplitude stops, while the same public ladder controls the worst-case residual at every scale.
- **Source pointers:** [The dyadic envelope holds for every frequency](../science/coherent_stopping.md#the-dyadic-envelope-holds-for-every-frequency). The trigonometric derivation is supplied locally; Watrous's channel framework remains the educational foundation.

### M16 — Suppress the undetected component across ladders

- **Central question:** Why repeat a ladder after it already reaches the supplied frequency floor?
- **Understanding target:** Explain why one completed ladder leaves at most one-quarter active amplitude on each label-one address and why $r$ completed ladders supply the additional factor $4^{-r}$. Keep amplitude attenuation distinct from probability attenuation.
- **Dependencies and story role:** Uses M15. It turns the within-ladder estimate into the accuracy mechanism for the whole circuit.
- **Conceptual connection:** Later ladders act on less amplitude and can therefore be compiled with fewer samples; repetition need not multiply the leading cost by the number of ladders.
- **Source pointers:** [The dyadic envelope](../science/coherent_stopping.md#the-dyadic-envelope-holds-for-every-frequency); [Local sampling cost](../science/sample_bound.md#local-sampling-cost-on-each-ideal-image).

### M17 — Convert detection into a clean Boolean phase

- **Central question:** How does a phase on detected clock labels become a phase on the data input?
- **Understanding target:** Explain the central reflection that is $+1$ on the active label and $-1$ on detected labels. Derive its isometry error from the residual active amplitude, then explain ideal uncomputation and the bound on the entire returned clock.
- **Dependencies and story role:** Uses M06, M14 and M16. It connects the stopped branches to the desired query rather than treating detection as the final output.
- **Conceptual connection:** Clean return is proved before tracing out work, so reference coherence and the caller's later computation remain covered.
- **Source pointers:** [Applying the phase and returning the clock](../science/coherent_stopping.md#applying-the-phase-and-returning-the-clock); Watrous §§3.3.2–3.3.3 ([Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M18 — Justify the inverse half with a canonical comparison

- **Central question:** Why does a noisy forward circuit not invalidate the return-path error estimate?
- **Understanding target:** Explain the middle replacement $DW\mapsto WO_f$, charge its error once, and identify each canonical inverse prefix. Distinguish a fresh-sample implementation of an inverse ideal phase from replaying or reversing the earlier random sample sequence.
- **Dependencies and story role:** Uses M09 and M17. It resolves the point where a local image bound could otherwise be applied outside its valid domain.
- **Conceptual connection:** The proof follows ideal comparison images inside a channel hybrid; it does not require the physical noisy state to remain exactly on those images.
- **Source pointers:** [The middle comparison and the return path](../science/sample_bound.md#the-middle-comparison-and-the-return-path); Watrous §§2.2.2 and 3.3.2–3.3.3 ([Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M19 — Price each forward and reverse streamed phase

- **Central question:** What does the active-amplitude envelope imply for a stage's sample coefficient?
- **Understanding target:** Combine $t_j=\pi/a_j$, the weighted image bound and the factor $4^{-r}$ to obtain local error at most $\kappa_{rj}/M$, with $\kappa_{rj}=2\pi^2 4^{-r}/a_j$. Explain why the same coefficient is valid in the inverse half.
- **Dependencies and story role:** Uses M12, M15–M16 and M18. It joins the new analytical estimate to the actual circuit.
- **Conceptual connection:** High-frequency addresses no longer impose the unrestricted $p_{\max}$ cost at every late stage because their relevant amplitudes have been attenuated.
- **Source pointers:** [Local sampling cost on each ideal image](../science/sample_bound.md#local-sampling-cost-on-each-ideal-image); [Weighted input-image bound](../science/weighted_error.md#weighted-input-image-bound).

### M20 — Allocate a finite integer sample budget

- **Central question:** How should a common error allowance be shared among unequal stage costs?
- **Understanding target:** Explain the square-root allocation through $T=\sum_i\sqrt{\kappa_i}$ and positive integer counts $M_i=\lceil2T\sqrt{\kappa_i}/\epsilon\rceil$. Derive the stochastic error sum and retain the ceiling contribution to total samples.
- **Dependencies and story role:** Uses M09 and M19. Local coefficients become one valid finite circuit budget.
- **Conceptual connection:** Allocation is based on known stage parameters, not on estimating the hidden frequencies from the stream.
- **Source pointers:** [Allocating integer sample counts](../science/sample_bound.md#allocating-integer-sample-counts); [Finite precision](../science/resources.md#finite-precision-does-not-restore-a-skew-penalty) for computable conservative allocations.

### M21 — Sum the geometric costs without losing the accuracy gain

- **Central question:** Why does the complete sample cost scale as $1/(b\epsilon)$?
- **Understanding target:** Evaluate the geometric sums over scale and repetition, bound $T=O(b^{-1/2})$ and obtain the explicit sample upper including stage ceilings. Explain how discarding attenuation across ladders would create an unnecessary squared logarithm in accuracy.
- **Dependencies and story role:** Uses M16 and M20. This is the global sample conclusion assembled from the local mechanism.
- **Conceptual connection:** Coherent stopping changes the cost of simulating later operations, not merely their execution order.
- **Source pointers:** [Allocating integer sample counts](../science/sample_bound.md#allocating-integer-sample-counts); [Samples and error allocation](../science/resources.md#samples-and-error-allocation).

### M22 — Close the full channel-error budget

- **Central question:** Which distinct errors must fit inside the requested tolerance?
- **Understanding target:** Combine deterministic stopping error, stochastic phase error and digital gate approximation under the stated unhalved diamond convention. Explain why the guarantee concerns the sample-averaged initialized channel and its complete output work.
- **Dependencies and story role:** Uses M06, M17–M18 and M20–M21. It integrates the proof components into the promised operation.
- **Conceptual connection:** A sample-count estimate alone is insufficient unless approximation and return obligations are included in the same channel comparison.
- **Source pointers:** [Final initialized-channel guarantee](../science/sample_bound.md#final-initialized-channel-guarantee); Watrous §§3.3.2–3.3.3 ([Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M23 — Lift the proof to controlled and bit queries

- **Central question:** Does the sample theorem preserve coherence between the query's on and off branches?
- **Understanding target:** Use the operator-valued block isometry from M12 to explain coherent outer control, its unchanged local bound and its clean clock return. Verify that the all-one Boolean function still produces the required relative control phase, and then recover the bit query.
- **Dependencies and story role:** Uses M07, M12 and M22. It completes the operational query interface rather than relying on an uncontrolled channel's phase convention.
- **Conceptual connection:** The same weighted argument covers an arbitrary retained control system, so a controlled query is constructed directly from the circuit.
- **Source pointers:** [Coherent control and a bit query](../science/coherent_stopping.md#coherent-control-and-a-bit-query); [Final initialized-channel guarantee](../science/sample_bound.md#final-initialized-channel-guarantee); [Complete initialized channels](../verification/README.md#complete-initialized-channels).

### M24 — Implement each record's controls with charged workspace

- **Central question:** What gates and temporary registers turn a classical record into its streamed update?
- **Understanding target:** Explain address/clock equality predicates, a controlled one-qubit phase and uncomputation of comparison work. Relate the compact detection clock to peak quantum width and distinguish width from the number of processed records.
- **Dependencies and story role:** Uses M14 and M23. It connects the channel construction to an ordinary circuit implementation.
- **Conceptual connection:** The current record specifies a small reversible control circuit; it does not grant coherent access to an entire retained classical dataset.
- **Source pointers:** [What happens to each sample](../science/resources.md#what-happens-to-each-sample); [Clock and comparison circuits](../science/resources.md#clock-and-comparison-circuits); gate-decomposition research dependencies in [related work](../references/RELATED_WORK.md#gate-implementation).

### M25 — Charge controller precision and input-holding time

- **Central question:** Can long phase times or public numerical parameters hide a large implementation cost?
- **Understanding target:** Explain modular reduction of rational multiples of $\pi$, conservative rational sample allocations and the finite gate-synthesis budget. Count the current record, stage/sample counters and public-parameter descriptions; identify the physical time for which the input must remain coherent.
- **Dependencies and story role:** Uses M20, M22 and M24. This completes the resource account beyond logical quantum width.
- **Conceptual connection:** Logical polylogarithmic overhead does not by itself establish a hardware crossover, negligible source latency or a noise-tolerant physical device.
- **Source pointers:** [Finite precision does not restore a skew penalty](../science/resources.md#finite-precision-does-not-restore-a-skew-penalty); [Charged interface and limits](../science/resources.md#charged-interface-and-limits).

### M26 — Interpret the heavy-tail examples faithfully

- **Central question:** What concrete improvement does removing the skew factor make possible?
- **Understanding target:** Analyze the normalized dyadic heavy tail, its support size and minimum probability, and compare $1/b$ with the earlier $p_{\max}/b^2$ coefficient. Explain the seven-address clock example without treating coefficient tables as numerical sample budgets or classical speedup evidence.
- **Dependencies and story role:** Uses M21 and M24–M25. It translates the theorem into a complete illustrative family after its costs are known.
- **Conceptual connection:** The example measures a difference between compiler upper bounds for the same passive unknown marginal; it supplies neither an earlier-method lower bound nor an application-level separation.
- **Source pointers:** [Examples of marginal skew](../science/examples.md); [Nearest phase-oracle construction](../references/RELATED_WORK.md#the-nearest-phase-oracle-construction).

### M27 — Match the rarity dependence and retain the precision gap

- **Central question:** What must every compiler learn before it can answer on a rarely observed address?
- **Understanding target:** Use the no-hit event to compare two functions differing at one address and derive the lower bound on sample count. Explain the fixed-error $1/b$ match, the remaining $1/\epsilon$ versus logarithmic precision gap, and the special role of coherent control when a phase would otherwise be global.
- **Dependencies and story role:** Uses M05–M07, M21 and M23. It places the achieved upper bound against an operational obstruction.
- **Conceptual connection:** A lower bound must change the Boolean target itself; changing only the probability-weighted evolution does not provide the needed converse.
- **Source pointers:** [Rare-address lower bound and remaining gap](../science/lower_bound.md); Watrous §§3.1 and 3.3.3 ([Chapter 3](https://jhwatrous.github.io/TQI.3.pdf)).

### M28 — Compose later queries without inventing a stored oracle

- **Central question:** What changes when a learning algorithm needs several coherent invocations?
- **Understanding target:** Allocate error $\epsilon/Q$ to each fresh invocation and derive the sufficient $Q^2/(b\epsilon)$ sample upper with its stage overhead. Distinguish that achievable bound from an optimal query law and from an unrestricted-memory function cache.
- **Dependencies and story role:** Uses M09, M21–M23 and M27. The single clean invocation becomes a usable algorithmic subroutine with its repeated costs visible.
- **Conceptual connection:** Returning quantum work clean permits composition, while the consumed classical sample resource must still be replenished for every invocation.
- **Source pointers:** [Several queries use several fresh source blocks](../science/sample_bound.md#several-queries-use-several-fresh-source-blocks); [What is not matched](../science/lower_bound.md#what-is-not-matched).

### M29 — Separate inherited tools from the additional capability

- **Central question:** What remains after the closest prior construction and other access models are credited?
- **Understanding target:** Identify the inherited streamed diagonal rotations, scalar moments, coherent stopping perspective and finite-gate tools. Explain the additional residual-amplitude channel estimate and allocation, and distinguish passive unknown-marginal access from known-probability importance weighting or chosen-proposal sampling.
- **Dependencies and story role:** Uses M10–M12, M15 and M21–M28. It integrates the scientific comparison around the actual task rather than around terminology.
- **Conceptual connection:** A shared filtering or simulation ingredient does not by itself settle the sample cost of the present input interface; conversely, an access difference must have a consequential demonstrated effect.
- **Source pointers:** [Related work and inherited ingredients](../references/RELATED_WORK.md); [Relation to the earlier compiler](../science/sample_bound.md#relation-to-the-earlier-unknown-marginal-compiler). Watrous remains the sole educational anchor; these are primary research comparisons.

### M30 — State the complete contribution with its boundaries

- **Central question:** What can the compiler now accomplish, under which assumptions and at which complete logical cost?
- **Understanding target:** Give one connected account from fresh fixed-IID deterministic records and a public positive floor to a clean reference-aware controlled Boolean query, its $1/b$ sample upper and charged small workspace. Keep the supplied floor, initialized-input convention, fresh-query costs, finite precision, fixed-error lower match and unresolved precision/query gaps together. Explain why correlated sources, label noise, unknown support, reusable stored oracles and downstream classical-task separations require separate claims.
- **Dependencies and story role:** Integrates M01–M29 and closes the narrative phase with the complete scientific proposition rather than an additional extension.
- **Conceptual connection:** The global result follows because a coherent stopping structure changes how local sample fluctuations act on the incoming image, and the implementation and comparison preserve that same operational meaning.
- **Source pointers:** [Input model and main result](../science/model.md), [sample theorem](../science/sample_bound.md), [resources](../science/resources.md), [lower bound](../science/lower_bound.md), [related work](../references/RELATED_WORK.md) and [verification scope](../verification/README.md).

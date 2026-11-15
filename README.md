# Quantum Stream Flattening

**Can an uneven classical data stream supply coherent quantum access without learning its sampling frequencies?** A weighted error estimate and a coherent stopping circuit give an affirmative answer for iid Boolean data.

The stream supplies ordinary records $(x,f(x))$ with an unknown fixed marginal $p(x)\ge b>0$. The compiler acts on an arbitrary quantum input already present during the stream. For unhalved diamond error $0<\epsilon<1$, its sample upper bound is

```math
M=O\!\left(\frac1{b\epsilon}\right).
```

The guarantee includes coherent control, arbitrary entangled references and return of initialized work within the same error. Only a certified positive probability floor is needed. The address-frequency assignment is never learned or stored, and each classical record is processed once. Every later oracle invocation consumes fresh samples.

[Quantum oracle sketching](references/RELATED_WORK.md) supplies the streamed phase rotations and scalar variance argument. The contribution here is the incoming-image error bound and dyadic stopping/allocation that remove the extra sampling-skew factor from the specified earlier unknown-marginal upper bound. At fixed accuracy, the inverse-$b$ sample dependence matches a rare-address lower bound. The dependence on accuracy and on the number of oracle calls is not claimed optimal.

## Read the science

Start with the [model and main result](science/model.md), then follow the circuit through [weighted channel error](science/weighted_error.md), [coherent stopping](science/coherent_stopping.md) and [sample allocation with clean return](science/sample_bound.md).

| Question | Account |
|---|---|
| What data access and error guarantee are supplied? | [Model](science/model.md) |
| Why do frequent addresses stop dominating the error? | [Weighted error](science/weighted_error.md) |
| How does the circuit detect unknown frequencies coherently? | [Stopping circuit](science/coherent_stopping.md) |
| How are forward and return errors budgeted? | [Sample theorem](science/sample_bound.md) |
| What do memory, gates and digital precision cost? | [Resources](science/resources.md) |
| Which sample dependence is necessary? | [Lower bound and open precision gap](science/lower_bound.md) |
| How large is the improvement on uneven streams? | [Examples](science/examples.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) |
| What has been checked computationally? | [Verification](verification/README.md) |

[The scientific index](science/README.md) connects these pages. [The LLM reading guide](llms.txt) gives the same authoritative routes by task.

## Learn the result

The educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [source-to-project bridge](learning/WATROUS_BRIDGE.md) selects the relevant channel and distance foundations, translates notation, and supplies the steps specific to this compiler. The [30-milestone map](learning/MILESTONES.md) builds from the data-access model to the complete theorem and its limits.

## Reproduce the finite checks

```bash
python3 verification/run_all.py
```

The complete-channel checks use NumPy and exact iid characteristic functions evaluated in floating point. They cover all input matrix units for small controlled-oracle examples, including non-dyadic frequencies, clock padding, the all-one relative phase and an uneven marginal. They do not substitute for the analytical diamond-norm proof or establish an interval-certified diamond optimum.

## Scope and physical costs

The theorem assumes deterministic labels, iid records and a known positive floor. The physical guarantee averages discarded record randomness. Each invocation keeps its input coherent while all samples and gates are processed; source latency and hardware error correction are additional physical costs. The [resource account](science/resources.md) charges logical controls, initialized work, counters and rotation precision. A stored reusable oracle, correlated/drifting streams, noisy labels, an independently new downstream quantum–classical separation and a hardware crossover are outside the result.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

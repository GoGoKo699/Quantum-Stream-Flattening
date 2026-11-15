# Quantum Stream Flattening

Can passive classical examples supply coherent Boolean access when their sampling frequencies are unknown?

For an iid stream `(x, f(x))` with deterministic binary labels and a known positive floor `p(x) >= b`, a coherent stopping construction implements the Boolean phase oracle using `O(1/(b epsilon))` fresh samples. The guarantee is an averaged physical-channel bound on arbitrary inputs and references, including approximate return of initialized work. Every invocation consumes fresh samples.

The scientific account develops the model, weighted channel-error estimate, dyadic stopping, sample allocation, and charged implementation costs. It builds on quantum oracle sketching by Zhao et al., [arXiv:2604.07639v2](https://arxiv.org/abs/2604.07639v2).

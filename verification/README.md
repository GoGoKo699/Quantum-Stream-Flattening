# Finite verification

Run from the repository root:

```bash
python3 verification/run_all.py
```

The suite requires Python 3 and NumPy. It reproduces the diagnostics in [averaged_channel_results.json](averaged_channel_results.json) using [verify_averaged_channel.py](verify_averaged_channel.py).

## Complete initialized channels

For each small example, the program propagates every input matrix unit through the complete controlled oracle. Every stochastic phase block is evaluated by the exact iid characteristic-function formula in floating point; the forward and return blocks use independent samples. The binary clock includes unused padded labels. The resulting full Choi matrix is checked for trace preservation, Hermiticity, positivity to numerical tolerance, clean target error and zero population of padded labels.

The examples include non-dyadic probabilities, an all-zero function, an all-one function and a 31:1 sampling imbalance. The all-one function is essential: an ordinary phase channel cannot observe a global minus sign, while the controlled oracle must retain it.

For the Hermiticity-preserving channel difference with Choi matrix $J_\Delta$ and input dimension $d_{\rm in}$, the program uses the bounds

```math
\frac{\|J_\Delta\|_1}{d_{\rm in}}
\le\|\Delta\|_\diamond
\le\left\|\mathrm{Tr}_{\rm out}|J_\Delta|\right\|.
```

The upper bound is a feasible Choi dual bound, not an optimization over all dual witnesses. No SDP optimum or interval certificate is claimed. Matrix positivity and norm inequalities are checked in floating point. The general theorem rests on the [written proofs](../science/README.md).

The published diagnostics have diamond upper bounds below 0.011, versus analytical envelope bounds below 0.263 at requested error 0.4. The trace-preservation residual is below $1.4\times10^{-14}$; small negative Choi eigenvalues are at roundoff scale. These finite values do not establish scaling laws or mathematical truth for untested dimensions.

To emit a fresh full report explicitly:

```bash
python3 verification/verify_averaged_channel.py --output verification/averaged_channel_results.json
```

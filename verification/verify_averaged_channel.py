"""Full averaged-channel diagnostics for the initialized controlled oracle.

This forms exact IID Schur multipliers (up to floating point), composes every
forward and independent-return stage, and examines the complete Choi matrix.
The resulting diamond bounds are standard Choi primal/dual bounds, not an SDP
solution or interval certificate. The analytic proof supplies the general result.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def two_level_hadamard_rows(array: np.ndarray, index: int, clock_dim: int) -> None:
    """Act on clock labels 0 and index; all padded labels receive identity."""
    for base in range(array.shape[-2] // clock_dim):
        zero, other = base * clock_dim, base * clock_dim + index
        row_zero = array[..., zero, :].copy()
        row_other = array[..., other, :].copy()
        array[..., zero, :] = (row_zero + row_other) / math.sqrt(2)
        array[..., other, :] = (row_zero - row_other) / math.sqrt(2)


def two_level_hadamard_channel(array: np.ndarray, index: int, clock_dim: int) -> None:
    two_level_hadamard_rows(array, index, clock_dim)
    for base in range(array.shape[-1] // clock_dim):
        zero, other = base * clock_dim, base * clock_dim + index
        col_zero = array[..., :, zero].copy()
        col_other = array[..., :, other].copy()
        array[..., :, zero] = (col_zero + col_other) / math.sqrt(2)
        array[..., :, other] = (col_zero - col_other) / math.sqrt(2)


def choi(images: np.ndarray) -> np.ndarray:
    input_dim, _, output_dim, _ = images.shape
    return images.transpose(0, 2, 1, 3).reshape(input_dim * output_dim, -1)


def output_partial_trace(matrix: np.ndarray, input_dim: int, output_dim: int) -> np.ndarray:
    return np.einsum("uava->uv", matrix.reshape(input_dim, output_dim, input_dim, output_dim))


def choi_diamond_bounds(matrix: np.ndarray, input_dim: int, output_dim: int) -> tuple[float, float]:
    """For Hermiticity-preserving maps: ||J||_1/d <= ||Phi||_diamond.

    The feasible dual operator |J| gives ||Phi||_diamond <= ||Tr_out |J|||.
    Neither bound is asserted to equal the diamond norm for this instance.
    """
    eigenvalues, eigenvectors = np.linalg.eigh((matrix + matrix.conj().T) / 2)
    absolute = (eigenvectors * np.abs(eigenvalues)) @ eigenvectors.conj().T
    partial = output_partial_trace(absolute, input_dim, output_dim)
    lower = float(np.sum(np.abs(eigenvalues)) / input_dim)
    upper = float(np.linalg.eigvalsh((partial + partial.conj().T) / 2).max())
    return lower, upper


def diagnose(probabilities: list[float], labels: list[int], floor: float, epsilon: float) -> dict:
    p = np.asarray(probabilities, dtype=float)
    f = np.asarray(labels, dtype=int)
    assert len(p) == len(f) and len(p) >= 2
    assert abs(float(p.sum()) - 1) < 1e-12 and np.min(p) >= floor > 0
    assert all(label in (0, 1) for label in labels) and 0 < epsilon <= 1
    address_dim = len(p)
    input_dim = 2 * address_dim  # outer coherent query control, then address
    upper = 1.0
    jmax = math.ceil(math.log2(2 * upper / floor))
    cycles = math.ceil(math.log(16 / epsilon, 4))
    stages = [(cycle, j, upper * 2.0**(-j))
              for cycle in range(cycles) for j in range(jmax + 1)]
    stage_count = len(stages)
    clock_dim = 1 << math.ceil(math.log2(stage_count + 1))
    output_dim = input_dim * clock_dim
    coefficients = [2 * math.pi**2 * 4.0**(-cycle) / a for cycle, _, a in stages]
    square_root_sum = 2 * sum(math.sqrt(value) for value in coefficients)
    sample_counts = [math.ceil(2 * square_root_sum * math.sqrt(value) / epsilon)
                     for value in coefficients]

    # Every input matrix unit is propagated: this is not a selected-state test.
    images = np.zeros((input_dim, input_dim, output_dim, output_dim), dtype=complex)
    ideal_isometry = np.zeros((output_dim, input_dim), dtype=complex)
    target_isometry = np.zeros_like(ideal_isometry)
    for u in range(input_dim):
        ideal_isometry[u * clock_dim, u] = 1
        target_isometry[u * clock_dim, u] = (-1)**((u // address_dim) * f[u % address_dim])
        for v in range(input_dim):
            images[u, v, u * clock_dim, v * clock_dim] = 1

    def phase_data(index: int) -> np.ndarray:
        indicators = np.zeros((address_dim, output_dim), dtype=float)
        for x in range(address_dim):
            indicators[x, (address_dim + x) * clock_dim + index] = f[x]
        return indicators

    def averaged_stage(index: int, a: float, count: int, sign: int) -> None:
        two_level_hadamard_channel(images, index, clock_dim)
        angle = sign * math.pi / (a * count)
        indicators = phase_data(index)
        one_sample_minus_identity = np.zeros((output_dim, output_dim), dtype=complex)
        for x in range(address_dim):
            difference = indicators[x, :, None] - indicators[x, None, :]
            one_sample_minus_identity += p[x] * np.expm1(1j * angle * difference)
        # log1p/expm1 retain the small variance term even for large sample counts.
        multiplier = np.exp(count * np.log1p(one_sample_minus_identity))
        images[:] *= multiplier
        two_level_hadamard_channel(images, index, clock_dim)

    ideal_gates = []
    envelope_excess = 0.0
    for index, ((cycle, _, a), count) in enumerate(zip(stages, sample_counts), 1):
        for x in range(address_dim):
            if f[x]:
                active = abs(ideal_isometry[(address_dim + x) * clock_dim,
                                             address_dim + x])
                envelope = 4.0**(-cycle) * min(1.0, a / p[x])
                envelope_excess = max(envelope_excess, active - envelope)
        averaged_stage(index, a, count, 1)
        two_level_hadamard_rows(ideal_isometry, index, clock_dim)
        phases = np.exp(1j * math.pi / a * np.sum(p[:, None] * phase_data(index), axis=0))
        ideal_isometry[:] *= phases[:, None]
        two_level_hadamard_rows(ideal_isometry, index, clock_dim)
        ideal_gates.append((index, phases))

    residual = max((abs(ideal_isometry[(address_dim + x) * clock_dim,
                                       address_dim + x]) for x in range(address_dim) if f[x]),
                   default=0.0)
    central_phase = np.ones(output_dim)
    for base in range(address_dim, input_dim):
        central_phase[base * clock_dim + 1:(base + 1) * clock_dim] = -1
    images[:] *= central_phase[:, None] * central_phase[None, :]
    ideal_isometry[:] *= central_phase[:, None]

    for reverse_index in range(stage_count - 1, -1, -1):
        index, phases = ideal_gates[reverse_index]
        _, _, a = stages[reverse_index]
        averaged_stage(index, a, sample_counts[reverse_index], -1)
        two_level_hadamard_rows(ideal_isometry, index, clock_dim)
        ideal_isometry[:] *= phases.conj()[:, None]
        two_level_hadamard_rows(ideal_isometry, index, clock_dim)

    actual_choi = choi(images)
    vector_target = target_isometry.T.reshape(-1)
    target_choi = np.outer(vector_target, vector_target.conj())
    difference = actual_choi - target_choi
    lower_bound, upper_bound = choi_diamond_bounds(difference, input_dim, output_dim)
    local_error_sum = 2 * sum(value / count for value, count in zip(coefficients, sample_counts))
    analytical_bound = 4 * 4.0**(-cycles) + local_error_sum
    isometry_error = float(np.linalg.norm(ideal_isometry - target_isometry, ord=2))
    hermiticity_error = float(np.linalg.norm(actual_choi - actual_choi.conj().T, ord=np.inf))
    trace_preservation_error = float(np.linalg.norm(
        output_partial_trace(actual_choi, input_dim, output_dim) - np.eye(input_dim), ord=np.inf))
    minimum_choi_eigenvalue = float(np.linalg.eigvalsh((actual_choi + actual_choi.conj().T) / 2).min())
    padding_rows = [base * clock_dim + label for base in range(input_dim)
                    for label in range(stage_count + 1, clock_dim)]
    padding_amplitude = (float(np.max(np.abs(images[..., padding_rows, :])))
                         if padding_rows else 0.0)
    assert envelope_excess <= 2e-12
    assert residual <= 4.0**(-cycles) + 2e-12
    assert isometry_error <= 2 * residual + 2e-11
    assert hermiticity_error < 2e-10
    assert trace_preservation_error < 2e-10
    assert minimum_choi_eigenvalue > -2e-10
    assert padding_amplitude < 2e-12
    assert lower_bound <= upper_bound + 2e-10
    assert upper_bound <= analytical_bound + 2e-9
    assert analytical_bound <= epsilon + 2e-12

    # On the all-one function an uncontrolled phase would be invisible. The
    # coherent query control makes this exactly a Z operation and is observable.
    controlled_global_phase_distance = None
    if np.all(f == 1):
        identity_isometry = np.zeros_like(target_isometry)
        for u in range(input_dim):
            identity_isometry[u * clock_dim, u] = 1
        vector_identity = identity_isometry.T.reshape(-1)
        ideal_vs_identity = target_choi - np.outer(vector_identity, vector_identity.conj())
        controlled_global_phase_distance = choi_diamond_bounds(
            ideal_vs_identity, input_dim, output_dim)[0]
        assert abs(controlled_global_phase_distance - 2) < 2e-10

    return {
        "probabilities": probabilities, "labels": labels, "public_floor": floor,
        "epsilon": epsilon, "cycles": cycles, "stages_each_direction": stage_count,
        "clock_dimension_including_padding": clock_dim,
        "unused_clock_labels": clock_dim - stage_count - 1,
        "fresh_samples_forward_and_return": 2 * sum(sample_counts),
        "minimum_sample_block": min(sample_counts),
        "ideal_residual_active_amplitude": float(residual),
        "ideal_clean_isometry_error": isometry_error,
        "maximum_envelope_excess": max(0.0, float(envelope_excess)),
        "full_channel_diamond_lower_bound": lower_bound,
        "full_channel_diamond_dual_upper_bound": upper_bound,
        "proved_envelope_error_bound": analytical_bound,
        "trace_preservation_error_inf": trace_preservation_error,
        "choi_hermiticity_error_inf": hermiticity_error,
        "minimum_choi_eigenvalue": minimum_choi_eigenvalue,
        "padding_output_maximum_entry": padding_amplitude,
        "controlled_all_one_vs_identity_diamond_lower_bound": controlled_global_phase_distance,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [([0.73, 0.27], [1, 0], 0.25, 0.4),
             ([0.5, 0.5], [1, 1], 0.5, 0.4),
             ([0.61, 0.39], [0, 0], 0.3, 0.4),
             ([0.96875, 0.03125], [0, 1], 0.03125, 0.4)]
    result = {
        "status": "passed",
        "scope": "Floating-point complete initialized controlled-oracle Choi maps from exact IID characteristic functions, with independent forward/return blocks. Choi norm bounds enclose diamond distance; no SDP optimum or interval certificate is claimed.",
        "cases": [diagnose(*case) for case in cases],
    }
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()

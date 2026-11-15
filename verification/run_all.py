"""Reproduce the complete initialized-channel scientific diagnostics."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def main() -> None:
    script = Path(__file__).with_name("verify_averaged_channel.py")
    completed = subprocess.run([sys.executable, str(script)], check=True,
                               capture_output=True, text=True)
    result = json.loads(completed.stdout)
    cases = result["cases"]
    print(f"PASS: {len(cases)} complete initialized controlled-channel diagnostics")
    print("Maximum diamond dual upper bound: "
          f"{max(c['full_channel_diamond_dual_upper_bound'] for c in cases):.8g}")
    print("Maximum trace-preservation residual: "
          f"{max(c['trace_preservation_error_inf'] for c in cases):.3g}")
    print(result["scope"])


if __name__ == "__main__":
    main()

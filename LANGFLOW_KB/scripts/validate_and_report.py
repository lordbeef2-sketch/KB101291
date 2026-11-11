#!/usr/bin/env python3
"""Validate and optionally run a Langflow flow, producing an evidence receipt.

NEVER execute untrusted component code. --execute is an explicit opt-in.
No provider keys are printed or stored. Output is deliberately not saved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

def run(argv, timeout):
    # Never persist stdout/stderr or the user-provided input value by default.
    # Flow output and error traces can contain prompt text, access tokens or PII.
    safe_command = [
        "<REDACTED>" if i and argv[i - 1] == "--input-value" else arg
        for i, arg in enumerate(argv)
    ]
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=timeout, check=False)
        return {
            "command": safe_command,
            "exit_code": p.returncode,
            "stdout_characters": len(p.stdout),
            "stderr_characters": len(p.stderr),
            "stdout_sha256": hashlib.sha256(p.stdout.encode()).hexdigest(),
            "stderr_sha256": hashlib.sha256(p.stderr.encode()).hexdigest(),
            "timed_out": False,
        }
    except subprocess.TimeoutExpired:
        return {"command": safe_command, "exit_code": None, "timed_out": True,
                "stdout_characters": None, "stderr_characters": None}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("flow", type=Path)
    p.add_argument("--level", type=int, default=4, choices=(1, 2, 3, 4))
    p.add_argument("--execute", action="store_true",
                   help="Explicitly run all components; may call paid APIs / tools")
    p.add_argument("--input-value", default="smoke test")
    p.add_argument("--timeout", type=int, default=120)
    p.add_argument("--report", type=Path)
    a = p.parse_args()
    if not a.flow.is_file():
        p.error("Flow does not exist")
    if shutil.which("lfx") is None:
        p.error("lfx executable missing. Install correct LFX version and bundles first")
    try:
        obj = json.loads(a.flow.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as e:
        p.error(f"Invalid JSON: {e}")
    data = obj.get("data") if isinstance(obj, dict) else None
    if not isinstance(data, dict) or not isinstance(data.get("nodes"), list) or not isinstance(data.get("edges"), list):
        p.error("Missing data.nodes / data.edges; use official 1.13.2 exported flow")
    receipt = {"flow": str(a.flow), "timestamp_utc": datetime.now(timezone.utc).isoformat(),
               "graph": {"nodes": len(data["nodes"]), "edges": len(data["edges"])},
               "validation": run(["lfx", "validate", str(a.flow), "--level", str(a.level)], a.timeout),
               "execution": None, "live_tested": False}
    if a.execute and receipt["validation"]["exit_code"] == 0:
        receipt["execution"] = run(
            ["lfx", "run", str(a.flow), "--input-value", a.input_value, "--format", "json"],
            a.timeout)
        receipt["live_tested"] = receipt["execution"]["exit_code"] == 0
    if a.report:
        a.report.parent.mkdir(parents=True, exist_ok=True)
        a.report.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if receipt["validation"]["exit_code"] != 0 or (
        a.execute and not receipt["live_tested"]
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

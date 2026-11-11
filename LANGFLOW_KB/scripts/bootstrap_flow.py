#!/usr/bin/env python3
"""Copy a real, tagged official Langflow starter JSON as an editable baseline."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

KB = Path(__file__).resolve().parents[1]
STARTERS = KB / "upstream-langflow/src/backend/base/langflow/initial_setup/starter_projects"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--list", action="store_true", help="List official 1.13.2 starter JSON files")
    p.add_argument("--starter", help="Exact starter name, e.g. Simple Agent")
    p.add_argument("--output", type=Path, help="Write destination .json (does not overwrite)")
    a = p.parse_args()

    if not STARTERS.is_dir():
        p.error("Missing upstream submodule; run git submodule update --init --recursive")
    choices = sorted(STARTERS.glob("*.json"))
    if a.list:
        for f in choices:
            print(f.stem)
        return
    if not a.starter or a.output is None:
        p.error("--starter and --output are required unless --list")
    source = next((f for f in choices if f.stem.casefold() == a.starter.casefold()), None)
    if source is None:
        p.error("Unknown starter; use --list")
    if a.output.suffix.lower() != ".json":
        p.error("--output must end in .json")
    with source.open("r", encoding="utf-8") as f:
        data = json.load(f)
    inner = data.get("data") if isinstance(data, dict) else None
    if not isinstance(inner, dict) or not isinstance(inner.get("nodes"), list) or not isinstance(inner.get("edges"), list):
        p.error("Starter has unexpected flow JSON structure")
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with a.output.open("x", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2)
        out.write("\n")
    print(f"Copied official starter '{source.name}' -> {a.output}")
    print("IMPORTANT: This is an UNTESTED baseline until lfx validate and runtime execution succeed.")
    print("Duplicate flow IDs may conflict if imported into an existing instance; use an official create/duplicate path.")


if __name__ == "__main__":
    main()

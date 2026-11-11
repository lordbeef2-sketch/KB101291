#!/usr/bin/env python3
"""Build a source-anchored, version-pinned LLM corpus for Langflow 1.13.2.

No arbitrary Langflow/plugin code is imported or executed. This is static analysis.
Requires: Python 3.10+ and a recursively checked-out upstream git submodule.
Output directory: LANGFLOW_KB/generated (gitignored).
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

KB = Path(__file__).resolve().parents[1]
UPSTREAM = KB / "upstream-langflow"
GENERATED = KB / "generated"
EXPECTED_COMMIT = "8b42952d734de18e34c2838ff6c634efb1815878"
SOURCE_EXTS = {
    ".md", ".mdx", ".py", ".ts", ".tsx", ".js", ".jsx", ".mjs",
    ".json", ".yaml", ".yml", ".toml", ".txt", ".rst", ".sh",
    ".ps1", ".sql", ".graphql", ".proto", ".html", ".xml",
    ".css", ".ini", ".cfg", ".make", ".dockerfile",
}
SKIP_DIRS = {
    ".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__",
    ".next", ".cache", ".tox", ".mypy_cache", ".pytest_cache",
    "coverage", "vendor",
}
MAX_BYTES = 1024 * 1024
CHUNK_CHARS = 4500
CHUNK_LINES = 85
ENV_RE = re.compile(r"\b(?:LANGFLOW|LFX)_[A-Z][A-Z0-9_]*\b")
VERSION = "1.13.2"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_BYTES:
            return None
        return path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return None


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def relative(path: Path) -> str:
    return path.relative_to(UPSTREAM).as_posix()


def literal(expr: ast.AST | None) -> Any:
    if expr is None:
        return None
    try:
        return ast.literal_eval(expr)
    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
        try:
            return {"dynamic_expression": ast.unparse(expr)[:800]}
        except Exception:
            return {"dynamic_expression": "<unknown>"}


def py_expression(expr: ast.AST | None) -> str:
    if expr is None:
        return ""
    try:
        return ast.unparse(expr)[:800]
    except Exception:
        return ""


def class_fields(expr: ast.AST | None) -> dict[str, Any]:
    """Extract named Input/Output constructor calls without executing Python."""
    if expr is None:
        return {"dynamic": True, "items": []}
    if isinstance(expr, (ast.Tuple, ast.List, ast.Set)):
        entries = expr.elts
        dynamic = False
    else:
        entries = [expr]
        dynamic = True
    result = []
    for entry in entries:
        if isinstance(entry, ast.Call):
            result.append({
                "constructor": py_expression(entry.func),
                "args": [literal(v) for v in entry.args],
                "kwargs": {kw.arg or "**": literal(kw.value) for kw in entry.keywords},
                "line": getattr(entry, "lineno", None),
            })
        else:
            result.append({"dynamic_expression": py_expression(entry), "line": getattr(entry, "lineno", None)})
            dynamic = True
    return {"dynamic": dynamic, "items": result}


def class_assignments(cls: ast.ClassDef) -> dict[str, ast.AST]:
    d: dict[str, ast.AST] = {}
    for stmt in cls.body:
        if isinstance(stmt, ast.Assign):
            for dest in stmt.targets:
                if isinstance(dest, ast.Name):
                    d[dest.id] = stmt.value
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and stmt.value is not None:
            d[stmt.target.id] = stmt.value
    return d


def component_category(path: str) -> str:
    parts = Path(path).parts
    if "components" in parts:
        i = parts.index("components")
        return parts[i + 1] if i + 1 < len(parts) - 1 else "core"
    if "bundles" in parts:
        i = parts.index("bundles")
        return "bundle-" + (parts[i + 1] if i + 1 < len(parts) else "unknown")
    return "unknown"


def parse_components(path: Path, source: str) -> list[dict[str, Any]]:
    p = relative(path)
    if not ("/components/" in "/" + p or p.startswith("src/bundles/")):
        return []
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    records = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        assignments = class_assignments(node)
        base_names = [py_expression(base) for base in node.bases]
        maybe_component = (
            "inputs" in assignments or "outputs" in assignments or
            node.name.endswith("Component") or
            any("Component" in base or "Tool" in base for base in base_names)
        )
        if not maybe_component:
            continue
        docstring = ast.get_docstring(node) or ""
        display = literal(assignments.get("display_name"))
        description = literal(assignments.get("description"))
        name = display if isinstance(display, str) else node.name
        records.append({
            "class_name": node.name,
            "display_name": name,
            "description": description if isinstance(description, str) else docstring[:800],
            "docstring": docstring[:3000],
            "bases": base_names,
            "source": p,
            "line": node.lineno,
            "category": component_category(p),
            "inputs": class_fields(assignments.get("inputs")),
            "outputs": class_fields(assignments.get("outputs")),
            "methods": [
                {
                    "name": x.name,
                    "line": x.lineno,
                    "async": isinstance(x, ast.AsyncFunctionDef),
                    "returns": py_expression(x.returns),
                }
                for x in node.body
                if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef))
            ],
            "source_only": True,
        })
    return records


def parse_cli_and_routes(path: Path, source: str) -> tuple[list[dict], list[dict]]:
    p = relative(path)
    if not p.endswith(".py"):
        return [], []
    is_cli = "/cli/" in "/" + p
    is_api = "/api/" in "/" + p or "/routes/" in "/" + p or p.endswith("router.py")
    if not is_cli and not is_api:
        return [], []
    try:
        mod = ast.parse(source)
    except SyntaxError:
        return [], []
    cli: list[dict] = []
    routes: list[dict] = []
    for fn in ast.walk(mod):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for dec in fn.decorator_list:
            if not isinstance(dec, ast.Call) or not isinstance(dec.func, ast.Attribute):
                continue
            method = dec.func.attr
            prefix = py_expression(dec.func.value)
            name_or_route = literal(dec.args[0]) if dec.args else None
            params = []
            args = fn.args.posonlyargs + fn.args.args + fn.args.kwonlyargs
            for arg in args:
                params.append({
                    "name": arg.arg,
                    "annotation": py_expression(arg.annotation),
                })
            record = {
                "python_function": fn.name,
                "decorator_owner": prefix,
                "decorator": method,
                "declared_name_or_path": name_or_route,
                "source": p,
                "line": fn.lineno,
                "params": params,
                "summary": (ast.get_docstring(fn) or "").split("\n")[0][:400],
            }
            if is_cli and method in {"command", "callback", "group"}:
                cli.append(record)
            if is_api and method.lower() in {"get", "post", "put", "patch", "delete", "options", "head", "api_route"}:
                routes.append(record)
    return cli, routes


def split_content(source: str, *, max_chars: int = CHUNK_CHARS, max_lines: int = CHUNK_LINES):
    """Line-preserving, bounded chunks. No prompt interpretation."""
    lines = source.splitlines()
    start = 0
    while start < len(lines):
        end = start
        chars = 0
        while end < len(lines) and end - start < max_lines:
            length = len(lines[end]) + 1
            if end > start and chars + length > max_chars:
                break
            chars += length
            end += 1
        if end == start:
            end = start + 1
        yield (start + 1, end, "\n".join(lines[start:end]))
        start = end


def safe_filename(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", value)[:90] or "unknown"


def guide_doc_source(component: dict, doc_paths: list[str]) -> tuple[str | None, str]:
    cat = component["category"].replace("bundle-", "")
    display = component["display_name"].lower()
    stem = re.sub(r"[^a-z0-9]+", "-", display).strip("-")
    candidates = [x for x in doc_paths if Path(x).stem.lower() == stem]
    if candidates:
        return candidates[0], "exact_doc"
    if component["category"].startswith("bundle-"):
        candidates = [x for x in doc_paths if Path(x).stem.lower() == "bundles-" + cat]
        if candidates:
            return candidates[0], "bundle_doc"
    return None, "source_only"


def render_guide(c: dict, doc: str | None, confidence: str, doc_text: str | None) -> str:
    lines = [
        "# " + c["display_name"],
        "",
        "## Identification",
        "- Python class: " + c["class_name"],
        "- Source: upstream-langflow/" + c["source"] + ":" + str(c["line"]),
        "- Version: " + VERSION,
        "- Category: " + c["category"],
        "- How-to evidence: " + confidence,
        "- Matching official doc source: " + (("upstream-langflow/" + doc) if doc else "NONE VERIFIED"),
        "",
        "## Purpose",
        str(c["description"] or "UNKNOWN - inspect implementation and tests"),
        "",
        "## Inputs (static AST; runtime may differ)",
        "Dynamic expression present: " + str(c["inputs"]["dynamic"]),
    ]
    for inp in c["inputs"]["items"]:
        lines.append("- " + json.dumps(inp, ensure_ascii=False, sort_keys=True))
    lines.extend(["", "## Outputs (static AST; runtime may differ)",
                  "Dynamic expression present: " + str(c["outputs"]["dynamic"])])
    for out in c["outputs"]["items"]:
        lines.append("- " + json.dumps(out, ensure_ascii=False, sort_keys=True))
    lines.extend([
        "", "## Methods",
        ", ".join(m["name"] + "@" + str(m["line"]) for m in c["methods"]) or "none declared",
        "", "## How to connect and execute",
        "1. Ensure component's provider/bundle is installed in the target environment.",
        "2. Use exact input name/types and method-bound output names from this class and live registry.",
        "3. Find a 1.13.2 starter/exported JSON node with matching type; preserve serialized handles.",
        "4. Supply required values via protected environment/connection references, not inline secrets.",
        "5. Validate the graph with installed lfx validate and run a representative input.",
        "6. Check runtime logs and negative cases. Never claim this static card is a passing runtime test.",
    ])
    if doc_text:
        lines.extend(["", "## Official documentation (verbatim source excerpt)",
                      "For the **full** official text, retrieve the source file above.", "",
                      doc_text[:12000]])
    else:
        lines.extend(["", "## Documentation gap",
                      "No uniquely matching official component how-to was located by file/name heuristic. "
                      "Read upstream Python class, tests and any provider bundle README; do not guess exact setup."])
    return "\n".join(lines) + "\n"


def discover_repo_files() -> list[Path]:
    found = []
    for p in UPSTREAM.rglob("*"):
        if not p.is_file() or any(part in SKIP_DIRS for part in p.relative_to(UPSTREAM).parts):
            continue
        found.append(p)
    return sorted(found, key=lambda q: relative(q))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-only", action="store_true",
                        help="Only source documentation and guides in text chunks; still index source metadata")
    args = parser.parse_args()

    if not (UPSTREAM / "src").is_dir() or not (UPSTREAM / "docs").is_dir():
        raise SystemExit("Upstream submodule missing: git submodule update --init --recursive")
    try:
        head = subprocess.check_output(
            ["git", "-C", str(UPSTREAM), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        raise SystemExit("Cannot verify upstream commit; git/submodule checkout required")
    if head != EXPECTED_COMMIT:
        raise SystemExit("Wrong upstream commit: " + head + "; expected " + EXPECTED_COMMIT)

    GENERATED.mkdir(parents=True, exist_ok=True)
    guide_dir = GENERATED / "component_guides"
    docs_dir = UPSTREAM / "docs" / "docs"
    official_docs = sorted(
        relative(p) for p in docs_dir.rglob("*")
        if p.is_file() and p.suffix in {".md", ".mdx"}
    )

    all_files = discover_repo_files()
    inventory = []
    components, cli_symbols, api_routes = [], [], []
    env_sources = defaultdict(set)
    examples = []
    chunks = 0
    skipped = []
    documents = GENERATED / "documents.jsonl"

    with documents.open("w", encoding="utf-8") as corpus:
        for file in all_files:
            path = relative(file)
            ext = file.suffix.lower()
            try:
                size = file.stat().st_size
            except OSError:
                continue
            item = {"path": path, "bytes": size, "extension": ext}
            inventory.append(item)
            if ext not in SOURCE_EXTS:
                continue
            source = safe_text(file)
            if source is None:
                skipped.append({"path": path, "reason": "too_large_or_unreadable"})
                continue
            item["sha256"] = sha256(source.encode("utf-8"))
            for key in set(ENV_RE.findall(source)):
                env_sources[key].add(path)
            if ext == ".py":
                components.extend(parse_components(file, source))
                cli, routes = parse_cli_and_routes(file, source)
                cli_symbols.extend(cli)
                api_routes.extend(routes)
            if ext == ".json" and size < MAX_BYTES:
                try:
                    data = json.loads(source)
                    graphs = [data]
                    if isinstance(data, dict) and isinstance(data.get("flow"), dict):
                        graphs.append(data["flow"])
                    for graph in graphs:
                        if not isinstance(graph, dict):
                            continue
                        inner = graph.get("data")
                        if not isinstance(inner, dict):
                            continue
                        nodes, edges = inner.get("nodes"), inner.get("edges")
                        if not isinstance(nodes, list) or not isinstance(edges, list):
                            continue
                        kinds = Counter(
                            str(node.get("data", {}).get("type", "UNKNOWN"))
                            for node in nodes if isinstance(node, dict)
                        )
                        examples.append({
                            "source": path, "name": graph.get("name"), "id": graph.get("id"),
                            "nodes": len(nodes), "edges": len(edges),
                            "types": dict(kinds), "sha256": item["sha256"],
                        })
                        break
                except (json.JSONDecodeError, TypeError, ValueError):
                    pass
            if args.docs_only and not (
                path.startswith("docs/") or path.endswith("README.md") or path.endswith("AGENTS.md")
            ):
                continue
            kind = ("docs" if path.startswith("docs/") else
                    "component_source" if "/components/" in "/" + path else
                    "cli_or_api" if "/cli/" in "/" + path or "/api/" in "/" + path else "source")
            for first, last, text in split_content(source):
                if not text.strip():
                    continue
                obj = {
                    "id": sha256((head + "|" + path + "|" + str(first)).encode())[:24],
                    "source_commit": head, "version": VERSION, "kind": kind,
                    "path": path, "start_line": first, "end_line": last, "text": text,
                }
                corpus.write(json.dumps(obj, ensure_ascii=False) + "\n")
                chunks += 1

        components.sort(key=lambda c: (c["category"], c["display_name"], c["source"], c["line"]))
        guide_index = []
        for c in components:
            doc, status = guide_doc_source(c, official_docs)
            c["official_doc"] = doc
            c["howto_evidence"] = status
            snippet = safe_text(UPSTREAM / doc) if doc else None
            unique = sha256((c["source"] + ":" + str(c["line"])).encode())[:10]
            guide_file = guide_dir / safe_filename(c["category"]) / (
                safe_filename(c["class_name"]) + "_" + unique + ".md"
            )
            guide_file.parent.mkdir(parents=True, exist_ok=True)
            guide = render_guide(c, doc, status, snippet)
            guide_file.write_text(guide, encoding="utf-8")
            c["guide_path"] = guide_file.relative_to(GENERATED).as_posix()
            guide_index.append({
                "name": c["display_name"], "class_name": c["class_name"],
                "guide": c["guide_path"], "source": c["source"],
                "official_doc": doc, "howto_evidence": status,
            })
            for first, last, text in split_content(guide):
                if not text.strip():
                    continue
                obj = {
                    "id": sha256((head + "|guide|" + c["guide_path"] + "|" + str(first)).encode())[:24],
                    "source_commit": head, "version": VERSION, "kind": "component_guide",
                    "path": c["guide_path"], "start_line": first, "end_line": last, "text": text,
                }
                corpus.write(json.dumps(obj, ensure_ascii=False) + "\n")
                chunks += 1

    write_json(GENERATED / "components.json", components)
    write_json(GENERATED / "cli_symbols.json", cli_symbols)
    write_json(GENERATED / "api_routes.json", api_routes)
    write_json(GENERATED / "environment_variables.json", [
        {"name": k, "source_files": sorted(v), "source_count": len(v)}
        for k, v in sorted(env_sources.items())
    ])
    write_json(GENERATED / "flow_examples.json", sorted(examples, key=lambda x: x["source"]))
    write_json(GENERATED / "source_inventory.json", inventory)
    write_json(GENERATED / "skipped_source_files.json", skipped)

    guide_lines = [
        "# Component guides — generated, source-anchored",
        "", "These pages are AST-derived and NOT runtime verified.",
        "If no exact upstream doc exists, source-only does not establish working configuration.",
        "",
    ]
    for x in guide_index:
        guide_lines.append(
            "- [" + x["name"].replace("[", "(").replace("]", ")") + "](" +
            x["guide"] + ") — " + x["class_name"] +
            " | " + x["howto_evidence"] + " | " + x["source"]
        )
    (GENERATED / "component_howtos.md").write_text("\n".join(guide_lines) + "\n", encoding="utf-8")

    counts = {
        "files_in_inventory": len(inventory),
        "components_candidates": len(components),
        "components_with_matched_docs": sum(c["howto_evidence"] != "source_only" for c in components),
        "cli_decorated_functions": len(cli_symbols),
        "api_decorated_routes": len(api_routes),
        "environment_symbols": len(env_sources),
        "exported_flow_examples": len(examples),
        "retrieval_chunks": chunks,
        "unreadable_or_oversized_text_files": len(skipped),
    }
    manifest = {
        "project": "Langflow", "version": VERSION,
        "upstream_git_commit": head, "generator": "scripts/build_corpus.py",
        "docs_only": args.docs_only, "source_of_truth": "pinned_upstream_source",
        "static_extraction": True, "runtime_validated": False,
        "counts": counts,
    }
    write_json(GENERATED / "manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations
from pathlib import Path


def _bullet_list(items: list[str], indent: int = 0) -> str:
    pad = " " * indent
    return "\n".join([f"{pad}- {x}" for x in items]) if items else f"{pad}- (none)"


def render_markdown(report: dict) -> str:
    s = report["summary"]
    lines = []

    # Header
    lines.append("# GHGA Intake Readiness Report")
    lines.append("")
    lines.append(f"**Status:** `{s['status']}`")
    lines.append(f"**Intake ready:** `{s['intake_ready']}`")
    lines.append(f"**Readiness score:** **{s['readiness_score']} / 100**")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Samples valid: **{s['samples_valid']} / {s['total_samples']}**")
    lines.append(f"- Files OK: **{s['files_ok']} / {s['total_files']}**")
    lines.append("")
    lines.append("### Score breakdown")
    sb = s["score_breakdown"]
    lines.append(f"- Metadata: {sb['metadata']} (weight {sb['weights']['metadata']})")
    lines.append(f"- Files: {sb['files']} (weight {sb['weights']['files']})")
    lines.append(f"- QC: {sb['qc']} (weight {sb['weights']['qc']}) — not implemented yet")
    lines.append("")

    # Blocking issues
    lines.append("## Blocking issues (must fix before intake)")
    lines.append("")

    blocking = []
    # metadata blocking
    for sample_id, info in report["samples"].items():
        if not info["metadata_valid"]:
            blocking.append(f"Metadata invalid for `{sample_id}`")
    # file blocking
    for f in report["files"]:
        if not f["ok"]:
            blocking.append(f"File check failed: `{f['file_path']}`")

    if not blocking:
        lines.append("- None ")
    else:
        lines.append(_bullet_list(blocking))

    lines.append("")

    # Details per sample
    lines.append("## Sample metadata validation")
    lines.append("")
    for sample_id, info in report["samples"].items():
        lines.append(f"### {sample_id}")
        lines.append(f"- Valid: `{info['metadata_valid']}`")
        if info["metadata_errors"]:
            lines.append("**Errors:**")
            lines.append(_bullet_list(info["metadata_errors"]))
        else:
            lines.append("- No metadata errors")
        lines.append("")

    # File table-like section
    lines.append("## File checks")
    lines.append("")
    for f in report["files"]:
        lines.append(f"- `{f['file_path']}` | sample `{f['sample_id']}` | ok `{f['ok']}` | size `{f.get('size_bytes')}`")
        if f["errors"]:
            lines.append("  - Errors:")
            lines.append(_bullet_list(f["errors"], indent=4))
        if f["warnings"]:
            lines.append("  - Warnings:")
            lines.append(_bullet_list(f["warnings"], indent=4))
    lines.append("")

    return "\n".join(lines)


def save_markdown(md: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

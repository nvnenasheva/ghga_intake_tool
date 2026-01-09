from __future__ import annotations

import argparse
from pathlib import Path

from .validate_metadata import validate_metadata_dir
from .file_checks import check_files_from_manifest
from .report import build_report, save_report
from .markdown_report import render_markdown, save_markdown


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ghga_intake", description="GHGA intake readiness checker (MVP).")
    p.add_argument("--manifest", required=True, type=Path, help="Path to manifest.csv")
    p.add_argument("--metadata_dir", required=True, type=Path, help="Directory with metadata JSON files")
    p.add_argument("--schema", required=True, type=Path, help="Path to JSON Schema file")
    p.add_argument("--out", default=Path("outputs/report"), type=Path,
                   help="Output prefix (default: outputs/report). Writes .json and .md")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # run checks
    metadata_results = validate_metadata_dir(args.metadata_dir, args.schema)
    file_results = check_files_from_manifest(args.manifest)

    # build report
    report = build_report(metadata_results, file_results)

    # save outputs
    out_json = args.out.with_suffix(".json")
    out_md = args.out.with_suffix(".md")

    save_report(report, out_json)
    md = render_markdown(report)
    save_markdown(md, out_md)

    # summary
    print("JSON report:", out_json.resolve())
    print("Markdown report:", out_md.resolve())
    print("Status:", report["summary"]["status"], "| Score:", report["summary"]["readiness_score"])
    print("Ready for intake:", report["summary"]["intake_ready"])

    return 0

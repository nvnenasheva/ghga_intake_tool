from pathlib import Path

from validate_metadata import validate_metadata_dir
from file_checks import check_files_from_manifest
from report import build_report, save_report
from markdown_report import render_markdown, save_markdown


if __name__ == "__main__":
    schema = Path("schemas/sample_metadata.schema.json")
    metadata_dir = Path("examples/metadata")
    manifest = Path("examples/manifest.csv")

    out_json = Path("outputs/report.json")
    out_md = Path("outputs/report.md")

    metadata_results = validate_metadata_dir(metadata_dir, schema)
    file_results = check_files_from_manifest(manifest)

    report = build_report(metadata_results, file_results)
    save_report(report, out_json)

    md = render_markdown(report)
    save_markdown(md, out_md)

    print("JSON report:", out_json.resolve())
    print("Markdown report:", out_md.resolve())
    print("Status:", report["summary"]["status"], "| Score:", report["summary"]["readiness_score"])

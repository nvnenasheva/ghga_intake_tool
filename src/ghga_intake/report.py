from __future__ import annotations
from pathlib import Path
import json


def _calc_readiness_score(total_samples: int, samples_valid: int, total_files: int, files_ok: int) -> dict:
    # Weights
    W_META = 50
    W_FILES = 40
    W_QC = 10  # placeholder for future QC integration

    meta_score = W_META * (samples_valid / total_samples) if total_samples else 0
    files_score = W_FILES * (files_ok / total_files) if total_files else 0
    qc_score = 0  # not implemented yet

    score = round(meta_score + files_score + qc_score, 1)

    return {
        "score": score,
        "meta_score": round(meta_score, 1),
        "files_score": round(files_score, 1),
        "qc_score": qc_score,
        "weights": {"metadata": W_META, "files": W_FILES, "qc": W_QC},
    }


def build_report(metadata_results: dict, file_results: list[dict]) -> dict:
    total_samples = len(metadata_results)
    samples_valid = sum(1 for v in metadata_results.values() if v["ok"])
    samples_invalid = total_samples - samples_valid

    total_files = len(file_results)
    files_ok = sum(1 for f in file_results if f["ok"])
    files_failed = total_files - files_ok

    intake_ready = (samples_invalid == 0) and (files_failed == 0)

    scoring = _calc_readiness_score(total_samples, samples_valid, total_files, files_ok)
    status = "READY" if (intake_ready and scoring["score"] >= 90) else "NEEDS_FIX"

    report = {
        "summary": {
            "total_samples": total_samples,
            "samples_valid": samples_valid,
            "samples_invalid": samples_invalid,
            "total_files": total_files,
            "files_ok": files_ok,
            "files_failed": files_failed,
            "intake_ready": intake_ready,
            "status": status,
            "readiness_score": scoring["score"],
            "score_breakdown": {
                "metadata": scoring["meta_score"],
                "files": scoring["files_score"],
                "qc": scoring["qc_score"],
                "weights": scoring["weights"],
            },
        },
        "samples": {},
        "files": [],
    }

    for sample_id, res in metadata_results.items():
        report["samples"][sample_id] = {
            "metadata_valid": res["ok"],
            "metadata_errors": res["errors"],
        }

    for f in file_results:
        report["files"].append(
            {
                "sample_id": f["sample_id"],
                "file_path": f["file_path"],
                "file_type": f.get("file_type"),
                "ok": f["ok"],
                "errors": f["errors"],
                "warnings": f["warnings"],
                "size_bytes": f.get("size_bytes"),
            }
        )

    return report


def save_report(report: dict, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

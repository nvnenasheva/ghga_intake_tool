from __future__ import annotations

import csv
import hashlib
from pathlib import Path


def compute_md5(path: Path, chunk_size: int = 8192) -> str:
    md5 = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            md5.update(chunk)
    return md5.hexdigest()


def check_files_from_manifest(manifest_csv: Path) -> list[dict]:
    results = []

    with manifest_csv.open() as f:
        reader = csv.DictReader(f)

        for row in reader:
            sample_id = row["sample_id"]
            file_path = Path(row["file_path"])
            expected_md5 = row.get("md5", "").strip()

            errors = []
            warnings = []

            if not file_path.exists():
                errors.append("File does not exist")
            elif file_path.stat().st_size == 0:
                errors.append("File is empty")
            else:
                if expected_md5:
                    actual_md5 = compute_md5(file_path)
                    if actual_md5 != expected_md5:
                        errors.append(
                            f"MD5 mismatch (expected {expected_md5}, got {actual_md5})"
                        )
                else:
                    warnings.append("No MD5 provided in manifest")

            results.append(
                {
                    "sample_id": sample_id,
                    "file_path": str(file_path),
                    "ok": len(errors) == 0,
                    "errors": errors,
                    "warnings": warnings,
                }
            )

    return results

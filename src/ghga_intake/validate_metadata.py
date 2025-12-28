import json
from pathlib import Path
from jsonschema import Draft202012Validator


def validate_metadata_dir(metadata_dir: Path, schema_path: Path) -> dict:
    results = {}

    schema = json.loads(schema_path.read_text())
    validator = Draft202012Validator(schema)

    for meta_file in metadata_dir.glob("*.json"):
        metadata = json.loads(meta_file.read_text())
        errors = []
        for e in validator.iter_errors(metadata):
            loc = ".".join([str(x) for x in e.path]) if e.path else "(root)"
            errors.append(f"{loc}: {e.message}")

        sample_id = metadata.get("sample_id", meta_file.stem)
        results[sample_id] = {
            "ok": len(errors) == 0,
            "errors": errors,
        }
    return results


if __name__ == "__main__":
    schema_path = Path("schemas/sample_metadata.schema.json")
    metadata_dir = Path("examples/metadata")
    print(f"Validating metadata against schema: {schema_path}")
    print("-" * 50)
    results = validate_metadata_dir(metadata_dir, schema_path)
    for sample_id, result in results.items():
        print(f"Validating {sample_id}")
        if result["ok"]:
            print(f"{sample_id} is valid")
        else:
            print(f"{sample_id} is NOT valid")
            for msg in result["errors"]:
                print("  -", msg)
        print("-" * 50)

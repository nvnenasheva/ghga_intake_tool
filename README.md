# GHGA Intake Mini-Tool

## Overview
This project is a small prototype that simulates the **intake and quality control of human genomics datasets** before their inclusion in a controlled-access archive such as the German Human Genome-Phenome Archive (GHGA).

The tool focuses on **metadata validation, file integrity checks, and dataset readiness assessment**, reflecting common challenges in managing sensitive human omics data.

## Motivation
In practice, many issues in data archiving arise not from sequencing quality itself, but from:
- incomplete or inconsistent metadata
- missing or mismatched files
- lack of clear QC documentation
- unclear readiness for data sharing

This prototype demonstrates how **early, automated validation steps** can reduce manual back-and-forth and improve data quality and reusability.

## Scope
The tool performs the following checks:

- **Metadata validation**  
  Validates sample metadata files against a JSON Schema using `jsonschema` (Draft 2020-12). Reports validation errors with specific field locations and messages.

- **File integrity checks**  
  Verifies the presence of data files listed in the manifest, checks file sizes, and validates optional MD5 checksums. Detects missing files and checksum mismatches.

- **Readiness scoring**  
  Calculates an operational readiness score based on:
  - Metadata completeness (50% weight)
  - File integrity (40% weight)
  - QC placeholder (10% weight, reserved for future QC integration)
  
  The final status is `READY` if all checks pass and score ≥ 90, otherwise `NEEDS_FIX`.

- **Report generation**  
  Produces both machine-readable (JSON) and human-readable (Markdown) reports with detailed validation results, error messages, and actionable recommendations.

No real patient data is used. All examples rely on public or mock datasets.

## Inputs

### Manifest File (CSV)
A CSV file with the following columns:
- `sample_id`: Identifier for the sample
- `file_path`: Relative path to the data file
- `md5`: Optional MD5 checksum for file verification

Example:
```csv
sample_id,file_path,md5
sample_001,examples/data/sample_001_R1.fastq.gz,e99a18c428cb38d5f260853678922e03
sample_002,examples/data/sample_002_R1.fastq.gz,
```

### Metadata Files (JSON)
JSON files containing sample metadata, validated against the provided JSON Schema. One file per sample, named `{sample_id}.json` or using the `sample_id` field within the JSON.

### JSON Schema
A JSON Schema file defining the structure and validation rules for metadata files.

## Outputs

The tool generates two report files:

1. **JSON Report** (`report.json`): Machine-readable structured report containing:
   - Validation results for each sample
   - File integrity check results
   - Overall readiness score and status
   - Detailed error messages

2. **Markdown Report** (`report.md`): Human-readable summary with:
   - Executive summary (status, score, readiness)
   - Per-sample validation details
   - Actionable recommendations

## Design Principles
- **Metadata-first approach**: data must be well-described before it can be shared.
- **Reproducibility**: all checks are deterministic and documented.
- **Separation of concerns**: validation, file checks, and reporting are modular.
- **Human genomics awareness**: designed with controlled-access and GDPR-sensitive data in mind.

## Intended Audience
This prototype is intended as a **demonstration project** for data stewardship and bioinformatics roles involving:
- human genomics data management
- research data infrastructures
- controlled-access data archives

## Status
This is a minimal, evolving prototype. Additional validation steps and QC integrations can be added as needed.

## Installation

### Requirements
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

The tool is packaged as a CLI and can be run with a single command:

```bash
PYTHONPATH=src python -m ghga_intake \
  --manifest examples/manifest.csv \
  --metadata_dir examples/metadata \
  --schema schemas/sample_metadata.schema.json \
  --out outputs/report
```

### Command-line Arguments

- `--manifest` (required): Path to the manifest CSV file listing data files
- `--metadata_dir` (required): Directory containing JSON metadata files (one per sample)
- `--schema` (required): Path to the JSON Schema file for metadata validation
- `--out` (optional): Output prefix for reports (default: `outputs/report`). Generates both `.json` and `.md` files

### Example

Using the provided examples:

```bash
PYTHONPATH=src python -m ghga_intake \
  --manifest examples/manifest.csv \
  --metadata_dir examples/metadata \
  --schema schemas/sample_metadata.schema.json
```

This will generate:
- `outputs/report.json` - Machine-readable JSON report
- `outputs/report.md` - Human-readable Markdown summary

The tool will also print a summary to the console:
```
JSON report: /path/to/outputs/report.json
Markdown report: /path/to/outputs/report.md
Status: NEEDS_FIX | Score: 75.0
Ready for intake: False
```

## Project Structure

```
ghga_intake_tool/
├── src/
│   └── ghga_intake/          # Main package
│       ├── cli.py            # Command-line interface
│       ├── validate_metadata.py  # Metadata validation
│       ├── file_checks.py    # File integrity checks
│       ├── report.py         # Report generation
│       └── markdown_report.py # Markdown rendering
├── examples/                 # Example data
│   ├── manifest.csv          # File manifest
│   ├── metadata/             # Sample metadata JSON files
│   └── data/                 # Example data files
├── schemas/                  # JSON Schema definitions
│   └── sample_metadata.schema.json
├── outputs/                  # Generated reports
└── requirements.txt          # Python dependencies
```

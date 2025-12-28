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
  Validates dataset metadata against a predefined JSON Schema to ensure completeness and consistency.

- **File integrity checks**  
  Verifies the presence of data files listed in a manifest, checks file types, sizes, and optional checksums.

- **QC artifact presence**  
  Detects whether basic QC reports (e.g. FastQC summaries) are available and flags missing QC information.

- **Readiness assessment**  
  Produces a structured report highlighting errors, warnings, and an overall readiness score for data intake.

No real patient data is used. All examples rely on public or mock datasets.

## Inputs
- JSON metadata files (one per sample or dataset)
- A manifest file listing associated data files
- Optional QC reports (e.g. FastQC outputs)

## Outputs
- A machine-readable JSON report summarizing validation results
- A human-readable summary highlighting issues and recommended actions

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

## How to use
### Requiremets
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Check validation of metadata
```bash
python3 validate_metadata.py
```
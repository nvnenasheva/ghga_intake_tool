<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #2c3e50;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 2em;
  }
  h1 {
    color: #1a5490;
    font-size: 2.5em;
    font-weight: 700;
    margin-bottom: 0.5em;
    border-bottom: 4px solid #4a90e2;
    padding-bottom: 0.3em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
  }
  h2 {
    color: #2c5aa0;
    font-size: 1.8em;
    font-weight: 600;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    padding-left: 0.5em;
    border-left: 5px solid #4a90e2;
    background: linear-gradient(90deg, rgba(74, 144, 226, 0.1) 0%, transparent 100%);
    padding: 0.5em;
    border-radius: 5px;
  }
  strong {
    color: #1a5490;
    font-weight: 600;
  }
  a {
    color: #4a90e2;
    text-decoration: none;
    font-weight: 500;
    border-bottom: 2px solid #4a90e2;
    transition: all 0.3s ease;
  }
  a:hover {
    color: #1a5490;
    border-bottom-color: #1a5490;
  }
  ul {
    list-style: none;
    padding-left: 0;
  }
  ul li {
    padding: 0.5em 0;
    padding-left: 1.5em;
    position: relative;
  }
  ul li:before {
    content: "▸";
    color: #4a90e2;
    font-weight: bold;
    position: absolute;
    left: 0;
  }
  code {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: 'Monaco', 'Courier New', monospace;
    font-size: 0.9em;
  }
  pre {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 1.2em;
    border-radius: 8px;
    border-left: 4px solid #4a90e2;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    overflow-x: auto;
  }
  pre code {
    background: transparent;
    padding: 0;
  }
  hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #4a90e2, transparent);
    margin: 3em 0;
  }
  .footnote {
    text-align: right;
    font-size: 0.85em;
    color: #7f8c8d;
    margin-top: 2em;
    padding-top: 1em;
    border-top: 1px solid #ecf0f1;
  }
  .title-slide {
    text-align: center;
    padding: 4em 3em;
    background: linear-gradient(135deg, #e8f4f8 0%, #d1e7dd 100%);
    border: 2px solid #4a90e2;
    border-radius: 12px;
    margin-bottom: 3em;
    box-shadow: 0 8px 24px rgba(74, 144, 226, 0.15);
    position: relative;
  }
  .title-slide::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, #1a5490 0%, #4a90e2 50%, #1a5490 100%);
    border-radius: 12px 12px 0 0;
  }
  .title-slide h1 {
    color: #1a5490;
    border-bottom: none;
    text-shadow: none;
    margin-bottom: 0.8em;
    font-size: 2.8em;
    letter-spacing: -0.02em;
  }
  .title-slide strong {
    color: #2c3e50;
    font-weight: 600;
  }
  .title-slide em {
    color: #7f8c8d;
    font-style: normal;
  }
  .title-slide a {
    color: #4a90e2;
    border-bottom: 2px solid #4a90e2;
  }
  .title-slide a:hover {
    color: #1a5490;
    border-bottom-color: #1a5490;
  }
  .title-slide .subtitle {
    color: #5a6c7d;
    font-size: 1.1em;
    margin-top: 0.5em;
    font-weight: 400;
  }
  .title-slide .author-info {
    margin-top: 2em;
    padding-top: 2em;
    border-top: 1px solid #ecf0f1;
  }
  .highlight-box {
    background: linear-gradient(135deg, #e8f4f8 0%, #d1e7dd 100%);
    border-left: 4px solid #4a90e2;
    padding: 1em;
    margin: 1em 0;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
</style>

<div class="title-slide">

# GHGA Intake Readiness Prototype

<div class="subtitle">A minimal, transparent tool for dataset onboarding</div>

<div class="author-info">

**Natalia Nenasheva**  
*Interview - Data Steward / Bioinformatics*

The full implementation is available on:  
**[GitHub Repository](https://github.com/nvnenasheva/ghga_intake_tool)**

12/01/2026
</div>

</div>

<!--
For the interview, I prepared a small prototype that simulates a GHGA-style data intake process.
It focuses on transparency, reproducibility, and practical decision-making rather than complex analytics.
-->

<div class="footnote">
<sup>1</sup> Natalia Nenasheva — 12/01/2026
</div>

---

## Motivation

Archiving human genomics data requires more than storage:
- complete and valid metadata
- file integrity and traceability
- transparent intake decisions

<div class="highlight-box">

This prototype simulates a realistic GHGA-style intake process.

</div>

<!--
When dealing with human genomics data, ingestion into an archive is not only about storing files.
It requires valid metadata, clear provenance, and confidence that the data can be reused legally and technically.

The goal of this prototype was to model a realistic intake scenario and make the decision process explicit.
-->

<div class="footnote">
<sup>1</sup> Natalia Nenasheva — 12/01/2026
</div>

---

## What the tool does

The tool performs three main checks:
- Metadata validation (JSON Schema)
- File integrity checks (existence, size, MD5)
- Aggregation into a single intake report

**Output:**
- Machine-readable JSON report
- Human-readable Markdown summary

<!--The tool performs three core checks.
First, it validates sample metadata using JSON Schema.
Second, it verifies file integrity, including existence, size, and optional MD5 checksums.

Finally, all results are merged into a single intake report, produced both as JSON for machines and Markdown for humans.
-->

<div class="footnote">
<sup>1</sup> Natalia Nenasheva — 12/01/2026
</div>

---

## Readiness Score

A simple operational score to support intake decisions:

<div class="highlight-box">

- **Metadata completeness** - 50%
- **File integrity** - 40%
- **QC placeholder** - 10%

</div>

The score supports prioritization.  
The final **READY** / **NEEDS_FIX** status is rule-based.

<!--
To make the intake decision more transparent, I introduced a simple readiness score.
It is not meant to evaluate scientific quality, but operational readiness.

Metadata is weighted highest because incomplete metadata blocks FAIR reuse.
File integrity is slightly lower, as file issues are often easier to fix.
Quality control is included as a placeholder, since QC requirements vary by project.

The score supports prioritization, while the final READY or NEEDS_FIX status is rule-based to avoid ambiguity.
-->

<div class="footnote">
<sup>1</sup> Natalia Nenasheva — 12/01/2026
</div>

---

## Usability

The tool is packaged as a **CLI**:

```bash
PYTHONPATH=src python -m ghga_intake \
  --manifest manifest.csv \
  --metadata_dir metadata/ \
  --schema schema.json
```

<div class="highlight-box">

This reflects real-world archive workflows.

</div>

<!--
I packaged the tool as a CLI to reflect real-world workflows.
It can be run with a single command and produces standardized outputs, similar to archive intake pipelines.

This also makes the tool easy to integrate into automated or semi-automated processes.
-->

<div class="footnote">
<sup>1</sup> Natalia Nenasheva — 12/01/2026
</div>

---

## Why this matters for GHGA

<div class="highlight-box">

- **Transparent and explainable** intake decisions
- **Clear feedback** to data providers
- **Extensible** for future policies (QC, access rules)
- **Aligns with FAIR** and archive best practices

</div>

<!--
This prototype reflects the core challenges of GHGA intake:
clear communication with data providers, transparent decisions, and extensibility.

While intentionally minimal, it demonstrates how structured checks, clear reporting, and policy-driven decisions can support a national genomics data infrastructure.
-->

<div class="footnote">
<sup>1</sup> Natalia Nenasheva — 12/01/2026
</div>
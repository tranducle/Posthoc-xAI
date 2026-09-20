# Post-hoc xAI phishing review: reproducibility package

This repository contains the study-level data, coding records, and reproducibility scripts for the systematic review **"Post-Hoc Explainable AI for Learning-Based Phishing Detection: A Systematic Literature Review and Evidence-Maturity Framework."**

The package is designed to reproduce the review's reported counts, percentages, sensitivity analyses, coding-reliability statistics, and the data underlying its tables and figures. It does not contain the manuscript, publisher PDFs, paper figures, or raw database exports.

## Repository contents

- `data/screening/`: full-text screening decisions for 156 assessed records.
- `data/extraction/`: extraction matrix for the 84 included studies.
- `data/coding/`: evidence-maturity, dataset, metric, baseline, temporal, and reliability coding.
- `data/canonical/study_master.csv`: canonical 84-study record used for the final synthesis.
- `derived/table_data/`: machine-readable data underlying the quantitative tables.
- `derived/figure_data/`: machine-readable data or definitions underlying Figures 1–5.
- `scripts/reproduce_results.py`: recomputes aggregate results and table/figure payloads.
- `scripts/reproduce_figures.py`: regenerates five stand-alone figures into a local `outputs/` directory.
- `scripts/verify_reproducibility.py`: checks the reported headline counts and reliability statistics.
- `docs/search_protocol.md`: database search protocol and source metadata.
- `docs/coding_codebook.md`: operational codebook used for evidence-maturity coding.
- `docs/FORMULAS.md`: formulas used for prevalence and reliability calculations.
- `docs/FILE_MAP.md`: mapping from manuscript tables/figures to repository data.
- `DATA.md`: data scope, provenance, and exclusions.
- `REPRODUCIBILITY.md`: end-to-end reproduction instructions.

## Quick start

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python scripts/verify_reproducibility.py
```

A successful run prints `"status": "PASS"` and regenerates the derived table/figure data from the public study-level records.

To regenerate local figure files:

```bash
python scripts/reproduce_figures.py
```

Generated images are written to `outputs/` and are intentionally excluded from version control.

## Data availability

The repository contains the screening, extraction, and derived coding records needed to audit the review. It does not redistribute publisher full texts or the original Scopus, Web of Science, or IEEE Xplore exports. See `DATA.md` for details.

## Version

The package version is recorded in `VERSION`. Git commit identifiers provide immutable snapshots of the public artifact.

## Citation

A formal citation will be added after publication. Until then, please cite the associated manuscript and the repository commit used for analysis.

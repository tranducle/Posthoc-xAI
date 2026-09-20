# Reproducibility

## Environment

Python 3.10 or newer is recommended.

Create a clean environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
```

The numerical synthesis uses only the Python standard library. Matplotlib is required only to render local figure files.

## Recompute all reported summaries

Run:

```bash
python scripts/reproduce_results.py
```

This command reads the public study-level records and regenerates:

- `derived/aggregate_results.json`;
- quantitative table payloads under `derived/table_data/`;
- figure data/definitions under `derived/figure_data/`;
- the coding-reliability table from the two coding passes in S6.

The script does not read the manuscript and does not use hard-coded local filesystem paths.

## Run the verification gate

```bash
python scripts/verify_reproducibility.py
```

The gate checks:

- 84 unique included studies;
- 156 full texts assessed, with 84 included and 72 excluded;
- annual publication counts;
- 63/84 studies in 2025–2026;
- 76 core post-hoc and 8 mixed-purpose studies;
- SHAP in 58 studies and LIME in 46;
- validation-design counts;
- trust, operational, validation-gate, reproducibility, and claim-risk counts;
- 72-study holdout agreement, Cohen/weighted kappa, and Gwet AC1 values.

A successful run writes `derived/verification_report.json` with `"status": "PASS"`.

## Regenerate local figures

First regenerate the figure data:

```bash
python scripts/reproduce_results.py
```

Then render figures:

```bash
python scripts/reproduce_figures.py
```

The figure script writes PNG and PDF files to `outputs/`. That directory is ignored by Git because this repository distributes the source data and generation code rather than manuscript image files.

Figures 1, 3, and 5 are directly data-driven. Figures 2 and 4 are conceptual summaries; their categories and evidence levels are stored as CSV files in `derived/figure_data/` so the displayed structure is auditable.

## Reproduce table data

Files in `derived/table_data/` are regenerated from the canonical study-level dataset and the metric/baseline coding files. `docs/FILE_MAP.md` maps each manuscript table to its source or generated payload.

## Reliability statistics

The reliability calculation uses the 72-study holdout subset in `data/coding/coding_reliability.csv`. Explanation role and mixed-purpose labels use unweighted Cohen kappa. Trust evidence, operational evidence, validation gate, reproducibility, and claim risk use quadratic-weighted Cohen kappa. Gwet AC1 and exact agreement are also reported. See `docs/FORMULAS.md`.

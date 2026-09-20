     1|# Post-hoc xAI phishing review: reproducibility package
     2|
     3|This repository contains the study-level data, coding records, and reproducibility scripts for the systematic review **“Post-Hoc Explainable AI for Learning-Based Phishing Detection: A Systematic Literature Review and Evidence-Maturity Taxonomy.”**
     4|
     5|The package is designed to reproduce the review's reported counts, percentages, sensitivity analyses, coding-reliability statistics, and the data underlying its tables and figures. It does not contain the manuscript, publisher PDFs, paper figures, or raw database exports.
     6|
     7|## Repository contents
     8|
     9|- `data/screening/`: full-text screening decisions for 156 assessed records.
    10|- `data/extraction/`: extraction matrix for the 84 included studies.
    11|- `data/coding/`: evidence-maturity, dataset, metric, baseline, temporal, and reliability coding.
    12|- `data/canonical/study_master.csv`: canonical 84-study record used for the final synthesis.
    13|- `derived/table_data/`: machine-readable data underlying the quantitative tables.
    14|- `derived/figure_data/`: machine-readable data or definitions underlying Figures 1–6.
    15|- `scripts/reproduce_results.py`: recomputes aggregate results and table/figure payloads.
    16|- `scripts/reproduce_figures.py`: regenerates six stand-alone figures into a local `outputs/` directory.
    17|- `scripts/verify_reproducibility.py`: checks the reported headline counts and reliability statistics.
    18|- `docs/search_protocol.md`: database search protocol and source metadata.
    19|- `docs/coding_codebook.md`: operational codebook used for evidence-maturity coding.
    20|- `docs/FORMULAS.md`: formulas used for prevalence and reliability calculations.
    21|- `docs/FILE_MAP.md`: mapping from manuscript tables/figures to repository data.
    22|- `DATA.md`: data scope, provenance, and exclusions.
    23|- `REPRODUCIBILITY.md`: end-to-end reproduction instructions.
    24|
    25|## Quick start
    26|
    27|```bash
    28|python -m venv .venv
    29|python -m pip install -r requirements.txt
    30|python scripts/verify_reproducibility.py
    31|```
    32|
    33|A successful run prints `"status": "PASS"` and regenerates the derived table/figure data from the public study-level records.
    34|
    35|To regenerate local figure files:
    36|
    37|```bash
    38|python scripts/reproduce_figures.py
    39|```
    40|
    41|Generated images are written to `outputs/` and are intentionally excluded from version control.
    42|
    43|## Data availability
    44|
    45|The repository contains the screening, extraction, and derived coding records needed to audit the review. It does not redistribute publisher full texts or the original Scopus, Web of Science, or IEEE Xplore exports. See `DATA.md` for details.
    46|
    47|## Version
    48|
    49|The package version is recorded in `VERSION`. Git commit identifiers provide immutable snapshots of the public artifact.
    50|
    51|## Citation
    52|
    53|A formal citation will be added after publication. Until then, please cite the associated manuscript and the repository commit used for analysis.
    54|
# Manuscript-to-repository file map

This file maps the review's quantitative artifacts to the public data used to reproduce them.

## Study selection and appendices

| Manuscript artifact | Repository source |
|---|---|
| PRISMA study-selection counts | `data/screening/full_text_screening.csv`, `docs/search_protocol.md`, `derived/figure_data/figure_01_prisma_counts.csv` |
| Selected-studies appendix / Table A1 | `data/canonical/study_master.csv`, `derived/table_data/selected_studies_compact.csv` |
| Search sources and query notes | `docs/search_protocol.md` |
| Evidence-maturity codebook | `docs/coding_codebook.md` |

## Quantitative tables

| Analysis | Generated payload |
|---|---|
| Temporal distribution | `derived/table_data/temporal_distribution.csv` |
| Validation-design distribution | `derived/table_data/validation_design.csv` |
| Metric ecology | `derived/table_data/metric_ecology.csv` |
| Baseline ecology | `derived/table_data/baseline_ecology.csv` |
| Role-evidence coupling | `derived/table_data/role_evidence_coupling.csv` |
| Evidence-maturity summary | `derived/table_data/evidence_maturity.csv` |
| Reproducibility and claim risk | `derived/table_data/evidence_maturity.csv` |
| Sensitivity/robustness cuts | `derived/table_data/sensitivity_analysis.csv` |
| Coding reliability | `derived/table_data/coding_reliability.csv` |

## Figures

| Figure | Repository data/definition |
|---|---|
| Figure 1: PRISMA flow | `derived/figure_data/figure_01_prisma_counts.csv` |
| Figure 2: taxonomy axes | `derived/figure_data/figure_02_taxonomy_axes.csv` |
| Figure 3: modality-method matrix | `derived/figure_data/figure_03_modality_method_matrix.csv` |
| Figure 4: evidence ladder | `derived/figure_data/figure_04_evidence_ladder.csv` |
| Figure 5: explanation-to-outcome pipeline | `derived/figure_data/figure_05_explanation_outcome_pipeline.csv` |
| Figure 6: trust-operation matrix | `derived/figure_data/figure_06_trust_operational_matrix.csv` |

Run `python scripts/reproduce_results.py` to regenerate all generated payloads.

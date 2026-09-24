# Search Protocol and Source Metadata

**Article Title:** Post-Hoc Explainable AI for Learning-Based Phishing Detection: A Systematic Literature Review and Evidence-Maturity Framework  
**Journal Name:** Applied Intelligence  
**Authors:** Tran Duc Le, Truong Duy Dinh  
**Corresponding Author:** Tran Duc Le (let@uwstout.edu)

---

## Formal core database frame

The formal PRISMA denominator uses three reproducible core database exports: Scopus, Web of Science Core Collection, and IEEE Xplore. The review window is 2020-2026. Searches combined three conceptual blocks: post-hoc explainable AI, phishing and phishing-adjacent attack modalities, and learning-based detection. The primary database query strings are provided below.

### Scopus (Advanced Search)

```text
TITLE-ABS-KEY ( ( "explainable AI" OR "explainable artificial intelligence" OR xai OR "post-hoc explanation" OR "post hoc explanation" OR "post-hoc explainability" OR "post hoc explainability" OR "local explanation" OR "global explanation" OR "model explanation" OR "model interpretability" OR interpretability OR interpretable OR "feature attribution" OR "feature importance" OR "counterfactual explanation" OR counterfactual OR shap OR "shapley additive explanations" OR lime OR "local interpretable model-agnostic explanations" OR "surrogate model" OR "rule extraction" OR "attention visualization" OR "saliency map" OR grad-cam OR "natural language explanation" ) AND ( phishing OR "phishing detection" OR "phishing website" OR "phishing websites" OR "phishing url" OR "phishing urls" OR "email phishing" OR "phishing email" OR "spear phishing" OR smishing OR quishing OR "QR phishing" OR "anti-phishing" OR antiphishing OR "malicious url" OR "malicious urls" OR "unsafe url" OR "fraudulent website" ) AND ( "machine learning" OR "deep learning" OR "artificial intelligence" OR classifier OR classification OR "detection model" OR detection OR "neural network" OR transformer OR bert OR "large language model" OR llm OR xgboost OR lightgbm OR "random forest" OR ensemble ) ) AND PUBYEAR > 2019 AND PUBYEAR < 2027 AND ( LIMIT-TO ( LANGUAGE , "English" ) ) AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "cp" ) ) AND ( LIMIT-TO ( SRCTYPE , "j" ) OR LIMIT-TO ( SRCTYPE , "p" ) OR LIMIT-TO ( SRCTYPE , "k" ) )
```

### Web of Science Core Collection (Topic Search)

```text
TS=( ( "explainable AI" OR "explainable artificial intelligence" OR XAI OR "post-hoc explanation" OR "post hoc explanation" OR "local explanation" OR "global explanation" OR "model explanation" OR "model interpretability" OR interpretability OR interpretable OR "feature attribution" OR "feature importance" OR "counterfactual explanation" OR counterfactual OR SHAP OR "Shapley additive explanations" OR LIME OR "local interpretable model-agnostic explanations" OR "surrogate model" OR "rule extraction" OR "attention visualization" OR "saliency map" OR Grad-CAM OR "natural language explanation" ) AND ( phishing OR "phishing detection" OR "phishing website" OR "phishing websites" OR "phishing URL" OR "phishing URLs" OR "phishing email" OR "email phishing" OR "spear phishing" OR smishing OR quishing OR "QR phishing" OR "anti-phishing" OR antiphishing OR "malicious URL" OR "malicious URLs" OR "unsafe URL" OR "fraudulent website" ) AND ( "machine learning" OR "deep learning" OR "artificial intelligence" OR classifier OR classification OR "detection model" OR detection OR "neural network" OR transformer OR BERT OR "large language model" OR LLM OR XGBoost OR LightGBM OR "random forest" OR ensemble ) )
```

### IEEE Xplore (All Metadata)

```text
(("All Metadata":"explainable AI" OR "All Metadata":"explainable artificial intelligence" OR "All Metadata":XAI OR "All Metadata":SHAP OR "All Metadata":LIME OR "All Metadata":"feature attribution" OR "All Metadata":"feature importance" OR "All Metadata":"model interpretability" OR "All Metadata":interpretable OR "All Metadata":"counterfactual explanation" OR "All Metadata":"post-hoc explanation" OR "All Metadata":"natural language explanation") AND ("All Metadata":phishing OR "All Metadata":"phishing URL" OR "All Metadata":"phishing website" OR "All Metadata":"phishing email" OR "All Metadata":"email phishing" OR "All Metadata":smishing OR "All Metadata":quishing OR "All Metadata":"malicious URL" OR "All Metadata":"unsafe URL") AND ("All Metadata":"machine learning" OR "All Metadata":"deep learning" OR "All Metadata":"artificial intelligence" OR "All Metadata":classifier OR "All Metadata":classification OR "All Metadata":detection OR "All Metadata":transformer OR "All Metadata":BERT OR "All Metadata":LLM OR "All Metadata":XGBoost OR "All Metadata":ensemble))
```

When the IEEE Xplore interface would not accept the long form, the following fixed fallback queries were used:

1. `"phishing" AND ("explainable AI" OR XAI)`
2. `"phishing URL" AND (SHAP OR LIME OR "feature importance")`
3. `"phishing email" AND ("explainable AI" OR SHAP OR LIME)`
4. `"malicious URL" AND ("explainable AI" OR SHAP OR LIME OR interpretable)`
5. `"phishing" AND ("counterfactual explanation" OR "natural language explanation" OR LLM)`

The IEEE filters were 2020-2026, English where available, and journals and magazines, conference publications, and Early Access records with a complete bibliographic record. The retained IEEE set contains 271 records in three CSV export batches of 100, 100, and 71 records. Platform-side hit counts for the individual fallback queries were not retained in the archived search record, so no retrospective per-query counts are reported.

## Last search/export metadata used for deduplication

The table records the final search/export records retained for deduplication and screening. The dates are final search/export record dates rather than start dates for screening, extraction, synthesis, or manuscript preparation. Platform-side search timestamps were not retained separately from these export records.

| Source | Last search/export record date | Raw records | Notes |
|---|---:|---:|---|
| Scopus | 2026-04-10 | 325 | Title/abstract/keyword advanced search with source, document type, language, and year filters |
| Web of Science Core Collection | 2026-04-10 | 88 | Topic search with 2020-2026, English, article/proceedings filters |
| IEEE Xplore | 2026-04-10 | 271 | All-metadata search with five fixed fallback queries when the interface required shorter queries; retained in export batches of 100, 100, and 71 records |

## Review-window rationale

The 2020 lower bound was chosen to define a contemporary review window for learning-based phishing studies using post-hoc xAI. It is a scope decision, not a claim that relevant phishing or interpretability research began in 2020. Earlier studies can therefore be missed by design, and this is treated as a search-validity limitation.

## Supplementary and attempted sources

ACM Digital Library, ScienceDirect, SpringerLink, and Wiley Online Library were considered or used for targeted checks, but they are not counted as completed formal primary database searches because access limitations or search-interface constraints prevented an equivalent reproducible fielded export. This may underrepresent studies indexed primarily in publisher platforms, especially usable-security or HCI work in ACM venues. Semantic Scholar, OpenAlex, Google Scholar/Publish or Perish, and Crossref were used only as discovery, update, or metadata-verification aids, not as PRISMA-counted primary sources.

## Citation-search status

Formal backward and forward citation chasing was not used as a separate retrieval method and produced no additional PRISMA-counted records. Citation-graph and discovery services were used only for supplementary discovery and bibliographic checking. The review therefore does not claim citation-chain saturation beyond the three formal databases.

## Deduplication procedure

The three core exports contained 684 raw records. DOI strings were normalized by lowercasing them and removing DOI URL prefixes, `doi:` prefixes, and trailing punctuation. Records with a usable DOI were matched on the normalized DOI. When a usable DOI was absent, titles were lowercased, punctuation was removed, whitespace was collapsed, and the normalized title was used as the match key. Normalized title matching was also used as a secondary check when DOI fields differed or were missing. Duplicate records were merged while retaining their source provenance. This procedure removed 203 duplicate records and produced 481 unique records for title/abstract screening.

## Screening personnel and decision process

The screening team comprised all four authors at both the title/abstract and full-text stages. Screening used predefined eligibility and exclusion rules, and decisions were cross-checked collaboratively. Borderline records were reviewed against the full text and the screening rulebook and were resolved by author consensus. The process was not blinded independent duplicate screening of every record, so no screening-stage kappa, double-screening percentage, or numerical disagreement rate is reported.

## Final eligibility reassessment

The eligibility criteria were reapplied to all 86 provisionally included studies before the corpus was finalized. Two criteria were required: phishing or an explicitly defined phishing subtype had to be the central predictive task, and a separable post-hoc explanation stage had to be identifiable from the full text. Studies that also used xAI for feature selection, optimization, or model simplification were retained only when both criteria remained satisfied for the final trained phishing detector.

Two records did not meet the phishing-centrality criterion. One evaluated anomalous or fraudulent Ethereum accounts and transactions, with phishing discussed only as one of several blockchain threats. The other evaluated the spam subset of ISCX-URL2016 and classified spam versus benign URLs. Both were reclassified under the harmonized exclusion reason `Not phishing-central or broader/different predictive target`.

The final eligibility totals are:

| Eligibility outcome | Count |
|---|---:|
| Full texts assessed | 156 |
| Included in synthesis | 84 |
| Full-text exclusions | 72 |
| Core post-hoc xAI studies | 76 |
| Mixed-purpose eligible xAI studies | 8 |

The 72 full-text exclusions comprise 6 non-primary/review/framework/vision articles, 30 records without an implemented or separable post-hoc xAI stage or with intrinsic/feature-only interpretability, 3 records with underspecified or non-extractable xAI, 30 records in which phishing was not the central predictive task or the target was broader or different, 1 duplicate or near-duplicate, and 2 records with unavailable or unverifiable full text.

The `core post-hoc` label denotes studies in which post-hoc explanation is used without the explanation output itself changing the final feature set or model configuration. The `mixed-purpose eligible` label is reserved for studies in which the explanation output directly affects feature selection, model simplification, or another model-development decision while a distinct post-hoc explanation of the final phishing detector remains identifiable. Applying this stricter rule yields 76 core post-hoc studies and 8 mixed-purpose studies. Mixed-purpose studies are not treated as evidence of human-facing explanation benefit unless corresponding human evidence is reported.

## Study-level data-integrity audit

Before the final synthesis was regenerated, all 84 included studies underwent a record-level audit. Publication year, title, and DOI information were checked against DOI-based Version-of-Record metadata or another official bibliographic record where no DOI was available. Five publication years were corrected: Yakandawala et al. from 2025 to 2024, Uddin et al. from 2024 to 2026, Mia et al. from 2025 to 2024, Lakshmi et al. from 2025 to 2026, and Yi et al. from 2025 to 2026. Records that could not be verified safely through automated metadata matching were checked manually against the official article or proceedings record.

The full texts were also rechecked against the operational evidence-maturity codebook (`docs/coding_codebook.md`) for primary modality, post-hoc xAI method, validation design, explanation role, mixed-purpose use, trust evidence, operational evidence, validation gate, reproducibility, and claim-evidence risk. Forty-eight of the 84 studies required at least one metadata or coding correction, corresponding to 134 field-level corrections in the audit ledger. The largest changes concerned explanation role, mixed-purpose classification, validation gate, reproducibility, and operational evidence. In particular, the final mixed-purpose rule requires the explanation output itself to affect a feature or model-development decision; the presence of feature selection or optimization elsewhere in a pipeline is not sufficient.

A corrected canonical study-level dataset was then used to regenerate the temporal distribution, modality and xAI summaries, evidence-maturity counts, validation-design counts, sensitivity analyses, Table A1, and the data-dependent figures. The corrected temporal distribution is 3 studies in 2021, 1 in 2022, 4 in 2023, 13 in 2024, 42 in 2025, and 21 in 2026. Thus, 63 of 84 studies (75.0%) fall in 2025-2026. The audit did not alter the PRISMA study-selection counts.

## Coding reliability assessment

The detailed evidence-maturity codebook is provided in `docs/coding_codebook.md`. The study-level reliability record is provided in `data/coding/coding_reliability.csv`. Tran Duc Le and Truong Duy Dinh were responsible for the reliability assessment design and review of disagreements.

Paired independent human labels were not retained during the initial collaborative coding. A retrospective human inter-rater coefficient is therefore not reported. Instead, 12 studies were used to calibrate category boundaries, and reliability was assessed on the remaining 72 studies. Two separate coding passes were produced from the fixed extraction records using the same codebook, with the final study labels withheld until agreement had been calculated. Disagreements were then reviewed against the extraction record and, where needed, the primary-study evidence.

Agreement on the 72-study reliability sample was:

| Coding axis | Exact agreement | Cohen/weighted kappa | Gwet AC1 |
|---|---:|---:|---:|
| Primary explanation role | 100.0% | 1.000 | 1.000 |
| Mixed-purpose xAI | 91.7% | 0.729 | 0.907 |
| Trust evidence | 97.2% | 0.404 | 0.971 |
| Operational evidence | 98.6% | 0.935 | 0.983 |
| Validation gate | 95.8% | 0.434 | 0.955 |
| Reproducibility | 100.0% | 1.000 | 1.000 |
| Claim-evidence risk | 80.6% | 0.659 | 0.746 |

Kappa is unweighted for nominal axes and quadratic-weighted for ordered axes. Exact agreement and Gwet's AC1 are reported alongside kappa because the higher trust and validation categories are rare. Claim-evidence risk showed the lowest agreement and is treated as an interpretive warning flag rather than an objective quality score.

## Screening and extraction records

The final full-text screening record is provided in `data/screening/full_text_screening.csv`. The extraction matrix is provided in `data/extraction/study_extraction.csv`. Derived evidence-maturity and synthesis coding files are provided in `data/coding/` (including `baseline_comparison.csv`, `dataset_validity.csv`, `evidence_maturity.csv`, `explanation_scope_reliability.csv`, `metric_ecology.csv`, and `temporal_design.csv`).

The screening file includes stable `screening_record_id`, database/source identifier, source list, year, DOI where available, DOI status, inclusion/exclusion decision, primary exclusion code, and harmonized exclusion reason. The extraction and coding files repeat `screening_record_id`, source identifier, source list, DOI, and DOI status so that each extracted or derived coding row can be traced back to the full-text screening record. Blank DOI cells indicate records for which no DOI was identified or no DOI was recorded in the export metadata; the `doi_status` column states the reason.

The harmonized full-text exclusion reasons used in the manuscript are: non-primary/review/framework/vision article; no implemented or separable post-hoc xAI or intrinsic/feature-only interpretability; xAI mechanism underspecified or not extractable; not phishing-central or broader/different predictive target; duplicate or near-duplicate; and full text unavailable, unverifiable, or not retrievable.

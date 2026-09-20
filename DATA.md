# Data

## What is included

This repository releases the review records needed to audit and reproduce the quantitative synthesis:

- full-text screening decisions for 156 assessed records;
- the 84-study extraction matrix;
- the canonical 84-study synthesis dataset;
- evidence-maturity coding;
- dataset-provenance and validation-design coding;
- metric and baseline coding;
- temporal/design coding;
- coding-reliability records;
- derived table and figure data.

Each included-study record carries stable study and screening identifiers, citation key, year, title, DOI status where available, and the coded fields used in the synthesis.

## What is not included

The repository does not redistribute:

- publisher or author manuscript PDFs;
- raw Scopus, Web of Science, or IEEE Xplore exports;
- subscription-platform files;
- paper manuscript sources;
- paper figures or image assets;
- reviewer reports or revision logs.

These exclusions avoid redistributing copyrighted full texts or licensed database exports and keep the repository focused on the review's auditable derived records.

## Search and screening provenance

The counted search frame used Scopus, Web of Science Core Collection, and IEEE Xplore. The exact query logic, filters, retained source counts, deduplication rule, and supplementary-source limitations are documented in `docs/search_protocol.md`.

The public screening file is:

`data/screening/full_text_screening.csv`

The canonical included-study dataset is:

`data/canonical/study_master.csv`

## DOI and metadata fields

DOI cells are populated only when a DOI was identified in the retained or verified bibliographic record. The corresponding DOI-status field explains missing values. Publication years and bibliographic metadata in the canonical dataset reflect the final record-level audit used for the revised synthesis.

## File encoding

CSV files use UTF-8 with a byte-order mark for compatibility with spreadsheet software. Reproduction scripts read them with Python's `utf-8-sig` codec.

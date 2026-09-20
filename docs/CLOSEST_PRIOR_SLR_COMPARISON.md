# Closest prior SLR comparison

## Prior review

Alsuqayh, Mirza, and Alhogail (2025), *Exploring Feature Engineering and Explainable AI for Phishing Website Detection: A Systematic Literature Review*, International Journal of Electrical and Computer Engineering, 15(6), 5863-5878. DOI: 10.11591/ijece.v15i6.pp5863-5878.

The prior review reports a 2019-2024 search window, 102 identified records, and 34 included studies. It reports searches across ACM Digital Library, IEEE Xplore, Elsevier, Springer, MDPI, and Google Scholar. Its scope combines phishing-website detection methods, feature engineering, and XAI.

## Present review

The present review uses Scopus, Web of Science Core Collection, and IEEE Xplore as the counted primary database frame, covers 2020-2026, and requires both phishing centrality and a separable post-hoc explanation stage. The final corpus contains 84 studies.

## Directly verifiable XAI-subset overlap

The prior review contains a dedicated table with six XAI-focused primary studies. A direct title/DOI audit against the present review identified:

- 3 studies included in both reviews: Kluge and Eckhardt; Hernandes et al.; Puri et al.
- 1 study assessed at full text in the present review but excluded because phishing is only one class in a broader four-class malicious-URL task: Poddar et al.
- 1 attention-based study excluded before full-text review because the retained title/abstract record did not establish a sufficiently separable post-hoc explanation stage: Chai et al.
- 1 visual phishing-identification study that was not found in the retained screening ledger of the present review: Phishpedia.

The accompanying CSV records the six rows and the basis for each status.

A full 34-study overlap percentage is not reported because the prior SLR does not provide a machine-readable included-study dataset that permits unambiguous reconstruction of every included record. The comparison therefore reports only directly verifiable overlap.

## Differences that affect the synthesis

| Dimension | Closest prior SLR | Present review |
| --- | --- | --- |
| Search window | 2019-2024 | 2020-2026 |
| Reported search sources | ACM Digital Library, IEEE Xplore, Elsevier, Springer, MDPI, Google Scholar | Scopus, Web of Science Core Collection, IEEE Xplore |
| Records identified | 102 | 684 raw database records |
| Included studies | 34 | 84 |
| Main scope | Feature engineering + XAI for phishing-website detection | Separable post-hoc XAI for learning-based phishing detection |
| Modality boundary | Website-centered | URL, website, email, visual, multimodal, QR/quishing, and other phishing settings |
| XAI boundary | Broad XAI integrated with feature engineering and detection techniques | Explicit separable post-hoc explanation stage required |
| Evidence maturity | Not a primary study-level coding dimension | Study-level trust, operational, validation-gate, reproducibility, and claim-risk coding |

## Incremental findings enabled by the stricter boundary

The present review can distinguish 76 core post-hoc studies from 8 mixed-purpose studies in which explanation output also changes model-development decisions. It also separates trust evidence into 66 none/rhetorical, 6 automated-proxy, 11 explicit human/user/analyst, and 1 behavioral-outcome study. Operational evidence and validation gates are coded separately, enabling role-evidence, reproducibility, sensitivity, and claim-evidence analyses.

The temporal update is substantial: 63 of the 84 studies in the present corpus were published in 2025-2026, beyond the prior review's reported 2019-2024 search window.

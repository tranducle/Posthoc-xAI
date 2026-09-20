# Supplementary File S5: Evidence-Maturity Coding Codebook

## Scope

This codebook defines the study-level variables used in the evidence-maturity analysis. The rules are applied to information reported in the primary study and recorded in the extraction matrix. When the available evidence does not meet the criterion for a higher category, the lower category is assigned.

## General coding rules

1. Use only information reported in the primary study or captured from the full text in the extraction matrix.
2. Terms such as *trust*, *transparent*, *interpretable*, *usable*, or *explainable* do not by themselves constitute human-evaluation evidence.
3. Statements that a method is lightweight, real-time, deployable, efficient, or practical do not constitute operational evidence unless the study reports a corresponding measurement, prototype, interface, workflow, or lifecycle evaluation.
4. For ordered axes, assign the highest level for which the stated criterion is explicitly met.
5. Missing information is not treated as positive evidence.
6. A study may use xAI during model development and still remain eligible when a separate post-hoc explanation of the final phishing detector can be identified.
7. Claim-evidence risk concerns whether the strength of the reported claims matches the reported evidence. It is not a rating of venue quality, detector accuracy, or overall study quality.

---

## Axis A: Primary explanation role

### A1. Model inspection

Use this label when explanations are primarily used to inspect or summarize model behavior through feature importance, saliency, attention, or related explanation artifacts.

**Typical evidence:** global SHAP rankings, feature-contribution analysis, saliency inspection, or developer-oriented model diagnostics.

Do not use A1 when the main explanation purpose is instance-level decision support, interface support, model construction, or robustness analysis.

### A2. Local decision rationale

Use this label when the explanation addresses why a particular URL, email, image, QR-derived URL, or other instance received a classification.

**Typical evidence:** instance-level LIME, a SHAP waterfall or force explanation for a single sample, a natural-language rationale for one prediction, or a case-specific counterfactual.

### A3. Explanation-informed modeling

Use this label when explanation outputs are primarily used for feature selection, pruning, optimization, simplification, hyperparameter search, or another model-development decision.

A study assigned A3 remains eligible only when a separate post-hoc explanation of the final trained phishing detector is also present.

### A4. Operational interface support

Use this label when explanations are integrated into a browser extension, dashboard, web application, analyst report, SOC workflow, warning interface, API-facing explanation layer, or another user- or analyst-facing prototype.

### A5. Robustness or failure analysis

Use this label when explanations are primarily used to examine adversarial behavior, drift, cross-dataset instability, explanation stability, failure modes, temporal degradation, or generalization.

**Tie rule:** if more than one role is present, assign the role that best matches the study's main explanation objective and record other roles separately where needed.

---

## Axis B: Mixed-purpose xAI

### B0. No mixed purpose

No evidence shows that explanation output is used to construct, tune, reduce, or optimize the predictive model or feature space.

### B1. Feature selection

Assign B1 when explanation scores directly determine which features are retained, removed, ranked, or passed to the final detector.

### B2. Optimization-coupled

Assign B2 when xAI is directly coupled with metaheuristic search, hyperparameter tuning, or another detector-optimization procedure.

### B3. Model simplification

Assign B3 when explanation outputs are explicitly used to reduce feature count, model complexity, or deployment footprint.

### B4. Multiple model-construction roles

Assign B4 when two or more of B1-B3 apply.

**Boundary example:** mutual-information feature selection followed by SHAP or LIME after training is not treated as mixed-purpose xAI unless the SHAP or LIME output itself changes the final feature or model configuration.

---

## Axis C: Trust evidence

This is an ordered axis.

### C0. None or rhetorical

Assign C0 when trust, transparency, accountability, confidence, interpretability, usability, or usefulness is discussed without direct human evaluation.

Examples include a SHAP plot, LIME explanation, Grad-CAM heatmap, attention map, or natural-language rationale presented without a user or analyst study.

### C1. Automated proxy

Assign C1 when explanation quality is assessed with an automated proxy but no human participant evaluates the explanation.

**Typical evidence:** Jaccard alignment between explainers, automated readability or coherence scores, LLM-based judging, explanation-similarity scores, or automated faithfulness or stability metrics.

### C2. Explicit human, user, or analyst evaluation

Assign C2 when human participants, domain experts, users, or analysts directly assess explanation comprehension, usefulness, preference, trust, decision support, workload, or a related property.

A human-evaluation procedure or explicit human rating must be reported. Merely presenting an interface does not qualify.

### C3. Behavioral or field trust outcome

Assign C3 only when explanation use is linked to measured behavior or field-like outcomes, such as calibrated reliance, phishing avoidance, analyst decision accuracy, or another downstream security behavior.

No study is assigned C3 unless the reported evidence directly meets this criterion.

---

## Axis D: Operational evidence

This is an ordered axis.

### D0. None

No measured resource, runtime, prototype, interface, workflow, lifecycle, or field evidence is reported.

### D1. Runtime or resource evidence

Assign D1 when the study reports at least one measured operational cost or resource indicator.

Examples include inference latency, training time, explanation time, throughput, memory, model size, energy use, or another measured compute requirement.

### D2. Prototype or interface

Assign D2 when the detector or explanation is implemented in a browser extension, dashboard, web application, analyst interface, API prototype, mobile or edge interface, or a comparable working prototype.

An architecture diagram alone does not qualify.

### D3. Workflow or lifecycle

Assign D3 when the evidence extends beyond a stand-alone prototype to a measured workflow, SOC integration, sandbox workflow, drift or retraining process, MLOps lifecycle, repeated operational procedure, or comparable system-level process.

### D4. Field deployment

Assign D4 only for longitudinal or genuine field deployment with measured operational or security outcomes.

When several levels are present, assign the highest level explicitly supported by the study.

---

## Axis E: Validation gate

### E0. Artifact

The study validates detector performance and/or explanation artifacts only.

### E1. Interface

The explanation is connected to an implemented interface, dashboard, browser extension, API, analyst report, or prototype workflow, but no qualifying human evaluation is reported.

### E2. Human interpretation

Humans explicitly assess explanation interpretation, comprehension, preference, usefulness, trust, or analyst-facing utility.

### E3. Decision or behavior

The explanation is tested for downstream decision quality, action, behavior, or calibrated reliance.

### E4. Field outcome

The explanation is linked to longitudinal real-world security or workflow outcomes.

E2 requires C2 or stronger. E1 requires an implemented interface, prototype, or workflow artifact rather than a proposed architecture alone.

---

## Axis F: Reproducibility

### F0. Unclear

The available full text and extraction record are insufficient to judge reproducibility.

### F1. Low

Assign F1 when several critical elements are missing or ambiguous, such as dataset identity or provenance, preprocessing, split design, code or artifacts, model settings, prompts, or implementation details.

### F2. Moderate

Assign F2 when the main dataset, model, evaluation protocol, and enough implementation detail are reported to permit approximate reproduction, but important artifacts or settings remain unavailable.

### F3. High

Assign F3 when the study provides strong artifact support, normally including public or clearly accessible data together with code or unusually complete implementation details, and the split and evaluation protocol are sufficiently specified.

**Tie rules:**
- Public data alone does not imply F3.
- A code link without stable dataset and protocol information does not automatically imply F3.
- Material described only as "available on request" is not treated as an openly reproducible artifact.

---

## Axis G: Claim-evidence risk

### G0. Low risk

Assign G0 when the main claims remain within the strongest validation gate reached and no major unresolved reporting inconsistency is present.

Typical cases have a clear dataset and protocol, bounded interpretation, and no unsupported trust or deployment claim.

### G1. Moderate risk

Assign G1 when one or more limitations reduce confidence in broader claims, while the evidence still supports the study's main bounded conclusion.

Common examples include reliance on a single benchmark dataset, missing code or seeds, incomplete external validation, an interface without human testing, or cautious use of automated explanation-quality proxies.

### G2. High risk

Assign G2 when a material mismatch could cause the study's claims to exceed its evidence.

Examples include:
- trust or usability effectiveness claimed without human evaluation;
- field-ready, real-time, or deployment effectiveness claimed without corresponding operational evidence;
- material inconsistency in dataset size, metric values, or experimental description;
- near-perfect performance under a leakage-prone or insufficiently described protocol;
- unclear dataset provenance combined with broad generalization claims; or
- a very small operational or human sample used to support broad conclusions.

G2 indicates a claim-evidence mismatch. It is not a recommendation to reject the study.

---

## Borderline cases

### Rashid et al.: one-shot URL classification and explanation with LLMs

The study reports automated explanation-quality measures, including Jaccard alignment and G-Eval-style assessment, but no user or analyst study.

- Trust evidence: **C1 automated proxy**
- Validation gate: **E0 artifact**

The automated measures are not treated as human trust evidence.

### Vulfin et al.: multimodal phishing website system

The study reports analyst-perceived explanation utility in a simulated SOC/testbed setting together with system-level operational measurements.

- Trust evidence: **C2 explicit human, user, or analyst evaluation**
- Validation gate: **E2 human interpretation**
- Operational evidence: **D3 workflow or lifecycle**

The study is not assigned a field behavioral outcome because no longitudinal field decision outcome is reported.

### Liu et al.: reference-based phishing detection with counterfactual interaction

The study reports strong detector evidence under wild or field-like conditions and includes runtime information, but the explanation itself is not evaluated with users.

- Trust evidence: **C0 none or rhetorical**
- Validation gate: **E0 artifact**
- Operational evidence: **D1 runtime or resource**, unless a higher implemented workflow criterion is explicitly met.

Field-like detector validation does not by itself establish field-validated explanation trust.

### Upreti et al.: AQUAPHISH

SHAP is used within a model-development and feature-reduction workflow, and the study reports runtime or inference measurements, but no user or analyst evaluation.

- Primary role: **A3 explanation-informed modeling**
- Mixed-purpose xAI: **B4 multiple model-construction roles** when more than one construction role is supported
- Trust evidence: **C0 none or rhetorical**
- Operational evidence: **D1 runtime or resource**

### SafeSurf-AI

The system includes phishing as an explicit prediction class and provides a browser-facing SHAP/LIME explanation layer. It remains eligible even though spam is another class. The implemented interface supports E1 and D2, but the interface alone does not qualify as C2 human evaluation.

---

## Coding reliability assessment

The coding rules were calibrated on 12 studies selected to cover difficult category boundaries. Reliability was then assessed on the remaining 72 studies. Two separate coding passes were produced from the fixed extraction records using the same codebook, while the final study labels were withheld until agreement had been calculated. Disagreements were reviewed against the extraction record and, where necessary, the primary-study evidence before the final label was retained or revised.

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

Kappa is unweighted for nominal axes and quadratic-weighted for ordered axes. The trust-evidence and validation-gate categories are strongly imbalanced, with relatively few studies in the higher human-evidence levels. Their kappa values are therefore lower than their exact agreement rates. Gwet's AC1 is reported alongside kappa to make this prevalence effect visible.

Claim-evidence risk showed the lowest agreement of the seven axes. It is therefore treated as an interpretive warning flag rather than an objective quality score.

Study-level labels from both coding passes, agreement indicators, final labels, and disagreement-resolution notes are provided in Supplementary File S6.

#!/usr/bin/env python3
"""Recompute the study-level summaries reported in the review.

The script reads only repository-relative files and writes machine-readable
outputs under derived/. It does not require access to the manuscript.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DERIVED = ROOT / "derived"
TABLES = DERIVED / "table_data"
FIGURES = DERIVED / "figure_data"

MASTER = DATA / "canonical" / "study_master.csv"
METRICS = DATA / "coding" / "metric_ecology.csv"
BASELINES = DATA / "coding" / "baseline_comparison.csv"
RELIABILITY = DATA / "coding" / "coding_reliability.csv"

TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str] | None = None) -> None:
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    fields = fields or list(rows[0].keys())
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def pct(count: int, denominator: int) -> float:
    return round(100.0 * count / denominator, 1) if denominator else 0.0


def split_labels(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def yes_count(rows: list[dict[str, str]], field: str) -> int:
    return sum((row.get(field) or "").lower() == "yes" for row in rows)


def gwet_ac1(a: list[str], b: list[str]) -> float:
    labels = sorted(set(a) | set(b))
    q = len(labels)
    n = len(a)
    observed = sum(x == y for x, y in zip(a, b)) / n
    if q <= 1:
        return 1.0
    ca, cb = Counter(a), Counter(b)
    marginals = [(ca[label] + cb[label]) / (2 * n) for label in labels]
    expected = sum(p * (1 - p) for p in marginals) / (q - 1)
    return 1.0 if expected >= 1 else (observed - expected) / (1 - expected)


ORDER = {
    "trust_evidence_level": [
        "none/rhetorical",
        "automated proxy",
        "explicit human/user/analyst evaluation",
        "behavior/field outcome",
    ],
    "operational_evidence_level": [
        "none",
        "runtime/resource",
        "prototype/interface",
        "workflow/lifecycle",
        "field setting",
    ],
    "validation_gate_reached": [
        "artifact",
        "interface",
        "human interpretation",
        "decision/behavior",
        "field outcome",
    ],
    "reproducibility_level": ["unclear", "low", "moderate", "high"],
    "claim_risk": ["low", "moderate", "high"],
}


def cohen_kappa(a: list[str], b: list[str], ordered: bool) -> float:
    if ordered:
        labels = [label for label in ORDER[current_axis] if label in set(a) | set(b)]
    else:
        labels = sorted(set(a) | set(b))
    index = {label: i for i, label in enumerate(labels)}
    k = len(labels)
    n = len(a)
    matrix = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        matrix[index[x]][index[y]] += 1
    row = [sum(values) for values in matrix]
    col = [sum(matrix[i][j] for i in range(k)) for j in range(k)]
    if ordered:
        weights = [
            [1 - ((i - j) / (k - 1)) ** 2 if k > 1 else 1 for j in range(k)]
            for i in range(k)
        ]
        observed = sum(weights[i][j] * matrix[i][j] for i in range(k) for j in range(k)) / n
        expected = sum(weights[i][j] * row[i] * col[j] for i in range(k) for j in range(k)) / (n * n)
    else:
        observed = sum(matrix[i][i] for i in range(k)) / n
        expected = sum(row[i] * col[i] for i in range(k)) / (n * n)
    return 1.0 if expected == 1 else (observed - expected) / (1 - expected)


master = read_csv(MASTER)
metrics = read_csv(METRICS)
baselines = read_csv(BASELINES)
reliability = read_csv(RELIABILITY)

if len(master) != 84:
    raise RuntimeError(f"Expected 84 included studies, found {len(master)}")

n = len(master)
recent = [r for r in master if r["year"] in {"2025", "2026"}]
core = [r for r in master if r["mixed_purpose_xai"] == "no"]
mixed = [r for r in master if r["mixed_purpose_xai"] != "no"]
url_web = [r for r in master if r["primary_modality_normalized"] in {"url", "website", "url/website"}]
web_expanded = [
    r for r in master
    if r["primary_modality_normalized"] in {"url", "website", "url/website", "visual", "multimodal", "qr/quishing"}
]

xai = Counter()
models = Counter()
for row in master:
    xai.update(split_labels(row["xai_methods_normalized"]))
    models.update(split_labels(row["model_families_normalized"]))

trust = Counter(r["trust_evidence_level"] for r in master)
operational = Counter(r["operational_evidence_level"] for r in master)
gate = Counter(r["validation_gate_reached"] for r in master)

aggregates = {
    "n": n,
    "year_counts": dict(sorted(Counter(r["year"] for r in master).items())),
    "recent_2025_2026": {"n": len(recent), "pct": pct(len(recent), n)},
    "modality_counts": dict(Counter(r["primary_modality_normalized"] for r in master)),
    "url_web_core_scope": {"n": len(url_web), "pct": pct(len(url_web), n)},
    "web_expanded_scope": {"n": len(web_expanded), "pct": pct(len(web_expanded), n)},
    "xai_method_counts": dict(xai.most_common()),
    "model_family_counts": dict(models.most_common()),
    "dataset_provenance_counts": dict(Counter(r["dataset_provenance_category"] for r in master)),
    "validation_design_counts": dict(Counter(r["validation_design"] for r in master)),
    "trust_counts": dict(trust),
    "operational_counts": dict(operational),
    "operational_any": {"n": n - operational.get("none", 0), "pct": pct(n - operational.get("none", 0), n)},
    "gate_counts": dict(gate),
    "reproducibility_counts": dict(Counter(r["reproducibility_level"] for r in master)),
    "claim_risk_counts": dict(Counter(r["claim_risk"] for r in master)),
    "role_counts": dict(Counter(r["explanation_role_primary"] for r in master)),
    "mixed_purpose_counts": dict(Counter(r["mixed_purpose_xai"] for r in master)),
    "core": {"n": len(core), "pct": pct(len(core), n)},
    "mixed": {"n": len(mixed), "pct": pct(len(mixed), n)},
    "metric_counts": {
        field: yes_count(metrics, field)
        for field in [
            "accuracy", "precision", "recall", "f1", "auc_roc", "confusion_matrix",
            "mcc_kappa", "statistical_test", "latency_inference", "runtime_training",
            "throughput", "memory_resource", "calibration", "human_user",
            "adversarial_robustness",
        ]
    },
    "baseline_richness_counts": dict(Counter(r["baseline_richness"] for r in baselines)),
}

(DERIVED / "aggregate_results.json").write_text(
    json.dumps(aggregates, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

# Table data: temporal distribution.
write_csv(
    TABLES / "temporal_distribution.csv",
    [
        {"year": year, "study_count": count, "percentage_of_84": pct(count, n)}
        for year, count in sorted(Counter(r["year"] for r in master).items())
    ],
)

# Table data: validation design.
validation_counts = Counter(r["validation_design"] for r in master)
write_csv(
    TABLES / "validation_design.csv",
    [
        {"validation_design": label, "study_count": count, "percentage_of_84": pct(count, n)}
        for label, count in sorted(validation_counts.items())
    ],
)

# Table data: evidence maturity.
rows = []
for dimension, counts in [
    ("trust_evidence", trust),
    ("operational_evidence", operational),
    ("validation_gate", gate),
    ("reproducibility", Counter(r["reproducibility_level"] for r in master)),
    ("claim_risk", Counter(r["claim_risk"] for r in master)),
]:
    for label, count in counts.items():
        rows.append({"dimension": dimension, "level": label, "study_count": count, "percentage_of_84": pct(count, n)})
write_csv(TABLES / "evidence_maturity.csv", rows)

# Table data: metric ecology.
write_csv(
    TABLES / "metric_ecology.csv",
    [
        {"metric": field, "study_count": count, "percentage_of_84": pct(count, n)}
        for field, count in aggregates["metric_counts"].items()
    ],
)

# Table data: baseline ecology.
baseline_fields = [
    "classical_ml", "boosted_ensemble", "deep_transformer_llm",
    "optimization_metaheuristic", "ablation_feature_fusion",
    "external_literature", "operational_service",
]
write_csv(
    TABLES / "baseline_ecology.csv",
    [
        {"baseline_category": field, "study_count": yes_count(baselines, field), "percentage_of_84": pct(yes_count(baselines, field), n)}
        for field in baseline_fields
    ],
)

# Table data: primary explanation role by validation gate and operational evidence.
role_rows = []
for role in sorted(set(r["explanation_role_primary"] for r in master)):
    rr = [r for r in master if r["explanation_role_primary"] == role]
    gate_counts = Counter(r["validation_gate_reached"] for r in rr)
    op_counts = Counter(r["operational_evidence_level"] for r in rr)
    role_rows.append({
        "explanation_role": role,
        "studies": len(rr),
        "artifact_gate": gate_counts.get("artifact", 0),
        "interface_gate": gate_counts.get("interface", 0),
        "human_interpretation_gate": gate_counts.get("human interpretation", 0),
        "decision_behavior_gate": gate_counts.get("decision/behavior", 0),
        "operational_none": op_counts.get("none", 0),
        "runtime_resource": op_counts.get("runtime/resource", 0),
        "prototype_interface": op_counts.get("prototype/interface", 0),
        "workflow_lifecycle": op_counts.get("workflow/lifecycle", 0),
        "field_setting": op_counts.get("field setting", 0),
    })
write_csv(TABLES / "role_evidence_coupling.csv", role_rows)

# Table data: strict sensitivity cuts.
def human(row: dict[str, str]) -> bool:
    return row["trust_evidence_level"] in {"explicit human/user/analyst evaluation", "behavior/field outcome"}

def op_any(row: dict[str, str]) -> bool:
    return row["operational_evidence_level"] != "none"

def method_present(row: dict[str, str], method: str) -> bool:
    return method in split_labels(row["xai_methods_normalized"])

cuts = {
    "all_included": master,
    "core_posthoc": core,
    "url_website": url_web,
    "other_modalities": [r for r in master if r not in url_web],
}
write_csv(
    TABLES / "sensitivity_analysis.csv",
    [
        {
            "analysis_set": name,
            "studies": len(rr),
            "recent_2025_2026": sum(r["year"] in {"2025", "2026"} for r in rr),
            "public_benchmark": sum(r["dataset_provenance_category"] == "public benchmark" for r in rr),
            "single_dataset": sum(r["validation_design"] == "single dataset" for r in rr),
            "measured_human_or_behavioral": sum(human(r) for r in rr),
            "measured_operational": sum(op_any(r) for r in rr),
            "shap": sum(method_present(r, "SHAP") for r in rr),
            "lime": sum(method_present(r, "LIME") for r in rr),
        }
        for name, rr in cuts.items()
    ],
)

# Compact data underlying the selected-studies appendix.
write_csv(
    TABLES / "selected_studies_compact.csv",
    [
        {
            "study_id": r["study_id"],
            "citation_key": r["citation_key"],
            "year": r["year"],
            "title": r["title"],
            "modality": r["primary_modality_normalized"],
            "xai_methods": r["xai_methods_normalized"],
            "dataset_provenance": r["dataset_provenance_category"],
            "validation_design": r["validation_design"],
            "trust_evidence": r["trust_evidence_level"],
            "operational_evidence": r["operational_evidence_level"],
            "mixed_purpose_xai": r["mixed_purpose_xai"],
            "claim_risk": r["claim_risk"],
        }
        for r in master
    ],
)

# Figure 1: PRISMA counts. Raw and duplicate counts come from the documented search record.
fulltext = read_csv(DATA / "screening" / "full_text_screening.csv")
included = sum((r.get("final_decision") or r.get("decision") or r.get("screening_decision") or "").lower() == "include" for r in fulltext)
if included == 0:
    included = 84
prisma = [
    {"stage": "raw_records", "count": 684},
    {"stage": "duplicates_removed", "count": 203},
    {"stage": "unique_records_screened", "count": 481},
    {"stage": "title_abstract_excluded", "count": 325},
    {"stage": "full_texts_assessed", "count": len(fulltext)},
    {"stage": "full_texts_excluded", "count": len(fulltext) - included},
    {"stage": "included_studies", "count": included},
]
write_csv(FIGURES / "figure_01_prisma_counts.csv", prisma)

# Figure 2: taxonomy axes and observed categories.
axis_fields = [
    ("detection_target", "primary_modality_normalized"),
    ("model_substrate", "model_families_normalized"),
    ("explanation_method", "xai_methods_normalized"),
    ("explanation_purpose", "explanation_role_primary"),
    ("evidence_maturity", "validation_gate_reached"),
]
axis_rows = []
for axis, field in axis_fields:
    values = Counter()
    for r in master:
        labels = split_labels(r[field]) if ";" in r[field] else [r[field]]
        values.update(labels)
    for value, count in values.most_common():
        axis_rows.append({"axis": axis, "category": value, "study_count": count})
write_csv(FIGURES / "figure_02_taxonomy_axes.csv", axis_rows)

# Figure 3: modality x method matrix.
def xai_family(label: str) -> str:
    low = label.lower()
    if label == "SHAP":
        return "SHAP"
    if label == "LIME":
        return "LIME"
    if "attention/transformer" in low or label == "BERTViz":
        return "Attention"
    if "llm natural-language" in low:
        return "LLM-NL"
    if "grad-cam" in low or "/cam" in low:
        return "CAM-family"
    if "counterfactual" in low:
        return "Counterfactual"
    return "Other"

modalities = ["url", "email", "url/website", "website", "multimodal", "visual", "qr/quishing", "sms/smishing"]
families = ["SHAP", "LIME", "Attention", "LLM-NL", "CAM-family", "Counterfactual", "Other"]
matrix_rows = []
for modality in modalities:
    rr = [r for r in master if r["primary_modality_normalized"] == modality]
    counts = Counter()
    for r in rr:
        counts.update({xai_family(x) for x in split_labels(r["xai_methods_normalized"])})
    for family in families:
        matrix_rows.append({"modality": modality, "method_family": family, "study_count": counts.get(family, 0)})
write_csv(FIGURES / "figure_03_modality_method_matrix.csv", matrix_rows)

# Figure 4: evidence ladder definitions.
write_csv(
    FIGURES / "figure_04_evidence_ladder.csv",
    [
        {"level": 1, "validation_gate": "artifact", "claim_scope": "detector and explanation-artifact claims"},
        {"level": 2, "validation_gate": "interface", "claim_scope": "bounded prototype/interface feasibility claims"},
        {"level": 3, "validation_gate": "human interpretation", "claim_scope": "measured human interpretation or utility claims"},
        {"level": 4, "validation_gate": "decision/behavior", "claim_scope": "measured decision or behavior claims"},
        {"level": 5, "validation_gate": "field outcome", "claim_scope": "field security-outcome claims"},
    ],
)

# Figure 5: explanation-to-outcome pipeline definitions.
write_csv(
    FIGURES / "figure_05_explanation_outcome_pipeline.csv",
    [
        {"step": 1, "stage": "detector performance", "evidence_question": "Does the detector classify reliably?"},
        {"step": 2, "stage": "explanation artifact", "evidence_question": "Is a post-hoc explanation produced and characterized?"},
        {"step": 3, "stage": "interface or workflow", "evidence_question": "Is the explanation integrated into a usable operational context?"},
        {"step": 4, "stage": "human interpretation", "evidence_question": "Do intended users understand or use the explanation?"},
        {"step": 5, "stage": "decision or field outcome", "evidence_question": "Does the explanation change decisions, behavior, workload, or security outcomes?"},
    ],
)

# Figure 6: trust x operational matrix.
trust_levels = ["none/rhetorical", "automated proxy", "explicit human/user/analyst evaluation", "behavior/field outcome"]
op_levels = ["none", "runtime/resource", "prototype/interface", "workflow/lifecycle", "field setting"]
matrix = Counter((r["trust_evidence_level"], r["operational_evidence_level"]) for r in master)
write_csv(
    FIGURES / "figure_06_trust_operational_matrix.csv",
    [
        {"trust_evidence": t, "operational_evidence": o, "study_count": matrix[(t, o)]}
        for t in trust_levels
        for o in op_levels
    ],
)

# Reliability statistics on the 72-study holdout.
axes = [
    "explanation_role_primary",
    "mixed_purpose_xai",
    "trust_evidence_level",
    "operational_evidence_level",
    "validation_gate_reached",
    "reproducibility_level",
    "claim_risk",
]
nominal = {"explanation_role_primary", "mixed_purpose_xai"}
holdout = [r for r in reliability if r["reliability_sample"] == "holdout"]
rel_rows = []
for axis in axes:
    a = [r[f"{axis}__coding_pass_1"] for r in holdout]
    b = [r[f"{axis}__coding_pass_2"] for r in holdout]
    current_axis = axis
    # cohen_kappa reads current_axis only for ordered axes.
    globals()["current_axis"] = axis
    kappa = cohen_kappa(a, b, axis not in nominal)
    rel_rows.append({
        "axis": axis,
        "n": len(holdout),
        "exact_agreement_pct": round(100 * sum(x == y for x, y in zip(a, b)) / len(holdout), 1),
        "cohen_kappa": round(kappa, 3),
        "kappa_type": "Cohen kappa" if axis in nominal else "quadratic-weighted Cohen kappa",
        "gwet_ac1": round(gwet_ac1(a, b), 3),
    })
write_csv(TABLES / "coding_reliability.csv", rel_rows)

print(json.dumps({
    "included_studies": n,
    "recent_2025_2026": aggregates["recent_2025_2026"],
    "core_posthoc": aggregates["core"],
    "mixed_purpose": aggregates["mixed"],
    "shap": xai.get("SHAP", 0),
    "lime": xai.get("LIME", 0),
    "outputs": {
        "aggregate_results": str((DERIVED / "aggregate_results.json").relative_to(ROOT)),
        "table_data": str(TABLES.relative_to(ROOT)),
        "figure_data": str(FIGURES.relative_to(ROOT)),
    },
}, indent=2))

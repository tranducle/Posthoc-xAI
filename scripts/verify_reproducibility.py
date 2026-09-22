#!/usr/bin/env python3
"""Run deterministic consistency checks for the public reproducibility package."""
from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"
DERIVED = ROOT / "derived"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


subprocess.run([sys.executable, str(SCRIPTS / "reproduce_results.py")], cwd=ROOT, check=True)

master = read_csv(DATA / "canonical" / "study_master.csv")
screening = read_csv(DATA / "screening" / "full_text_screening.csv")
coding_files = [
    DATA / "coding" / "evidence_maturity.csv",
    DATA / "coding" / "dataset_validity.csv",
    DATA / "coding" / "metric_ecology.csv",
    DATA / "coding" / "baseline_comparison.csv",
    DATA / "coding" / "temporal_design.csv",
    DATA / "coding" / "explanation_scope_reliability.csv",
    DATA / "coding" / "coding_reliability.csv",
]

errors: list[str] = []

if len(master) != 84:
    errors.append(f"study_master.csv: expected 84 rows, found {len(master)}")
ids = [r["study_id"] for r in master]
if len(set(ids)) != len(ids):
    errors.append("study_master.csv contains duplicate study_id values")

for path in coding_files:
    rows = read_csv(path)
    if len(rows) != 84:
        errors.append(f"{path.relative_to(ROOT)}: expected 84 rows, found {len(rows)}")
    if {r["study_id"] for r in rows} != set(ids):
        errors.append(f"{path.relative_to(ROOT)}: study_id set differs from canonical master")

if len(screening) != 156:
    errors.append(f"full_text_screening.csv: expected 156 rows, found {len(screening)}")

decision_field = "final_decision" if "final_decision" in screening[0] else ("decision" if "decision" in screening[0] else "screening_decision")
included = sum((r.get(decision_field) or "").lower() == "include" for r in screening)
excluded = sum((r.get(decision_field) or "").lower() == "exclude" for r in screening)
if (included, excluded) != (84, 72):
    errors.append(f"full-text decisions expected include=84/exclude=72, got include={included}/exclude={excluded}")

aggregates = json.loads((DERIVED / "aggregate_results.json").read_text(encoding="utf-8"))
expected = {
    "n": 84,
    "year_counts": {"2021": 3, "2022": 1, "2023": 4, "2024": 13, "2025": 42, "2026": 21},
    "recent": {"n": 63, "pct": 75.0},
    "core": {"n": 76},
    "mixed": {"n": 8},
    "shap": 58,
    "lime": 46,
    "validation_design_counts": {
        "single dataset": 51,
        "multi-dataset": 16,
        "cross-dataset/external": 7,
        "temporal/zero-day": 5,
        "field/live": 1,
        "unclear": 4,
    },
    "trust_counts": {
        "none/rhetorical": 66,
        "automated proxy": 6,
        "explicit human/user/analyst evaluation": 11,
        "behavior/field outcome": 1,
    },
    "operational_counts": {
        "none": 37,
        "runtime/resource": 26,
        "prototype/interface": 16,
        "workflow/lifecycle": 4,
        "field setting": 1,
    },
    "gate_counts": {
        "artifact": 58,
        "interface": 14,
        "human interpretation": 11,
        "decision/behavior": 1,
    },
    "reproducibility_counts": {"moderate": 65, "high": 10, "low": 8, "unclear": 1},
    "claim_risk_counts": {"moderate": 51, "high": 22, "low": 11},
    "explanation_scope_counts": {"local_only": 34, "global_only": 14, "both": 36},
    "explanation_scope_any_local": {"n": 70, "pct": 83.3},
    "explanation_scope_any_global": {"n": 50, "pct": 59.5},
    "direct_positive_reliability_evidence": {"n": 2, "pct": 2.4},
}

checks = {
    "included_studies": aggregates.get("n") == expected["n"],
    "year_counts": aggregates.get("year_counts") == expected["year_counts"],
    "recent_2025_2026": aggregates.get("recent_2025_2026") == expected["recent"],
    "core_posthoc": aggregates.get("core", {}).get("n") == expected["core"]["n"],
    "mixed_purpose": aggregates.get("mixed", {}).get("n") == expected["mixed"]["n"],
    "shap": aggregates.get("xai_method_counts", {}).get("SHAP") == expected["shap"],
    "lime": aggregates.get("xai_method_counts", {}).get("LIME") == expected["lime"],
    "validation_design": aggregates.get("validation_design_counts") == expected["validation_design_counts"],
    "trust": aggregates.get("trust_counts") == expected["trust_counts"],
    "operational": aggregates.get("operational_counts") == expected["operational_counts"],
    "validation_gate": aggregates.get("gate_counts") == expected["gate_counts"],
    "reproducibility": aggregates.get("reproducibility_counts") == expected["reproducibility_counts"],
    "claim_risk": aggregates.get("claim_risk_counts") == expected["claim_risk_counts"],
    "explanation_scope": aggregates.get("explanation_scope_counts") == expected["explanation_scope_counts"],
    "explanation_scope_any_local": aggregates.get("explanation_scope_any_local") == expected["explanation_scope_any_local"],
    "explanation_scope_any_global": aggregates.get("explanation_scope_any_global") == expected["explanation_scope_any_global"],
    "direct_positive_reliability_evidence": aggregates.get("direct_positive_reliability_evidence") == expected["direct_positive_reliability_evidence"],
}
for name, passed in checks.items():
    if not passed:
        errors.append(f"aggregate check failed: {name}")

# Reported coding-reliability values.
reliability = read_csv(DERIVED / "table_data" / "coding_reliability.csv")
expected_reliability = {
    "explanation_role_primary": (100.0, 1.000, 1.000),
    "mixed_purpose_xai": (91.7, 0.729, 0.907),
    "trust_evidence_level": (97.2, 0.404, 0.971),
    "operational_evidence_level": (98.6, 0.935, 0.983),
    "validation_gate_reached": (95.8, 0.434, 0.955),
    "reproducibility_level": (100.0, 1.000, 1.000),
    "claim_risk": (80.6, 0.659, 0.746),
}
for row in reliability:
    axis = row["axis"]
    exp = expected_reliability[axis]
    got = (
        float(row["exact_agreement_pct"]),
        round(float(row["cohen_kappa"]), 3),
        round(float(row["gwet_ac1"]), 3),
    )
    if got != exp:
        errors.append(f"reliability mismatch for {axis}: expected {exp}, got {got}")

report = {
    "status": "PASS" if not errors else "FAIL",
    "errors": errors,
    "checks": checks,
    "screening": {"rows": len(screening), "included": included, "excluded": excluded},
    "canonical_master_rows": len(master),
    "headline_counts": {
        "recent_2025_2026": aggregates["recent_2025_2026"],
        "core_posthoc": aggregates["core"],
        "mixed_purpose": aggregates["mixed"],
        "explanation_scope_counts": aggregates["explanation_scope_counts"],
        "explanation_scope_any_local": aggregates["explanation_scope_any_local"],
        "explanation_scope_any_global": aggregates["explanation_scope_any_global"],
        "direct_positive_reliability_evidence": aggregates["direct_positive_reliability_evidence"],
        "SHAP": aggregates["xai_method_counts"]["SHAP"],
        "LIME": aggregates["xai_method_counts"]["LIME"],
    },
}
(DERIVED / "verification_report.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(json.dumps(report, indent=2, ensure_ascii=False))
raise SystemExit(0 if not errors else 1)

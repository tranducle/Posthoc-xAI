from __future__ import annotations

import csv
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReproductionTests(unittest.TestCase):
    def test_verification_gate(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "verify_reproducibility.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + "\n" + result.stderr)

    def test_canonical_master(self):
        with (ROOT / "data" / "canonical" / "study_master.csv").open(
            "r", encoding="utf-8-sig", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 84)
        self.assertEqual(len({row["study_id"] for row in rows}), 84)

    def test_headline_counts(self):
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "reproduce_results.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads((ROOT / "derived" / "aggregate_results.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["recent_2025_2026"], {"n": 63, "pct": 75.0})
        self.assertEqual(payload["core"]["n"], 76)
        self.assertEqual(payload["mixed"]["n"], 8)
        self.assertEqual(payload["xai_method_counts"]["SHAP"], 58)
        self.assertEqual(payload["xai_method_counts"]["LIME"], 46)
        self.assertEqual(
            payload["explanation_scope_counts"],
            {"local_only": 34, "global_only": 14, "both": 36},
        )
        self.assertEqual(payload["explanation_scope_any_local"], {"n": 70, "pct": 83.3})
        self.assertEqual(payload["explanation_scope_any_global"], {"n": 50, "pct": 59.5})
        self.assertEqual(payload["direct_positive_reliability_evidence"], {"n": 2, "pct": 2.4})


if __name__ == "__main__":
    unittest.main()

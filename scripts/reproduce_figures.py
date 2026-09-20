#!/usr/bin/env python3
"""Regenerate the five review figures from repository data.

Generated image files are written to outputs/ and are intentionally excluded
from version control. The repository stores the source data and generation code,
not the manuscript figures themselves.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIGDATA = ROOT / "derived" / "figure_data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    with (FIGDATA / name).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def save(fig, stem: str) -> None:
    fig.tight_layout()
    fig.savefig(OUT / f"{stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)


# Figure 1: PRISMA flow counts.
rows = read_csv("figure_01_prisma_counts.csv")
labels = [r["stage"].replace("_", " ") for r in rows]
values = [int(r["count"]) for r in rows]
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.barh(labels, values)
ax.set_xlabel("Records / studies")
ax.set_title("PRISMA study-selection counts")
ax.invert_yaxis()
for i, value in enumerate(values):
    ax.text(value, i, f" {value}", va="center")
save(fig, "figure_01_prisma_counts")


# Figure 2: taxonomy axes and category frequencies.
rows = read_csv("figure_02_taxonomy_axes.csv")
by_axis: dict[str, list[tuple[str, int]]] = defaultdict(list)
for r in rows:
    by_axis[r["axis"]].append((r["category"], int(r["study_count"])))
fig, axes = plt.subplots(len(by_axis), 1, figsize=(10, 14))
if len(by_axis) == 1:
    axes = [axes]
for ax, (axis_name, values) in zip(axes, by_axis.items()):
    values = sorted(values, key=lambda x: x[1], reverse=True)[:12]
    ax.barh([x[0] for x in values][::-1], [x[1] for x in values][::-1])
    ax.set_title(axis_name.replace("_", " ").title())
    ax.set_xlabel("Study count")
save(fig, "figure_02_taxonomy_axes")


# Figure 3: modality-method matrix.
rows = read_csv("figure_03_modality_method_matrix.csv")
modalities = []
families = []
for r in rows:
    if r["modality"] not in modalities:
        modalities.append(r["modality"])
    if r["method_family"] not in families:
        families.append(r["method_family"])
matrix = [[0 for _ in families] for _ in modalities]
for r in rows:
    matrix[modalities.index(r["modality"])][families.index(r["method_family"])] = int(r["study_count"])
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(matrix, aspect="auto")
ax.set_xticks(range(len(families)), families, rotation=35, ha="right")
ax.set_yticks(range(len(modalities)), modalities)
ax.set_title("Modality-method evidence matrix")
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        ax.text(j, i, str(value), ha="center", va="center")
fig.colorbar(im, ax=ax, label="Study count")
save(fig, "figure_03_modality_method_matrix")


# Figure 4: evidence ladder.
rows = read_csv("figure_04_evidence_ladder.csv")
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.axis("off")
for idx, r in enumerate(rows):
    y = len(rows) - idx
    ax.text(0.03, y, f"{r['level']}. {r['validation_gate']}", fontsize=12, weight="bold", va="center")
    ax.text(0.38, y, r["claim_scope"], fontsize=11, va="center", wrap=True)
ax.set_xlim(0, 1)
ax.set_ylim(0.5, len(rows) + 0.8)
ax.set_title("Evidence-maturity ladder")
save(fig, "figure_04_evidence_ladder")


# Figure 5: trust x operational evidence matrix.
rows = read_csv("figure_05_trust_operational_matrix.csv")
trust = []
operational = []
for r in rows:
    if r["trust_evidence"] not in trust:
        trust.append(r["trust_evidence"])
    if r["operational_evidence"] not in operational:
        operational.append(r["operational_evidence"])
matrix = [[0 for _ in operational] for _ in trust]
for r in rows:
    matrix[trust.index(r["trust_evidence"])][operational.index(r["operational_evidence"])] = int(r["study_count"])
fig, ax = plt.subplots(figsize=(11, 5.8))
im = ax.imshow(matrix, aspect="auto")
ax.set_xticks(range(len(operational)), operational, rotation=30, ha="right")
ax.set_yticks(range(len(trust)), trust)
ax.set_title("Trust-operation evidence matrix")
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        ax.text(j, i, str(value), ha="center", va="center")
fig.colorbar(im, ax=ax, label="Study count")
save(fig, "figure_05_trust_operational_matrix")

print(f"Generated 5 figures under {OUT.relative_to(ROOT)}/")

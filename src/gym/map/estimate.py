"""Compute closure per stratum for the Rust map (fable-plan.md § 4): Chapman and
Chao1 capture-recapture over the crosswalk, then the five-part closure rule.

Usage:
  uv run gym map estimate --crosswalk-dir merge/ --batch n \\
      --out estimate/ [--threshold 0.10] [--audit-pass a --audit-pass b] [--merge-check-agreement 0.95]

Reads every `crosswalk-b<i>.csv` with `i <= batch` (one row per team's mention of
a canonical Question in a source, per fable-plan.md line 130: "the crosswalk is
the capture-recapture input"). `--audit-pass` and `--merge-check-agreement` carry
part 3 of the rule (the batch's audit verdict and the merge-check agreement):
those are agent-written verdicts in `audit-b<n>.md` / `merge-check-b<n>.md`, not
structured data this plan gives a machine-readable shape for, so they are passed
in rather than parsed from prose.

Part 5 of the rule (a closed stratum re-opens on a later bad estimate, or on a
new Position adding a Question) needs no separate code: every run recomputes
every stratum fresh from the full crosswalk, so a stratum that regresses simply
stops reporting PASS on its next run.
"""

from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path


def read_crosswalk(directory: Path, through_batch: int) -> list[dict]:
    rows: list[dict] = []
    for path in sorted(directory.glob("crosswalk-b*.csv")):
        with path.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                if int(row["batch"]) <= through_batch:
                    rows.append(row)
    return rows


def chapman(n1: int, n2: int, m: int) -> tuple[float, float]:
    """Chapman-corrected Lincoln-Petersen estimate and its standard error (Seber 1982)."""
    estimate = (n1 + 1) * (n2 + 1) / (m + 1) - 1
    variance = (n1 + 1) * (n2 + 1) * (n1 - m) * (n2 - m) / ((m + 1) ** 2 * (m + 2))
    return estimate, math.sqrt(max(variance, 0.0))


def chao1(seen: int, f1: int, f2: int) -> tuple[float, float] | None:
    """Chao1 estimate and standard error (Chao 1987), or None when f2 = 0 (undefined)."""
    if f2 == 0:
        return None
    estimate = seen + f1**2 / (2 * f2)
    ratio = f1 / f2
    variance = f2 * (0.5 * ratio**2 + ratio**3 + 0.25 * ratio**4)
    return estimate, math.sqrt(max(variance, 0.0))


class StratumResult:
    def __init__(self, stratum: str, rows: list[dict]) -> None:
        self.stratum = stratum
        team_a = {row["question_id"] for row in rows if row["team"] == "a"}
        team_b = {row["question_id"] for row in rows if row["team"] == "b"}
        self.n1, self.n2, self.m = len(team_a), len(team_b), len(team_a & team_b)
        self.seen = len(team_a | team_b)
        self.batches = sorted({int(row["batch"]) for row in rows})
        self.chapman_n, self.chapman_se = chapman(self.n1, self.n2, self.m)
        mentions = Counter(row["question_id"] for row in rows)
        self.f1 = sum(1 for count in mentions.values() if count == 1)
        self.f2 = sum(1 for count in mentions.values() if count == 2)
        chao = chao1(self.seen, self.f1, self.f2)
        self.chao1_n, self.chao1_se = chao if chao else (None, None)

    def unseen_fraction(self, estimate: float | None) -> float | None:
        if estimate is None or estimate <= 0:
            return None
        return max(estimate - self.seen, 0.0) / estimate

    def ci(self, estimate: float, se: float) -> tuple[float, float]:
        return estimate - 1.96 * se, estimate + 1.96 * se

    def rule(self, threshold: float, audit_pass: set[str], merge_check_agreement: float) -> dict[str, str]:
        chapman_fraction = self.unseen_fraction(self.chapman_n)
        chao1_fraction = self.unseen_fraction(self.chao1_n)
        part1 = chapman_fraction is not None and chao1_fraction is not None and chapman_fraction <= threshold and chao1_fraction <= threshold
        part2 = len(self.batches) >= 2
        part3 = {"a", "b"} <= audit_pass and merge_check_agreement >= 0.90
        if self.seen >= 10:
            part4 = True
        elif len(self.batches) >= 3:
            part4 = "merge-into-core"
        else:
            part4 = False
        verdict = "PASS" if part1 and part2 and part3 and part4 is True else "FAIL"
        return {
            "part1_unseen_fraction": "PASS" if part1 else "FAIL",
            "part2_two_batches": "PASS" if part2 else "FAIL",
            "part3_audit_and_merge_check": "PASS" if part3 else "FAIL",
            "part4_seen_at_least_10": "PASS" if part4 is True else ("MERGE-INTO-CORE" if part4 == "merge-into-core" else "FAIL"),
            "part5_reopen": "N/A (recomputed fresh every run)",
            "verdict": verdict,
        }


def render(results: list[StratumResult], threshold: float, audit_pass: set[str], merge_check_agreement: float) -> str:
    lines = [f"# Closure — threshold {threshold:.0%}", ""]
    lines.append("| stratum | n1 | n2 | m | seen | Chapman N̂ | Chapman unseen % | 95% CI | Chao1 N̂ | Chao1 unseen % | 95% CI | verdict |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for result in sorted(results, key=lambda r: r.stratum):
        chapman_fraction = result.unseen_fraction(result.chapman_n)
        chapman_ci = result.ci(result.chapman_n, result.chapman_se)
        chao1_fraction = result.unseen_fraction(result.chao1_n)
        if result.chao1_n is None:
            chao1_cell, chao1_fraction_cell, chao1_ci_cell = "undefined (f2=0)", "undefined", "undefined"
        else:
            chao1_ci = result.ci(result.chao1_n, result.chao1_se)
            chao1_cell = f"{result.chao1_n:.1f}"
            chao1_fraction_cell = f"{chao1_fraction:.1%}"
            chao1_ci_cell = f"[{chao1_ci[0]:.1f}, {chao1_ci[1]:.1f}]"
        rule = result.rule(threshold, audit_pass, merge_check_agreement)
        lines.append(
            f"| {result.stratum} | {result.n1} | {result.n2} | {result.m} | {result.seen} "
            f"| {result.chapman_n:.1f} | {chapman_fraction:.1%} | [{chapman_ci[0]:.1f}, {chapman_ci[1]:.1f}] "
            f"| {chao1_cell} | {chao1_fraction_cell} | {chao1_ci_cell} | {rule['verdict']} |"
        )
    lines.append("")
    lines.append("## Five-part rule, per stratum")
    for result in sorted(results, key=lambda r: r.stratum):
        rule = result.rule(threshold, audit_pass, merge_check_agreement)
        lines.append(f"- {result.stratum}: 1={rule['part1_unseen_fraction']} 2={rule['part2_two_batches']} "
                      f"3={rule['part3_audit_and_merge_check']} 4={rule['part4_seen_at_least_10']} "
                      f"5={rule['part5_reopen']} -> {rule['verdict']}")
    return "\n".join(lines) + "\n"


def main(crosswalk_dir: Path, batch: int, out: Path, threshold: float, audit_pass: set[str], merge_check_agreement: float) -> int:
    rows = read_crosswalk(crosswalk_dir, batch)
    strata = sorted({row["stratum"] for row in rows})
    results = [StratumResult(stratum, [row for row in rows if row["stratum"] == stratum]) for stratum in strata]

    out.mkdir(parents=True, exist_ok=True)
    text = render(results, threshold, audit_pass, merge_check_agreement)
    out_path = out / f"closure-b{batch}.md"
    out_path.write_text(text, encoding="utf-8")
    print(text)
    print(f"written: {out_path}")
    return 0

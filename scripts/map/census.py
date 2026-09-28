"""Nothing-new census: the scripted gate that runs before the batch audit draws (batch-2-prep.md; slice-1-review.md § 4, process changes).

Usage: `uv run python scripts/map/census.py --recon RECON --batch n --out RECON/audit/`.

Reads every `team-{a,b}/readlog-b<n>-*.csv` and `extract-b<n>-*.md`. Entries in
files named `*-fix<k>.*` (re-extraction of flagged rows) supersede every earlier
entry for their frame ids. A row is nothing-new when every entry left for it
reads `yes` with `new_questions` and `claims` both 0. It is flagged when:

- a read-log line does not parse to the 7 columns of `prompts/t2-extract.md`;
- it is nothing-new and its extract section has no `### Nothing new` block with
  a `reason-code:` from REASON_CODES and a `reason:` line;
- its reason sentence uses the opposition vocabulary in FORBIDDEN, which the
  frozen t2 prompt bans from reasons (rule 6: opposition is never a ground).

Writes `census-b<n>.md` (counts, every flagged row) and
`census-b<n>-population.csv` (team, frame_id, reason_code: the population the
audit draws from). Exit status 1 while anything is flagged: the audit does not
draw until the census exits 0.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

READLOG_FIELDS = ["frame_id", "url", "read", "locator_span", "new_questions", "claims", "minutes"]
REASON_CODES = {"off-subject", "no-decision", "no-rust-voice"}
FORBIDDEN = re.compile(
    r"\b(disagree\w*|agree\w*|oppos\w*|debat\w*|disput\w*|contest\w*|controvers\w*|counter\w*|"
    r"push(es|ed|ing)?[- ]?back|rebut\w*|dissent\w*|consensus|unanimous\w*|competing|rival\w*|"
    r"single[- ]voice\w*|one voice|only voice|second voice|other voices?|another (view|voice|position|opinion)|"
    r"nobody|no[- ]one)\b",
    re.IGNORECASE,
)
SECTION = re.compile(r"^## .*?\b(f\d{6})\b")


def is_fix(path: Path) -> bool:
    return re.search(r"-fix\d+$", path.stem) is not None


def ordered(paths: list[Path]) -> list[Path]:
    """Ordinary files first, then fix files in name order, so later entries supersede earlier ones."""
    return sorted(paths, key=lambda path: (is_fix(path), path.name))


def read_logs(team_dir: Path, batch: int, flags: list[tuple[str, str]]) -> dict[str, list[list[str]]]:
    entries: dict[str, list[list[str]]] = {}
    for path in ordered(list(team_dir.glob(f"readlog-b{batch}-*.csv"))):
        fresh: dict[str, list[list[str]]] = {}
        with path.open(encoding="utf-8", newline="") as handle:
            for line_number, row in enumerate(csv.reader(handle), start=1):
                if not row or row[0] == "frame_id":
                    continue
                if len(row) != len(READLOG_FIELDS):
                    flags.append((row[0], f"{path.name} line {line_number}: {len(row)} columns, not {len(READLOG_FIELDS)}"))
                    continue
                fresh.setdefault(row[0], []).append(row)
        for frame_id, rows in fresh.items():
            entries[frame_id] = (entries.get(frame_id, []) if not is_fix(path) else []) + rows
    return entries


def nothing_new_reasons(team_dir: Path, batch: int) -> dict[str, dict[str, str]]:
    reasons: dict[str, dict[str, str]] = {}
    for path in ordered(list(team_dir.glob(f"extract-b{batch}-*.md"))):
        current, in_block = None, False
        for line in path.read_text(encoding="utf-8").splitlines():
            section = SECTION.match(line)
            if section:
                current, in_block = section.group(1), False
                reasons[current] = {}
                continue
            if line.startswith("### "):
                in_block = line.strip().lower() == "### nothing new"
                continue
            if current and in_block:
                label, _, value = line.partition(":")
                if label.strip().lower() in {"reason-code", "reason"}:
                    reasons[current][label.strip().lower()] = value.strip()
    return reasons


def census_team(team_dir: Path, batch: int) -> tuple[list[tuple[str, str]], list[tuple[str, str]], Counter]:
    flags: list[tuple[str, str]] = []
    entries = read_logs(team_dir, batch, flags)
    reasons = nothing_new_reasons(team_dir, batch)
    population: list[tuple[str, str]] = []
    codes: Counter = Counter()
    for frame_id in sorted(entries):
        rows = entries[frame_id]
        if not all(row[2] == "yes" for row in rows):
            continue
        try:
            if sum(int(row[4]) + int(row[5]) for row in rows) != 0:
                continue
        except ValueError:
            flags.append((frame_id, "new_questions or claims is not an integer"))
            continue
        reason = reasons.get(frame_id, {})
        code, sentence = reason.get("reason-code", ""), reason.get("reason", "")
        if code not in REASON_CODES:
            flags.append((frame_id, f"reason-code {code!r} not one of {sorted(REASON_CODES)}"))
            continue
        if not sentence:
            flags.append((frame_id, "no reason line"))
            continue
        hit = FORBIDDEN.search(sentence)
        if hit:
            flags.append((frame_id, f"forbidden ground {hit.group(0)!r}: {sentence}"))
            continue
        population.append((frame_id, code))
        codes[code] += 1
    return flags, population, codes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recon", required=True, type=Path)
    parser.add_argument("--batch", required=True, type=int)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    lines = [f"# Nothing-new census — batch {args.batch}", "",
             "| team | nothing-new rows passing | flagged | " + " | ".join(sorted(REASON_CODES)) + " |",
             "| --- | --- | --- | " + " | ".join("---" for _ in REASON_CODES) + " |"]
    flagged_lines: list[str] = []
    population_rows: list[dict] = []
    total_flags = 0
    for team in "ab":
        flags, population, codes = census_team(args.recon / f"team-{team}", args.batch)
        total_flags += len(flags)
        lines.append(f"| {team} | {len(population)} | {len(flags)} | " + " | ".join(str(codes[code]) for code in sorted(REASON_CODES)) + " |")
        flagged_lines += [f"- {team} `{frame_id}`: {why}" for frame_id, why in flags]
        population_rows += [{"team": team, "frame_id": frame_id, "reason_code": code} for frame_id, code in population]
    lines += ["", f"Gate: {'PASS' if total_flags == 0 else 'FAIL'} ({total_flags} flagged)", "", "## Flagged rows", ""]
    lines += flagged_lines or ["none"]

    args.out.mkdir(parents=True, exist_ok=True)
    report = args.out / f"census-b{args.batch}.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with (args.out / f"census-b{args.batch}-population.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["team", "frame_id", "reason_code"])
        writer.writeheader()
        writer.writerows(population_rows)
    print("\n".join(lines))
    print(f"written: {report}")
    return 0 if total_flags == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

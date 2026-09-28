"""Compile RECON/args/arguments-chunk-00..03.md into MAP/arguments/.
Transcription only. An Argument whose values are entirely value-candidate
entries stays out of MAP; see RECON/args/value-candidates.md. See
RECON/compile/compile-b1.md for accounting.
"""
import re
import glob
import yaml
from pathlib import Path
from collections import Counter, defaultdict

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
MAP = Path("/Users/ryzhakar/pp/gym/maps/rust")

VALUE_IDS = {"approachability", "correctness", "iteration-speed", "performance", "simplicity", "stability"}

LINE_RE = re.compile(r"^- (for|against) \| (.*?) \| values: (.*?) \| sources: (.*)$")
NO_ARG_RE = re.compile(r"^- (for|against) \| no argument in sources")
SRC_ID_RE = re.compile(r"\bf\d{6}(?=@)")


def split_top_level(s: str, sep: str = ",") -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


existing_questions = {p.stem for p in (MAP / "questions").glob("*.yaml")}
existing_positions = {p.stem for p in (MAP / "positions").glob("*.yaml")}
existing_sources = {p.stem for p in (MAP / "sources").glob("*.yaml")}

issues = []
arguments = []  # list of dicts, one per kept Argument, position/side/text/values/sources
candidate_occurrences = []  # (candidate_name, question_id, position_id, side)
n_no_arg = 0
n_total_lines = 0
n_parse_fail = 0

cur_q = None
cur_p = None
for fp in sorted(glob.glob(str(RECON / "args" / "arguments-chunk-*.md"))):
    for raw in Path(fp).read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            cur_q = line[3:].strip()
            if cur_q not in existing_questions:
                issues.append(("arg-question-missing", f"'{cur_q}' ({fp}) does not resolve to an existing Question; its Arguments are skipped."))
            continue
        if line.startswith("### "):
            cur_p = line[4:].strip()
            if cur_p not in existing_positions:
                issues.append(("arg-position-missing", f"'{cur_p}' ({fp}) does not resolve to an existing Position; its Arguments are skipped."))
            continue
        if line.strip() == "- no argument in sources" or NO_ARG_RE.match(line):
            n_no_arg += 1
            continue
        if line.startswith("- for |") or line.startswith("- against |"):
            n_total_lines += 1
            if cur_p not in existing_positions:
                continue  # already flagged above; nothing to attach it to
            m = LINE_RE.match(line)
            if not m:
                n_parse_fail += 1
                issues.append(("arg-parse-fail", f"{fp}: {line[:200]!r}"))
                continue
            side, text, values_seg, sources_seg = m.groups()
            tokens = split_top_level(values_seg)
            fixed = [t for t in tokens if t in VALUE_IDS]
            candidates = [t for t in tokens if t.startswith("value-candidate:")]
            unknown = [t for t in tokens if t not in VALUE_IDS and not t.startswith("value-candidate:")]
            for u in unknown:
                issues.append(("arg-unknown-value-token", f"{fp} {cur_p}: unrecognized value token {u!r}; dropped."))
            for c in candidates:
                name = c[len("value-candidate:"):].strip()
                name = re.sub(r"\s*\(flagged:.*$", "", name).strip()
                candidate_occurrences.append((name, cur_q, cur_p, side))

            seen_src = []
            for sid in SRC_ID_RE.findall(sources_seg):
                if sid not in seen_src:
                    seen_src.append(sid)
            for sid in seen_src:
                if sid not in existing_sources:
                    issues.append(("arg-source-missing", f"{fp} {cur_p}: source '{sid}' does not resolve to an existing Source; dropped from this Argument's sources."))
            seen_src = [s for s in seen_src if s in existing_sources]

            if fixed:
                arguments.append(dict(question=cur_q, position=cur_p, side=side, text=text.strip(),
                                       values=fixed, sources=seen_src))

issues.append(("args-parsed", f"{n_total_lines} for/against lines parsed, {n_parse_fail} failed to parse, {n_no_arg} 'no argument in sources' lines skipped"))

# ---------------------------------------------------------------------------
# Assign ids: <position>--NN, sequential per position over kept Arguments only.
# ---------------------------------------------------------------------------

by_position = defaultdict(list)
for a in arguments:
    by_position[a["position"]].append(a)

n_written = 0
for pid, args in by_position.items():
    for i, a in enumerate(args, start=1):
        aid = f"{pid}--{i:02d}"
        data = {"id": aid, "position": a["position"], "side": a["side"], "text": a["text"], "values": a["values"]}
        if a["sources"]:
            data["sources"] = a["sources"]
        path = MAP / "arguments" / f"{aid}.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)
        n_written += 1

n_parsed_ok = n_total_lines - n_parse_fail
n_excluded_candidate_only = n_parsed_ok - len(arguments)
issues.append(("arguments-written", f"{n_written} Argument entities written across {len(by_position)} Positions"))
issues.append(("arguments-excluded-candidate-only", f"{n_excluded_candidate_only} Arguments excluded from MAP (values were entirely value-candidate entries)"))

# ---------------------------------------------------------------------------
# RECON/args/value-candidates.md
# ---------------------------------------------------------------------------

by_candidate = defaultdict(list)
for name, q, p, side in candidate_occurrences:
    by_candidate[name].append((q, p, side))

lines = ["# Value candidates (t5 compile, 2026-09-28)", "",
         "Every `value-candidate:` name seen in `args/arguments-chunk-00..03.md`, "
         "whether or not the Argument carrying it also carried a fixed Value (and so "
         "made it into `MAP/arguments/`). An Argument whose values were entirely "
         "candidates is not in MAP at all; this is its only record.", ""]
for name in sorted(by_candidate, key=lambda n: -len(by_candidate[n])):
    occ = by_candidate[name]
    lines.append(f"## {name} ({len(occ)})")
    lines.append("")
    for q, p, side in occ:
        lines.append(f"- {q} / `{p}` ({side})")
    lines.append("")

(RECON / "args" / "value-candidates.md").write_text("\n".join(lines), encoding="utf-8")
issues.append(("value-candidates-written", f"{len(by_candidate)} distinct candidate names, {len(candidate_occurrences)} total occurrences, written to RECON/args/value-candidates.md"))

print("questions with arguments:", len({a['question'] for a in arguments}))
print("positions with arguments:", len(by_position))
print("arguments written:", n_written)
print("candidate-only excluded:", n_excluded_candidate_only)
print()
for t, d in issues:
    print(t, "|", d)

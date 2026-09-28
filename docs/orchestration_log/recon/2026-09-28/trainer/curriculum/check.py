"""Check curriculum/rust.yaml and curriculum/baseline.yaml against maps/rust/.

Run from anywhere: `uv run python <path>/check.py`. Prints one PASS/FAIL/WARN line
per check, then a count; exits 1 on any FAIL.
"""

import collections
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "pyproject.toml").exists())
MAP = ROOT / "maps" / "rust"

UNIT_KEYS = {"id", "kind", "cluster", "concepts", "question", "domain", "form",
             "revisit_at_days", "after", "status", "gap"}
BASELINE_FORMS = {"predict-output", "fix-the-compile-error", "write-to-tests"}
FIRST_DELAYED_PROBE_MIN_DAYS = 7  # O3

results = []


def check(ok, what, level="FAIL"):
    results.append(("PASS" if ok else level, what))


def load_kind(home):
    d = MAP / home
    return {p.stem: yaml.safe_load(p.read_text()) for p in d.glob("*.yaml")} if d.is_dir() else {}


concepts = load_kind("concepts")
questions = load_kind("questions")
domains = load_kind("domains")
positions = load_kind("positions")
arguments = load_kind("arguments")

positions_of = collections.defaultdict(set)
for pid, p in positions.items():
    positions_of[p["question"]].add(pid)
argued = {a["position"] for a in arguments.values()}

cur = yaml.safe_load((HERE / "rust.yaml").read_text())
base = yaml.safe_load((HERE / "baseline.yaml").read_text())
forms = cur["forms"]
units = cur["units"]
by_id = {u["id"]: u for u in units}

check(len(units) == 12, f"12 units (found {len(units)})")
check(len(by_id) == len(units), "unit ids unique")

seen = set()
for u in units:
    uid = u.get("id", "?")
    extra = set(u) - UNIT_KEYS
    check(not extra, f"{uid}: no unknown fields {sorted(extra) or ''}")
    kind = u.get("kind")
    check(kind in ("mechanism", "judgment"), f"{uid}: kind is mechanism|judgment ({kind})")
    form = u.get("form")
    check(form in forms, f"{uid}: names a defined form ({form})")
    check(form in forms and forms[form]["kind"] == kind, f"{uid}: form kind matches unit kind")
    check(u.get("domain") in domains, f"{uid}: domain resolves ({u.get('domain')})")
    for c in u.get("concepts", []):
        check(c in concepts, f"{uid}: concept resolves ({c})")
    check(bool(u.get("concepts")), f"{uid}: concepts non-empty")
    days = u.get("revisit_at_days", [])
    check(bool(days) and all(isinstance(d, int) and d > 0 for d in days) and days == sorted(days)
          and days[0] >= FIRST_DELAYED_PROBE_MIN_DAYS,
          f"{uid}: revisit_at_days ascending, first >= {FIRST_DELAYED_PROBE_MIN_DAYS} ({days})")
    for a in u.get("after", []):
        check(a in seen, f"{uid}: after {a} resolves and precedes it")

    if kind == "mechanism":
        check("question" not in u, f"{uid}: mechanism unit names no question")
        check("status" not in u, f"{uid}: mechanism unit carries no status")
        check(bool(u.get("cluster")), f"{uid}: mechanism unit names its cluster")
    if kind == "judgment":
        q = u.get("question")
        check(q in questions, f"{uid}: question resolves ({q})")
        if q in questions:
            check(u.get("domain") in questions[q]["domains"], f"{uid}: domain is one of the question's domains")
            npos = len(positions_of[q])
            check(npos >= 2, f"{uid}: question has >= 2 positions ({npos})")
            reach, stack = set(), list(u.get("after", []))
            while stack:
                a = stack.pop()
                if a in by_id and a not in reach:
                    reach.add(a)
                    stack.extend(by_id[a].get("after", []))
            trained = {c for a in reach for c in by_id[a]["concepts"]}
            want = set(questions[q]["concepts"]) & trained
            check(set(u["concepts"]) == want,
                  f"{uid}: concepts = question concepts reachable through after "
                  f"(missing {sorted(want - set(u['concepts']))}, extra {sorted(set(u['concepts']) - want)})")
            has_args = sum(1 for p in positions_of[q] if p in argued) >= 2
            if has_args:
                check(u.get("status") != "needs-arguments",
                      f"{uid}: needs-arguments is stale (>= 2 positions argued)", "WARN")
            else:
                check(u.get("status") == "needs-arguments",
                      f"{uid}: marked needs-arguments (MAP/arguments has {len(arguments)} files)")
    if u.get("gap"):
        results.append(("WARN", f"{uid}: map gap declared: {u['gap'][:90]}"))
    seen.add(uid)

# Baseline.
items = base["items"]
clusters = {u["cluster"] for u in units if u["kind"] == "mechanism"}
check(len(items) == 6, f"baseline: 6 items (found {len(items)})")
bc = collections.Counter(i["cluster"] for i in items)
check(set(bc) == clusters and all(n == 1 for n in bc.values()),
      f"baseline: one item per mechanism cluster ({dict(bc)})")
fc = collections.Counter(i["form"] for i in items)
check(set(fc) <= BASELINE_FORMS and all(fc[f] == 2 for f in BASELINE_FORMS),
      f"baseline: 2 items per form ({dict(fc)})")
for i in items:
    for k in ("id", "cluster", "form", "tests", "pass", "continuous"):
        check(bool(i.get(k)), f"baseline {i.get('id', '?')}: names {k}")

counts = collections.Counter(r for r, _ in results)
for r, what in results:
    print(f"{r:4}  {what}")
print(f"\n{counts['PASS']} PASS, {counts['FAIL']} FAIL, {counts['WARN']} WARN")
print(f"MAP: {len(concepts)} concepts, {len(questions)} questions, {len(domains)} domains, "
      f"{len(positions)} positions, {len(arguments)} arguments")
sys.exit(1 if counts["FAIL"] else 0)

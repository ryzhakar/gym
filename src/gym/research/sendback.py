"""Build re-extraction bundles for batch-1 rows still logged "nothing new".

Usage: uv run python scripts/research/sendback.py <team-a|team-b> <pass-name>

`pass-name` selects a round (see PASSES): "R", the first send-back the audit
(RECON/audit/audit-b1.md) asked for, or "T", a third pass over rows still nothing-new after
that send-back was re-extracted. Each pass writes its own samples/bundles/b1-{team}-{pass}NN.txt
slices and b1-{team}-{pass}-manifest.csv, independent of the others.

Population: merge every RECON/team-{team}/readlog-b1-*.csv entry by frame_id, across ALL
files present for that team at run time (original slices, s-prefixed re-reads, L1/L2
supplements, and - once they exist - sR* re-reads of the R pass). Six team-a rows have an
unquoted comma in `locator_span` (extra CSV fields); 18 team-b rows are missing the `minutes`
column (one field short) - PARSE_ROW tolerates both, following the exact recipe in the
audit's own `draw.py`. A frame_id is still-nothing-new when every merged entry reads "yes"
and its new_questions sum to 0 across all of them: an L1/L2 or sR* re-read that actually
found content makes the sum nonzero, which is what excludes a row a later pass calls
"superseded" - no separate exclusion step is needed once every readlog file is merged in,
which is also why the R pass and the T pass share one population function: T's population is
just R's, recomputed once sR* entries exist on disk to merge in.

This reproduced the R pass's population count exactly against the audit's own figures
(team-a 92, team-b 101) as a correctness check.

Re-fetches (via cache.fetch_by_class_route) any selected row whose current cached text is a
bot/login stub or under 1,500 chars - a thin capture masquerading as "nothing new" is exactly
what a send-back exists to correct.

Output: samples/bundles/b1-team-{team}-{pass}{nn}.txt (~150k-char slices, never splitting a
source, same header format as bundle.py) and samples/bundles/b1-team-{team}-{pass}-manifest.csv
(slice,data_row,id,url,status,reason,chars).
"""
import csv
import glob
import sys
from pathlib import Path

from gym.paths import ROOT
from gym.research import cache as c

RECON = ROOT / "docs/orchestration_log/recon/2026-09-27/research/rust-map"
SAMPLES = RECON / "samples"
BUNDLES = SAMPLES / "bundles"
STATUS_CSV = SAMPLES / "prefetch-b1-status.csv"
SLICE_TARGET_CHARS = 150_000

# Per pass: ids to drop from the population regardless of merge outcome (a "decided" exclusion,
# not a fetch-quality one), and ids expected already inside the population as a sanity check.
PASSES = {
    "R": {"exclude": set(), "expect": {"team-a": "f000227", "team-b": "f012788"}},
    "T": {"exclude": {"f000149"}, "expect": {}},  # f000149: access gap, decided - not resent
}


def parse_row(r: list[str]) -> tuple[str, str, str, str, str]:
    """frame_id, url, read, new_questions, claims - tolerant of the two known malformations."""
    if len(r) == 7:
        return r[0], r[1], r[2], r[4], r[5]
    if len(r) > 7:  # unquoted comma inside locator_span added extra fields in the middle
        return r[0], r[1], r[2], r[-3], r[-2]
    if len(r) == 6:  # missing `minutes`; every other column keeps its normal index
        return r[0], r[1], r[2], r[4], r[5]
    raise ValueError(r)


def nothing_new_population(team: str) -> dict[str, str]:
    """frame_id -> url, for every row whose merged read-log entries are all "yes" with
    new_questions summing to 0."""
    entries: dict[str, list[tuple[str, str, str]]] = {}
    for path in sorted(glob.glob(str(RECON / team / "readlog-b1-*.csv"))):
        for row in csv.reader(open(path, newline="")):
            if row[0] == "frame_id":
                continue
            fid, url, read, nq, _claims = parse_row(row)
            entries.setdefault(fid, []).append((url, read, nq))

    population = {}
    for fid, es in entries.items():
        all_yes = all(read == "yes" for _, read, _ in es)
        total_nq = sum(int(nq) if nq.strip() else 0 for _, _, nq in es)
        if all_yes and total_nq == 0:
            population[fid] = es[0][0]
    return population


def latest_status_by_id_url() -> dict[tuple[str, str], dict]:
    latest: dict[tuple[str, str], dict] = {}
    for row in csv.DictReader(STATUS_CSV.open(newline="")):
        latest[(row["id"], row["url"])] = row
    return latest


def load_text(status_row: dict) -> str | None:
    key = status_row.get("key")
    if not key:
        return None
    for suffix in (".txt", ".abstract.txt"):
        p = c.CACHE / f"{key}{suffix}"
        if p.exists():
            return p.read_text(errors="replace")
    return None


def is_stub_or_thin(text: str | None) -> str | None:
    """None if the text is usable; else the drop reason (no-text, stub, thin)."""
    if text is None:
        return "no-text"
    lower = text.lower()
    if any(marker in lower for marker in c.CHALLENGE_MARKERS):
        return "stub"
    if len(text) < c.MIN_PAGE_CHARS:
        return "thin"
    return None


def build(team_arg: str, pass_name: str) -> None:
    pass_config = PASSES[pass_name]
    team_letter = team_arg[-1]  # "team-a" -> "a"
    population = nothing_new_population(f"team-{team_letter}")

    # A soft check, not a hard invariant: `expected` held the first time this pass ran, but
    # population membership is expected to shift once real extraction work lands (e.g. an
    # sR* re-read moving a row's new_questions above 0 correctly drops it from later passes).
    expected = pass_config["expect"].get(team_arg)
    if expected and expected not in population:
        print(f"note: {expected} no longer in the nothing-new population (expected the first "
              f"time this pass ran; a later re-read likely found real content)")
    for fid in pass_config["exclude"]:
        population.pop(fid, None)

    batch_rows = list(csv.DictReader((SAMPLES / f"batch-1-{team_arg}.csv").open(newline="")))
    row_by_id = {r["id"]: (i, r) for i, r in enumerate(batch_rows, start=1)}
    status_by_id_url = latest_status_by_id_url()

    manifest: list[dict] = []
    kept: list[tuple[dict, str]] = []
    refetched = 0

    for fid in sorted(population):
        if fid not in row_by_id:
            continue  # a frame_id logged by this team but not in its own batch CSV row set
        data_row, batch_row = row_by_id[fid]
        status_row = status_by_id_url.get((fid, batch_row["url"]), {})
        text = load_text(status_row)
        reason = is_stub_or_thin(text)
        if reason:  # stub/redirect/thin (or never fetched) - try once, live
            try:
                fetched = c.fetch_by_class_route(batch_row["url"], batch_row["class"])
                text = fetched.text
                c.save_text(c.url_key(batch_row["url"]), text, fetched.route, batch_row["url"])
                reason = is_stub_or_thin(text)
                refetched += 1
            except Exception as e:  # noqa: BLE001 - genuinely unreachable; report and move on
                reason = reason or "no-text"
                text = None
        chars = len(text) if text is not None else 0
        manifest.append({
            "data_row": data_row, "id": fid, "url": batch_row["url"],
            "status": "dropped" if reason else "kept", "reason": reason or "", "chars": chars,
        })
        if reason is None:
            kept.append((batch_row | {"data_row": data_row}, text))

    kept.sort(key=lambda rt: rt[0]["data_row"])
    BUNDLES.mkdir(parents=True, exist_ok=True)
    for stale in BUNDLES.glob(f"b1-{team_arg}-{pass_name}*.txt"):
        stale.unlink()  # this bundle is fully rebuilt each run, unlike bundle.py's frozen slices

    slices: list[list[tuple[dict, str]]] = [[]]
    running = 0
    for row, text in kept:
        piece_len = min(len(text), SLICE_TARGET_CHARS)
        if slices[-1] and running + piece_len > SLICE_TARGET_CHARS:
            slices.append([])
            running = 0
        slices[-1].append((row, text))
        running += piece_len

    row_to_slice = {}
    for i, sl in enumerate(slices, start=1):
        if not sl:
            continue
        path = BUNDLES / f"b1-{team_arg}-{pass_name}{i:02d}.txt"
        with path.open("w") as f:
            for row, text in sl:
                if len(text) > SLICE_TARGET_CHARS:
                    text = text[:SLICE_TARGET_CHARS] + "\n[... truncated at 150,000 chars ...]\n"
                header = (f"=== ROW {row['data_row']} | {row['id']} | {row['url']} | "
                          f"{row['date']} | {row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
                row_to_slice[row["data_row"]] = i

    for entry in manifest:
        entry["slice"] = (f"{pass_name}{row_to_slice[entry['data_row']]:02d}"
                           if entry["data_row"] in row_to_slice else "")

    manifest.sort(key=lambda e: e["data_row"])
    manifest_path = BUNDLES / f"b1-{team_arg}-{pass_name}-manifest.csv"
    with manifest_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slice", "data_row", "id", "url", "status", "reason", "chars"])
        w.writeheader()
        for entry in manifest:
            w.writerow({k: entry[k] for k in w.fieldnames})

    n_slices = sum(1 for sl in slices if sl)
    n_kept = sum(1 for e in manifest if e["status"] == "kept")
    n_dropped = len(manifest) - n_kept
    print(f"{team_arg} pass {pass_name}: {len(population)} nothing-new population, "
          f"{len(manifest)} rows built, {refetched} re-fetched, {n_kept} kept, "
          f"{n_dropped} dropped, {n_slices} slices -> {manifest_path}")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])

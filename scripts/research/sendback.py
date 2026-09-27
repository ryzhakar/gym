"""Build send-back bundles: batch-1 rows an extractor logged as "nothing new" that the
audit (RECON/audit/audit-b1.md) sends back for re-extraction.

Usage: uv run python scripts/research/sendback.py <team-a|team-b>

Population: merge every RECON/team-{team}/readlog-b1-*.csv entry by frame_id, across ALL
files for that team (the original slices, the s-prefixed re-reads, and the L1/L2 supplements).
Six team-a rows have an unquoted comma in `locator_span` (extra CSV fields); 18 team-b rows
are missing the `minutes` column (one field short) - PARSE_ROW tolerates both, following the
exact recipe in the audit's own `draw.py`. A frame_id sends back when every merged entry reads
"yes" and its new_questions sum to 0 across all of them: an L1/L2 re-read that actually found
content makes the sum nonzero, which is what excludes a row the audit calls "superseded" -
no separate exclusion step is needed once every readlog file is merged in.

This reproduces the audit's own "nothing-new" population count exactly (team-a 92, team-b
101) as a correctness check. team-a f000227 and team-b f012788 are confirmed already inside
it (single yes/0 entries each) rather than added on top.

Re-fetches (via cache.fetch_by_class_route) any selected row whose current cached text is a
bot/login stub or under 1,500 chars - a thin capture masquerading as "nothing new" is exactly
what this send-back exists to correct (f000227's rtic.rs stub was already fixed in an earlier
round and needs no further work here).

Output: samples/bundles/b1-team-{team}-R{nn}.txt (~150k-char slices, never splitting a
source, same header format as bundle.py) and samples/bundles/b1-team-{team}-R-manifest.csv
(slice,data_row,id,url,status,reason,chars).
"""
import csv
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cache as c  # noqa: E402 - local module, path set above

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
SAMPLES = RECON / "samples"
BUNDLES = SAMPLES / "bundles"
STATUS_CSV = SAMPLES / "prefetch-b1-status.csv"
SLICE_TARGET_CHARS = 150_000
FORCED = {"team-a": "f000227", "team-b": "f012788"}  # confirmed already inside the population


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


def build(team_arg: str) -> None:
    team_letter = team_arg[-1]  # "team-a" -> "a"
    population = nothing_new_population(f"team-{team_letter}")
    forced = FORCED[team_arg]
    assert forced in population, f"{forced} expected inside the nothing-new population, wasn't"

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
    for stale in BUNDLES.glob(f"b1-{team_arg}-R*.txt"):
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
        path = BUNDLES / f"b1-{team_arg}-R{i:02d}.txt"
        with path.open("w") as f:
            for row, text in sl:
                if len(text) > SLICE_TARGET_CHARS:
                    text = text[:SLICE_TARGET_CHARS] + "\n[... truncated at 150,000 chars ...]\n"
                header = (f"=== ROW {row['data_row']} | {row['id']} | {row['url']} | "
                          f"{row['date']} | {row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
                row_to_slice[row["data_row"]] = i

    for entry in manifest:
        entry["slice"] = f"R{row_to_slice[entry['data_row']]:02d}" if entry["data_row"] in row_to_slice else ""

    manifest.sort(key=lambda e: e["data_row"])
    manifest_path = BUNDLES / f"b1-{team_arg}-R-manifest.csv"
    with manifest_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slice", "data_row", "id", "url", "status", "reason", "chars"])
        w.writeheader()
        for entry in manifest:
            w.writerow({k: entry[k] for k in w.fieldnames})

    n_slices = sum(1 for sl in slices if sl)
    n_kept = sum(1 for e in manifest if e["status"] == "kept")
    n_dropped = len(manifest) - n_kept
    print(f"{team_arg}: {len(population)} nothing-new population, {len(manifest)} rows built, "
          f"{refetched} re-fetched, {n_kept} kept, {n_dropped} dropped, "
          f"{n_slices} slices -> {manifest_path}")


if __name__ == "__main__":
    build(sys.argv[1])

"""Cut a fetched batch into read-sized text bundles for extraction agents.

Usage: uv run python scripts/research/bundle.py <team-a|team-b> [--batch n] [--out DIR]

Input: samples/batch-{n}-team-{team}.csv (data rows, in order) and the shared cache
CACHE/<key>.txt. Each batch row's fetch status comes from samples/prefetch-b{n}-status.csv,
looked up by (id, url) - fetch-csv appends rather than rewrites, so a re-fetched row may
have more than one status line; the last one (most recent) wins.

For each row, keep only if its cached text exists, is not a bot/login-wall stub, and passes
cache.py's own page check (validate_page_text: >=1,500 chars, or a whole page by that host's
COMPLETE_PAGE_MARKERS); otherwise it is dropped with one reason: no-text, stub, thin. A row on
forums.swift.org is kept only with >=3 "rust" mentions, else dropped as off-subject (a
stricter, host-specific override - Swift-internal threads with a passing Rust comparison
produced zero Questions in every slice read). Every other row with zero "rust" mentions is
also dropped as off-subject, unless its URL is a github.com repo, a *.rs / docs.rs /
crates.io host, or one of this batch's own class=domain-subframes hosts (presumed on-subject
even at zero mentions, since the frame put it in scope on purpose). Kept rows are cut, in
CSV order, into ~150k-char slices, never splitting a source (an oversized source becomes its
own slice: cut at 150k in batch 1, whole from batch 2 on).

Batch 1 only (BATCH_1 below; later batches have none of this): some slices are frozen - already assigned and read by an extractor.
Their manifest rows and slice files are left untouched; only unassigned rows are
reclassified and packed into new slices numbered above the frozen range. Exception: a frozen
row matching a SUPPLEMENTS predicate (class=hn-lobsters -> L1; a talks-class row whose frozen
`chars` exceeded the 150k slice cap, i.e. it was truncated -> L2) gets a fresh copy of its
current cached text written to a supplementary b1-{team}-<name>.txt, and the manifest's slice
column for that row is repointed at that name - the original numbered slice file is still
left alone. Once assigned to a supplement a row stays there on every future rerun, even if
refreshed text no longer matches the predicate that first caught it.

Output: samples/bundles/b{n}-{team}-{jj}.txt (one file per slice, each source preceded by a
`=== ROW n | id | url | date | class ===` header) and samples/bundles/b{n}-{team}-manifest.csv
(slice,data_row,id,url,status,reason,chars). `--out` writes elsewhere; frozen state is still
read from samples/bundles/, so batch 1 can be re-cut into a scratch directory and compared.
"""
import argparse
import csv
import sys
from pathlib import Path
from typing import Callable
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
import cache as c  # noqa: E402 - local module, path set above

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
SAMPLES = RECON / "samples"
BUNDLES = SAMPLES / "bundles"
SLICE_TARGET_CHARS = 150_000

# Each entry: (supplement slice name, predicate over (batch_row, frozen_manifest_entry)).
# A frozen row matching one of these gets its current cached text written to a supplementary
# b1-{team}-<name>.txt, and its manifest slice/chars repointed there - the original numbered
# slice file is left exactly as it was. Checked in order; a row is claimed by the first match.
SUPPLEMENTS: list[tuple[str, Callable[[dict, dict], bool]]] = [
    ("L1", lambda batch_row, frozen_entry: "hn-lobsters" in batch_row["class"].split(";")),
    ("L2", lambda batch_row, frozen_entry: (
        "talks" in batch_row["class"].split(";")
        and int(frozen_entry.get("chars") or 0) > SLICE_TARGET_CHARS
    )),
]
# Batch-specific history. Only batch 1 has any: rows extracted before bundling existed,
# slices already assigned when the bundler changed, and supplements for defects fixed later.
BATCH_1 = {
    "excluded": {"team-a": set(range(1, 31))},  # already extracted
    "frozen_max": {"team-a": 25, "team-b": 20},  # slices 1..N already assigned/read; never touched
    "supplements": SUPPLEMENTS,
    "truncate": True,  # an oversized source became its own slice, cut at 150k (L2 later fixed talks)
    "frame_fixes": False,
}
# From batch 2 on: a source is never cut (rule 1, read in full): an oversized one fills its own
# slice whole. Rows listed in RECON/frame/*-fix-drop.csv (Tier 1 frame fixes) are dropped.
NO_HISTORY = {"excluded": {}, "frozen_max": {}, "supplements": [], "truncate": False, "frame_fixes": True}
FRAME = RECON / "frame"


def frame_fix_drops() -> dict[str, str]:
    """frame_id -> the drop list naming it (frame-swift-fix-drop.csv, frame-zh-talks-fix-drop.csv, ...)."""
    drops: dict[str, str] = {}
    for path in sorted(FRAME.glob("*-fix-drop.csv")):
        for row in csv.DictReader(path.open(newline="")):
            drops.setdefault(row["frame_id"], path.stem)
    return drops
SWIFT_FORUM_HOST = "forums.swift.org"
SWIFT_FORUM_MIN_MENTIONS = 3  # Swift-internal threads with a passing Rust mention read as noise


def host_of(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def is_presumed_on_subject_host(host: str, domain_subframe_hosts: set[str]) -> bool:
    return (host == "github.com" or host in ("crates.io", "docs.rs")
            or host.endswith(".rs") or host in domain_subframe_hosts)


def domain_subframe_hosts_of(batch_rows: list[dict]) -> set[str]:
    return {host_of(r["url"]) for r in batch_rows if "domain-subframes" in r["class"].split(";")}


def latest_status_by_id_url(status_csv: Path) -> dict[tuple[str, str], dict]:
    # cmd_fetch_csv appends, it never rewrites in place - a batch CSV re-run (e.g. the
    # attribution-fix re-fetch) adds a second block of rows rather than replacing the first.
    # Last occurrence per (id, url) wins, matching cache.py's own find_cached() semantics.
    latest: dict[tuple[str, str], dict] = {}
    for row in csv.DictReader(status_csv.open(newline="")):
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


def classify(text: str | None, url: str, domain_subframe_hosts: set[str]) -> str | None:
    """None if the row is kept; otherwise the drop reason."""
    if text is None:
        return "no-text"
    lower = text.lower()
    if any(marker in lower for marker in c.CHALLENGE_MARKERS):
        return "stub"
    try:
        c.validate_page_text(text, url=url)  # the cache's own floor and whole-page exemptions
    except c.FetchError:
        return "thin"
    host = host_of(url)
    mentions = lower.count("rust")
    if host == SWIFT_FORUM_HOST:
        # Swift-internal threads with a passing Rust comparison produced zero Questions in
        # every slice read so far - held to a real bar here, not the domain-subframes pass.
        return None if mentions >= SWIFT_FORUM_MIN_MENTIONS else "off-subject"
    if mentions == 0 and not is_presumed_on_subject_host(host, domain_subframe_hosts):
        return "off-subject"
    return None


def is_frozen_slice(slice_value: str, frozen_max: int) -> bool:
    if not slice_value:
        return False
    if not slice_value.isdigit():  # a supplement name (L1, L2, ...): stays frozen forever
        return True
    return int(slice_value) <= frozen_max


def load_frozen(batch: int, team: str, frozen_max: int) -> dict[int, dict]:
    """Manifest rows already assigned to a frozen slice - read, untouched, never reclassified."""
    manifest_path = BUNDLES / f"b{batch}-{team}-manifest.csv"
    if not frozen_max or not manifest_path.exists():
        return {}
    return {
        int(r["data_row"]): r
        for r in csv.DictReader(manifest_path.open(newline=""))
        if is_frozen_slice(r["slice"], frozen_max)
    }


def build(team: str, batch: int = 1, out: Path = BUNDLES) -> None:
    history = BATCH_1 if batch == 1 else NO_HISTORY
    prefix = f"b{batch}-{team}"
    batch_csv = SAMPLES / f"batch-{batch}-{team}.csv"
    batch_rows = list(csv.DictReader(batch_csv.open(newline="")))
    status_by_id_url = latest_status_by_id_url(SAMPLES / f"prefetch-b{batch}-status.csv")
    excluded = history["excluded"].get(team, set())
    domain_subframe_hosts = domain_subframe_hosts_of(batch_rows)
    frozen_max = history["frozen_max"].get(team, 0)
    frozen = load_frozen(batch, team, frozen_max)
    fixes = frame_fix_drops() if history["frame_fixes"] else {}

    manifest: list[dict] = []
    kept: list[tuple[dict, str]] = []  # (batch_row with data_row, text)
    swift_dropped = 0

    for data_row, batch_row in enumerate(batch_rows, start=1):
        if data_row in excluded:
            continue
        if data_row in frozen:
            entry = dict(frozen[data_row])
            entry["data_row"] = data_row  # normalize to int; the rest passes through as-is
            manifest.append(entry)
            continue
        status_row = status_by_id_url.get((batch_row["id"], batch_row["url"]), {})
        text = load_text(status_row)
        reason = f"frame-fix:{fixes[batch_row['id']]}" if batch_row["id"] in fixes else classify(text, batch_row["url"], domain_subframe_hosts)
        if reason == "off-subject" and host_of(batch_row["url"]) == SWIFT_FORUM_HOST:
            swift_dropped += 1
        chars = len(text) if text is not None else 0
        manifest.append({
            "data_row": data_row, "id": batch_row["id"], "url": batch_row["url"],
            "status": "dropped" if reason else "kept", "reason": reason or "", "chars": chars,
        })
        if reason is None:
            kept.append((batch_row | {"data_row": data_row}, text))

    out.mkdir(parents=True, exist_ok=True)
    for stale in out.glob(f"{prefix}-*.txt"):
        suffix = stale.stem.rsplit("-", 1)[-1]
        if suffix.isdigit() and int(suffix) > frozen_max:
            stale.unlink()  # only non-frozen numbered slices are ever regenerated; L1 is separate

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
    for i, sl in enumerate(slices, start=frozen_max + 1):
        if not sl:
            continue
        path = out / f"{prefix}-{i:02d}.txt"
        with path.open("w") as f:
            for row, text in sl:
                if history["truncate"] and len(text) > SLICE_TARGET_CHARS:
                    text = text[:SLICE_TARGET_CHARS] + "\n[... truncated at 150,000 chars ...]\n"
                header = (f"=== ROW {row['data_row']} | {row['id']} | {row['url']} | "
                          f"{row['date']} | {row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
                row_to_slice[row["data_row"]] = i

    for entry in manifest:
        if entry["data_row"] not in frozen:
            entry["slice"] = row_to_slice.get(entry["data_row"], "")

    # Frozen rows matching a SUPPLEMENTS predicate: the frozen slice file is left alone, but
    # its text may be stale (a defect fixed after that slice was assigned). Give an extractor
    # a fresh copy in a supplementary slice, and repoint the manifest at it rather than the
    # stale slice. Once assigned to a supplement, a row stays there on every future rerun even
    # if fresher text would no longer match the predicate that first caught it (e.g. an L2 talk
    # is short again after cleanup, so `chars > 150k` alone would no longer flag it).
    claimed: set[int] = set()
    supplement_counts: dict[str, int] = {}
    for name, predicate in history["supplements"]:
        already = {dr for dr in frozen if frozen[dr]["slice"] == name}
        newly = {
            dr for dr in frozen
            if dr not in claimed and dr not in already
            and predicate(batch_rows[dr - 1], frozen[dr])
        }
        rows_for_this = already | newly
        claimed |= rows_for_this
        supplement_counts[name] = len(rows_for_this)
        if not rows_for_this:
            continue
        fresh_chars = {}
        supplement_path = out / f"{prefix}-{name}.txt"
        with supplement_path.open("w") as f:
            for data_row in sorted(rows_for_this):
                batch_row = batch_rows[data_row - 1]
                status_row = status_by_id_url.get((batch_row["id"], batch_row["url"]), {})
                text = load_text(status_row) or ""
                fresh_chars[data_row] = len(text)
                header = (f"=== ROW {data_row} | {batch_row['id']} | {batch_row['url']} | "
                          f"{batch_row['date']} | {batch_row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
        for entry in manifest:
            if entry["data_row"] in fresh_chars:
                entry["slice"] = name
                entry["chars"] = fresh_chars[entry["data_row"]]  # the frozen row's chars was stale

    manifest.sort(key=lambda e: int(e["data_row"]))
    manifest_path = out / f"{prefix}-manifest.csv"
    with manifest_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slice", "data_row", "id", "url", "status", "reason", "chars"])
        w.writeheader()
        for entry in manifest:
            w.writerow({k: entry[k] for k in w.fieldnames})

    n_new_slices = sum(1 for sl in slices if sl)
    n_kept = sum(1 for e in manifest if e["status"] == "kept")
    n_dropped = len(manifest) - n_kept
    supplement_summary = ", ".join(f"{n} in {name}" for name, n in supplement_counts.items())
    print(f"{team}: {len(manifest)} rows total ({len(frozen)} frozen, {len(excluded)} excluded), "
          f"{n_kept} kept, {n_dropped} dropped ({swift_dropped} by the swift-forum rule), "
          f"{n_new_slices} new slices (numbered {frozen_max + 1}+), "
          f"supplements: {supplement_summary} -> {manifest_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("team", choices=["team-a", "team-b"])
    parser.add_argument("--batch", type=int, default=1)
    parser.add_argument("--out", type=Path, default=BUNDLES)
    args = parser.parse_args()
    build(args.team, args.batch, args.out)

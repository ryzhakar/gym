"""Cut a fetched batch into read-sized text bundles for extraction agents.

Usage: uv run python scripts/research/bundle.py <team-a|team-b>

Input: samples/batch-1-team-{team}.csv (data rows, in order) and the shared cache
CACHE/<key>.txt. Each batch row's fetch status comes from samples/prefetch-b1-status.csv,
looked up by (id, url) - fetch-csv appends rather than rewrites, so a re-fetched row may
have more than one status line; the last one (most recent) wins.

For each row, keep only if its cached text exists, is not a bot/login-wall stub, and is
>=1,500 chars; otherwise it is dropped with one reason: no-text, stub, thin. A row on
forums.swift.org is kept only with >=3 "rust" mentions, else dropped as off-subject (a
stricter, host-specific override - Swift-internal threads with a passing Rust comparison
produced zero Questions in every slice read). Every other row with zero "rust" mentions is
also dropped as off-subject, unless its URL is a github.com repo, a *.rs / docs.rs /
crates.io host, or one of this batch's own class=domain-subframes hosts (presumed on-subject
even at zero mentions, since the frame put it in scope on purpose). Kept rows are cut, in
CSV order, into ~150k-char slices, never splitting a source (an oversized source becomes its
own truncated slice).

Some slices are frozen (FROZEN_SLICE_MAX below) - already assigned and read by an extractor.
Their manifest rows and slice files are left untouched; only unassigned rows are
reclassified and packed into new slices numbered above the frozen range. Exception: a frozen
row of class=hn-lobsters (SUPPLEMENT_CLASS) whose cached text was refreshed after its slice
was assigned gets a fresh copy written to a supplementary b1-{team}-L1.txt, and the manifest's
slice column for that row is repointed at "L1" - the original numbered slice file is still
left alone.

Output: samples/bundles/b1-{team}-{jj}.txt (one file per slice, each source preceded by a
`=== ROW n | id | url | date | class ===` header) and samples/bundles/b1-{team}-manifest.csv
(slice,data_row,id,url,status,reason,chars).
"""
import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
import cache as c  # noqa: E402 - local module, path set above

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
SAMPLES = RECON / "samples"
STATUS_CSV = SAMPLES / "prefetch-b1-status.csv"
BUNDLES = SAMPLES / "bundles"
SLICE_TARGET_CHARS = 150_000
EXCLUDED_DATA_ROWS = {"team-a": set(range(1, 31))}  # already extracted
FROZEN_SLICE_MAX = {"team-a": 20, "team-b": 16}  # slices 1..N already assigned/read; never touched
SUPPLEMENT_CLASS = "hn-lobsters"  # frozen rows of this class get a fresh copy in slice L1
SWIFT_FORUM_HOST = "forums.swift.org"
SWIFT_FORUM_MIN_MENTIONS = 3  # Swift-internal threads with a passing Rust mention read as noise


def host_of(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def is_presumed_on_subject_host(host: str, domain_subframe_hosts: set[str]) -> bool:
    return (host == "github.com" or host in ("crates.io", "docs.rs")
            or host.endswith(".rs") or host in domain_subframe_hosts)


def domain_subframe_hosts_of(batch_rows: list[dict]) -> set[str]:
    return {host_of(r["url"]) for r in batch_rows if "domain-subframes" in r["class"].split(";")}


def latest_status_by_id_url() -> dict[tuple[str, str], dict]:
    # cmd_fetch_csv appends, it never rewrites in place - a batch CSV re-run (e.g. the
    # attribution-fix re-fetch) adds a second block of rows rather than replacing the first.
    # Last occurrence per (id, url) wins, matching cache.py's own find_cached() semantics.
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


def classify(text: str | None, url: str, domain_subframe_hosts: set[str]) -> str | None:
    """None if the row is kept; otherwise the drop reason."""
    if text is None:
        return "no-text"
    lower = text.lower()
    if any(marker in lower for marker in c.CHALLENGE_MARKERS):
        return "stub"
    if len(text) < c.MIN_PAGE_CHARS:
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
    if slice_value == "L1":  # already-supplemented row from a frozen slice; stays frozen
        return True
    return bool(slice_value) and int(slice_value) <= frozen_max


def load_frozen(team: str) -> dict[int, dict]:
    """Manifest rows already assigned to a frozen slice - read, untouched, never reclassified."""
    manifest_path = BUNDLES / f"b1-{team}-manifest.csv"
    frozen_max = FROZEN_SLICE_MAX.get(team, 0)
    if not frozen_max or not manifest_path.exists():
        return {}
    return {
        int(r["data_row"]): r
        for r in csv.DictReader(manifest_path.open(newline=""))
        if is_frozen_slice(r["slice"], frozen_max)
    }


def build(team: str) -> None:
    batch_csv = SAMPLES / f"batch-1-{team}.csv"
    batch_rows = list(csv.DictReader(batch_csv.open(newline="")))
    status_by_id_url = latest_status_by_id_url()
    excluded = EXCLUDED_DATA_ROWS.get(team, set())
    domain_subframe_hosts = domain_subframe_hosts_of(batch_rows)
    frozen = load_frozen(team)
    frozen_max = FROZEN_SLICE_MAX.get(team, 0)

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
        reason = classify(text, batch_row["url"], domain_subframe_hosts)
        if reason == "off-subject" and host_of(batch_row["url"]) == SWIFT_FORUM_HOST:
            swift_dropped += 1
        chars = len(text) if text is not None else 0
        manifest.append({
            "data_row": data_row, "id": batch_row["id"], "url": batch_row["url"],
            "status": "dropped" if reason else "kept", "reason": reason or "", "chars": chars,
        })
        if reason is None:
            kept.append((batch_row | {"data_row": data_row}, text))

    BUNDLES.mkdir(parents=True, exist_ok=True)
    for stale in BUNDLES.glob(f"b1-{team}-*.txt"):
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
        path = BUNDLES / f"b1-{team}-{i:02d}.txt"
        with path.open("w") as f:
            for row, text in sl:
                if len(text) > SLICE_TARGET_CHARS:
                    text = text[:SLICE_TARGET_CHARS] + "\n[... truncated at 150,000 chars ...]\n"
                header = (f"=== ROW {row['data_row']} | {row['id']} | {row['url']} | "
                          f"{row['date']} | {row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
                row_to_slice[row["data_row"]] = i

    for entry in manifest:
        if entry["data_row"] not in frozen:
            entry["slice"] = row_to_slice.get(entry["data_row"], "")

    # Frozen rows of SUPPLEMENT_CLASS: the frozen slice file is left alone, but its text may
    # be stale (a defect fixed after that slice was assigned). Give an extractor a fresh copy
    # in a supplementary slice L1, and repoint the manifest at it rather than the stale slice.
    supplement_rows = [
        (data_row, batch_rows[data_row - 1]) for data_row in frozen
        if SUPPLEMENT_CLASS in batch_rows[data_row - 1]["class"].split(";")
    ]
    if supplement_rows:
        fresh_chars = {}
        supplement_path = BUNDLES / f"b1-{team}-L1.txt"
        with supplement_path.open("w") as f:
            for data_row, batch_row in sorted(supplement_rows):
                status_row = status_by_id_url.get((batch_row["id"], batch_row["url"]), {})
                text = load_text(status_row) or ""
                fresh_chars[data_row] = len(text)
                header = (f"=== ROW {data_row} | {batch_row['id']} | {batch_row['url']} | "
                          f"{batch_row['date']} | {batch_row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
        for entry in manifest:
            if entry["data_row"] in fresh_chars:
                entry["slice"] = "L1"
                entry["chars"] = fresh_chars[entry["data_row"]]  # the frozen row's chars was stale

    manifest.sort(key=lambda e: int(e["data_row"]))
    manifest_path = BUNDLES / f"b1-{team}-manifest.csv"
    with manifest_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slice", "data_row", "id", "url", "status", "reason", "chars"])
        w.writeheader()
        for entry in manifest:
            w.writerow({k: entry[k] for k in w.fieldnames})

    n_new_slices = sum(1 for sl in slices if sl)
    n_kept = sum(1 for e in manifest if e["status"] == "kept")
    n_dropped = len(manifest) - n_kept
    print(f"{team}: {len(manifest)} rows total ({len(frozen)} frozen, {len(excluded)} excluded), "
          f"{n_kept} kept, {n_dropped} dropped ({swift_dropped} by the swift-forum rule), "
          f"{n_new_slices} new slices (numbered {frozen_max + 1}+), "
          f"{len(supplement_rows)} rows refreshed in slice L1 -> {manifest_path}")


if __name__ == "__main__":
    build(sys.argv[1])

"""Cut a fetched batch into read-sized text bundles for extraction agents.

Usage: uv run python scripts/research/bundle.py <team-a|team-b>

Input: samples/batch-1-team-{team}.csv (data rows, in order), samples/prefetch-b1-status.csv
(one status row per batch row, in the same order: team-a's 198 rows first, then team-b's 198),
and the shared cache CACHE/<key>.txt.

For each row, keep only if its cached text exists, is not a bot/login-wall stub, and is
>=1,500 chars; otherwise it is dropped with one reason: no-text, stub, thin. A row with zero
"rust" mentions (case-insensitive) is also dropped as off-subject, unless its URL is a
github.com repo, a *.rs / docs.rs / crates.io host, or one of this batch's own
class=domain-subframes hosts (any host such a row appears under is presumed on-subject even
at zero mentions, since the frame put it in scope on purpose). Kept rows are cut, in CSV
order, into ~150k-char slices, never splitting a source (an oversized source becomes its own
truncated slice).

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


def host_of(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def is_presumed_on_subject_host(host: str, domain_subframe_hosts: set[str]) -> bool:
    return (host == "github.com" or host in ("crates.io", "docs.rs")
            or host.endswith(".rs") or host in domain_subframe_hosts)


def domain_subframe_hosts_of(batch_rows: list[dict]) -> set[str]:
    return {host_of(r["url"]) for r in batch_rows if "domain-subframes" in r["class"].split(";")}


def team_status_rows(team: str) -> list[dict]:
    # fetch-csv appended team-a's rows first, then team-b's, each in its batch CSV's row
    # order; team-a's own row count is the exact split point (not an assumed 50/50 split).
    all_rows = list(csv.DictReader(STATUS_CSV.open(newline="")))
    n_a = sum(1 for _ in csv.DictReader((SAMPLES / "batch-1-team-a.csv").open(newline="")))
    return all_rows[:n_a] if team == "team-a" else all_rows[n_a:]


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
    if "rust" not in lower and not is_presumed_on_subject_host(host_of(url), domain_subframe_hosts):
        return "off-subject"
    return None


def build(team: str) -> None:
    batch_csv = SAMPLES / f"batch-1-{team}.csv"
    batch_rows = list(csv.DictReader(batch_csv.open(newline="")))
    status_rows = team_status_rows(team)
    assert len(batch_rows) == len(status_rows), (
        f"{team}: {len(batch_rows)} batch rows vs {len(status_rows)} status rows"
    )
    excluded = EXCLUDED_DATA_ROWS.get(team, set())
    domain_subframe_hosts = domain_subframe_hosts_of(batch_rows)

    manifest: list[dict] = []
    kept: list[tuple[dict, str]] = []  # (batch_row with data_row, text)

    for data_row, (batch_row, status_row) in enumerate(zip(batch_rows, status_rows), start=1):
        if data_row in excluded:
            continue
        text = load_text(status_row)
        reason = classify(text, batch_row["url"], domain_subframe_hosts)
        chars = len(text) if text is not None else 0
        manifest.append({
            "data_row": data_row, "id": batch_row["id"], "url": batch_row["url"],
            "status": "dropped" if reason else "kept", "reason": reason or "", "chars": chars,
        })
        if reason is None:
            kept.append((batch_row | {"data_row": data_row}, text))

    BUNDLES.mkdir(parents=True, exist_ok=True)
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
        entry["slice"] = row_to_slice.get(entry["data_row"], "")

    manifest_path = BUNDLES / f"b1-{team}-manifest.csv"
    with manifest_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slice", "data_row", "id", "url", "status", "reason", "chars"])
        w.writeheader()
        for entry in manifest:
            w.writerow({k: entry[k] for k in w.fieldnames})

    n_slices = sum(1 for sl in slices if sl)
    n_kept = sum(1 for e in manifest if e["status"] == "kept")
    n_dropped = len(manifest) - n_kept
    print(f"{team}: {len(manifest)} rows processed ({len(excluded)} excluded), "
          f"{n_kept} kept, {n_dropped} dropped, {n_slices} slices -> {manifest_path}")


if __name__ == "__main__":
    build(sys.argv[1])

"""Batch 1 re-cuts byte-identical after the bundlers took a batch parameter.

Run: `uv run --with pytest pytest scripts/research/test_bundle.py`. Reads the shared cache; writes only to tmp.
"""

from __future__ import annotations

from pathlib import Path

import csv

import pytest

from gym.research import books, bundle
from gym.research import cache as c

BUNDLE_OUTPUTS = ("b1-team-b-21.txt", "b1-team-b-L1.txt", "b1-team-b-manifest.csv")
BOOKS_OUTPUTS = ("b1-team-a-B01.txt", "b1-team-a-B-manifest.csv")


def recon_files_present(samples: Path, team: str, outputs: tuple[str, ...]) -> bool:
    """The batch-1 inputs, every cached text its status rows name, and the expected outputs all exist."""
    status_csv = samples / "prefetch-b1-status.csv"
    inputs = [samples / f"batch-1-{team}.csv", status_csv, *(samples / "bundles" / name for name in outputs)]
    if not all(p.is_file() for p in inputs):
        return False
    keys = {row["key"] for row in csv.DictReader(status_csv.open(newline="")) if row["key"]}
    return all((c.CACHE / f"{k}.txt").is_file() or (c.CACHE / f"{k}.abstract.txt").is_file() for k in keys)


@pytest.mark.skipif(
    not recon_files_present(bundle.SAMPLES, "team-b", BUNDLE_OUTPUTS),
    reason=f"live, gitignored recon data or cache absent at {bundle.SAMPLES}, {c.CACHE}",
)
def test_bundle_recuts_batch_1_team_b(tmp_path: Path) -> None:
    bundle.build("team-b", 1, tmp_path)
    for name in BUNDLE_OUTPUTS:
        assert (tmp_path / name).read_bytes() == (bundle.BUNDLES / name).read_bytes(), name


@pytest.mark.skipif(
    not recon_files_present(books.SAMPLES, "team-a", BOOKS_OUTPUTS),
    reason=f"live, gitignored recon data or cache absent at {books.SAMPLES}, {c.CACHE}",
)
def test_books_recuts_batch_1_team_a(tmp_path: Path) -> None:
    books.build("team-a", 1, tmp_path)
    for name in BOOKS_OUTPUTS:
        assert (tmp_path / name).read_bytes() == (books.BUNDLES / name).read_bytes(), name

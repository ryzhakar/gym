"""Batch 1 re-cuts byte-identical after the bundlers took a batch parameter.

Run: `uv run --with pytest pytest scripts/research/test_bundle.py`. Reads the shared cache; writes only to tmp.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gym.research import books, bundle


@pytest.mark.skipif(
    not bundle.BUNDLES.exists(),
    reason=f"live, gitignored recon data absent at {bundle.BUNDLES}",
)
def test_bundle_recuts_batch_1_team_b(tmp_path: Path) -> None:
    bundle.build("team-b", 1, tmp_path)
    for name in ("b1-team-b-21.txt", "b1-team-b-L1.txt", "b1-team-b-manifest.csv"):
        assert (tmp_path / name).read_bytes() == (bundle.BUNDLES / name).read_bytes(), name


@pytest.mark.skipif(
    not books.BUNDLES.exists(),
    reason=f"live, gitignored recon data absent at {books.BUNDLES}",
)
def test_books_recuts_batch_1_team_a(tmp_path: Path) -> None:
    books.build("team-a", 1, tmp_path)
    for name in ("b1-team-a-B01.txt", "b1-team-a-B-manifest.csv"):
        assert (tmp_path / name).read_bytes() == (books.BUNDLES / name).read_bytes(), name

"""Test for the map site generator. Run: `uv run pytest tests/map/test_site.py`."""

from __future__ import annotations

from pathlib import Path

from gym.map.site import main as build_site
from gym.paths import ROOT


def test_site_builds_on_rust_map(tmp_path: Path) -> None:
    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    assert out.exists()
    assert out.stat().st_size > 100_000
    # Spec asked for the literal string "Voice 1"; it never appears in the
    # static file (or in the prototype's own committed index.html) because
    # voice labels ("Voice " + index) are computed client-side by the page's
    # JS, not baked in by the Python builder. Asserting the JS fragment that
    # does the labelling instead, verbatim from the prototype and unchanged
    # by this migration. See migrate-map-report.md for the full note.
    assert 'return "Voice " + (idx >= 0 ? idx + 1 : "?");' in out.read_text(encoding="utf-8")

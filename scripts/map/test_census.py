"""Tests for the nothing-new census gate. Run: `uv run --with pytest pytest scripts/map/test_census.py`."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from census import census_team  # noqa: E402

HEADER = "frame_id,url,read,locator_span,new_questions,claims,minutes\n"


def write(team_dir: Path, name: str, text: str) -> None:
    team_dir.mkdir(parents=True, exist_ok=True)
    (team_dir / name).write_text(text, encoding="utf-8")


def section(frame_id: str, code: str, reason: str) -> str:
    return f"## {frame_id} — t (2025-01-01, en)\n### Nothing new\nreason-code: {code}\nreason: {reason}\n\n"


def test_passing_flagged_and_superseded_rows(tmp_path: Path) -> None:
    team = tmp_path / "team-a"
    write(team, "readlog-b2-01.csv", HEADER
          + "f000001,u,yes,all,0,0,5\n"
          + "f000002,u,yes,all,0,0,5\n"
          + "f000003,u,yes,all,1,2,5\n"
          + "f000004,u,yes,all,0,0,5\n"
          + "f000005,u,yes,a, b,0,0,5\n"
          + "f000006,u,unreachable,none,0,0,1\n")
    write(team, "extract-b2-01.md",
          section("f000001", "off-subject", "The post is about Go generics.")
          + section("f000002", "no-decision", "Only one voice speaks and nobody argues back.")
          + "## f000003 — t\n### Questions\n- Q: x\n\n"
          + section("f000004", "single-voice", "A lone opinion."))
    flags, population, codes = census_team(team, 2)
    flagged = {frame_id for frame_id, _ in flags}
    assert population == [("f000001", "off-subject")]
    assert flagged == {"f000002", "f000004", "f000005"}

    write(team, "readlog-b2-fix1.csv", HEADER + "f000002,u,yes,all,0,0,5\nf000004,u,yes,all,1,1,5\n")
    write(team, "extract-b2-fix1.md", section("f000002", "no-decision", "Install steps with no stated reason."))
    flags, population, codes = census_team(team, 2)
    assert population == [("f000001", "off-subject"), ("f000002", "no-decision")]
    assert {frame_id for frame_id, _ in flags} == {"f000005"}
    assert codes["no-decision"] == 1

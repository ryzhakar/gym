"""Tests for check_record.py: a clean file passes, a malformed row or header is caught as FAIL.

Run: `uv run pytest scripts/train/tests/test_check_record.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_record  # noqa: E402
import record_schema  # noqa: E402


@pytest.fixture(autouse=True)
def isolated_record_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(record_schema, "RECORD_DIR", tmp_path)
    return tmp_path


def write(path: Path, name: str, rows: list[str]) -> None:
    header = ",".join(record_schema.FILES[name])
    (path / f"{name}.csv").write_text("\n".join([header, *rows]) + ("\n" if rows or True else ""), encoding="utf-8")


def test_clean_file_has_no_findings(isolated_record_dir: Path) -> None:
    write(isolated_record_dir, "queue", ["2026-09-28T10:00,delayed_probe,unit-1,2026-10-05"])
    assert check_record.check_file("queue") == []


def test_bad_enum_is_a_fail(isolated_record_dir: Path) -> None:
    write(isolated_record_dir, "queue", ["2026-09-28T10:00,not_a_kind,unit-1,2026-10-05"])
    findings = check_record.check_file("queue")
    assert len(findings) == 1
    assert "not one of" in findings[0]


def test_bad_date_is_a_fail(isolated_record_dir: Path) -> None:
    write(isolated_record_dir, "queue", ["2026-09-28T10:00,delayed_probe,unit-1,not-a-date"])
    findings = check_record.check_file("queue")
    assert len(findings) == 1
    assert "not YYYY-MM-DD" in findings[0]


def test_timestamps_going_backward_is_a_fail(isolated_record_dir: Path) -> None:
    write(
        isolated_record_dir,
        "queue",
        [
            "2026-09-28T10:00,delayed_probe,unit-1,2026-10-05",
            "2026-09-28T09:00,delayed_probe,unit-2,2026-10-05",
        ],
    )
    findings = check_record.check_file("queue")
    assert len(findings) == 1
    assert "goes back" in findings[0]


def test_wrong_header_is_a_fail(isolated_record_dir: Path) -> None:
    (isolated_record_dir / "queue.csv").write_text("wrong,header\n", encoding="utf-8")
    findings = check_record.check_file("queue")
    assert len(findings) == 1
    assert "header" in findings[0]


def test_missing_file_is_a_fail(isolated_record_dir: Path) -> None:
    findings = check_record.check_file("sessions")
    assert len(findings) == 1
    assert "does not exist" in findings[0]


def test_main_exits_1_on_any_fail(isolated_record_dir: Path, capsys: pytest.CaptureFixture) -> None:
    for name in record_schema.FILES:
        write(isolated_record_dir, name, [])
    write(isolated_record_dir, "queue", ["2026-09-28T10:00,not_a_kind,unit-1,2026-10-05"])
    assert check_record.main() == 1
    assert "1 FAIL" in capsys.readouterr().out


def test_main_exits_0_when_all_clean(isolated_record_dir: Path) -> None:
    for name in record_schema.FILES:
        write(isolated_record_dir, name, [])
    assert check_record.main() == 0


def test_ladder_gap_turn_with_a_blank_note_is_a_fail(isolated_record_dir: Path) -> None:
    write(isolated_record_dir, "turns", ["2026-09-28T10:00,2026-09-28T09:55,1,ladder-gap,unit-1-unshown,5.00,,"])
    findings = check_record.check_file("turns")
    assert len(findings) == 1
    assert "note is required" in findings[0]


def test_non_ladder_gap_turn_with_a_note_is_a_fail(isolated_record_dir: Path) -> None:
    write(isolated_record_dir, "turns", ["2026-09-28T10:00,2026-09-28T09:55,1,hint-1,unit-1-attempt,5.00,hint,should not be here"])
    findings = check_record.check_file("turns")
    assert len(findings) == 1
    assert "note must be empty" in findings[0]


def test_ladder_gap_turn_with_a_note_is_clean(isolated_record_dir: Path) -> None:
    write(
        isolated_record_dir,
        "turns",
        ['2026-09-28T10:00,2026-09-28T09:55,1,ladder-gap,unit-1-unshown,5.00,,"ladder gap: unit-1-unshown"'],
    )
    assert check_record.check_file("turns") == []

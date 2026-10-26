"""gym records check: the four checks memento lacks, against tmp record trees; and the repo's own records."""

from __future__ import annotations

import subprocess
from collections.abc import Callable
from pathlib import Path

import pytest
from typer.testing import CliRunner

from gym.records import check_records
from gym.records.cli import app

runner = CliRunner()
Tree = Callable[[dict[str, str]], Path]


@pytest.fixture
def tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Tree:
    """`tree({path: text})` writes a git-tracked tree and points the checker's root at it."""
    monkeypatch.setattr(check_records, "ROOT", tmp_path)
    monkeypatch.setattr(check_records, "SCHEMA_PATH", tmp_path / ".claude/memento.yaml")

    def build(files: dict[str, str]) -> Path:
        for name, text in files.items():
            (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
            (tmp_path / name).write_text(text, encoding="utf-8")
        git = ["git", "-C", str(tmp_path)]
        subprocess.run([*git, "init", "-q"], check=True)
        subprocess.run([*git, "add", "-A"], check=True)
        return tmp_path

    return build


SCHEMA = {
    "kinds": {
        "map": {"home": ".claude/memento-map.md"},
        "opinion_map": {"home": "docs/opinion-map.md"},
        "subject": {"home": "docs/subjects/*.md"},
        "directive": {"home": "docs/conventions.md"},
        "charter": {"home": "CLAUDE.md"},
        "frame": {"home": "docs/ground-truth.md"},
        "fact": {"home": "docs/capabilities.md"},
        "change": {"home": "docs/architecture_log.md"},
    }
}


def wheres(findings) -> list[str]:
    return [finding.where for finding in findings]


def test_check_reports_zero_fail_on_the_repo() -> None:
    result = runner.invoke(app, ["check"])
    assert result.exit_code == 0
    assert "records: 0 FAIL" in result.stdout


def test_a_map_without_a_dated_audit_line_fails(tree: Tree) -> None:
    tree({".claude/memento-map.md": "| path | kind |\n"})
    assert wheres(check_records.check_audited(SCHEMA)) == [".claude/memento-map.md"]


def test_a_map_with_a_dated_audit_line_passes(tree: Tree) -> None:
    tree({".claude/memento-map.md": "Audited 2026-10-26.\n\n| path | kind |\n"})
    assert list(check_records.check_audited(SCHEMA)) == []


def test_a_retired_entry_must_name_an_archived_file_that_exists_and_a_gone_original(tree: Tree) -> None:
    tree({"archive/a.md": "x", "old.md": "x", "docs/new.md": "x"})
    schema = {
        "retired": [
            {"path": "archive/missing.md", "was": "gone.md", "superseded_by": "docs/new.md"},
            {"path": "archive/a.md", "was": "old.md", "superseded_by": "docs/new.md, docs/absent.md"},
        ]
    }
    messages = [finding.message for finding in check_records.check_retired(schema)]
    assert messages == [
        "the archived file does not exist",
        "'old.md' still exists beside its archived copy",
        "superseded_by names 'docs/absent.md', which does not exist",
    ]


def test_a_subject_pointing_at_a_missing_file_or_heading_fails(tree: Tree) -> None:
    tree(
        {
            "docs/opinion-map.md": "# Map\n\n## Real heading\n",
            "docs/subjects/rust.md": "see docs/gone.md\n\nsee opinion-map § Real heading\n\nsee opinion-map § No such\n",
            "docs/conventions.md": "",
        }
    )
    files = check_records.committable_files()
    messages = [finding.message for finding in check_records.check_pointers(SCHEMA, files)]
    assert messages == ["points at 'docs/gone.md', which does not exist", "'opinion-map § No such' names no heading in docs/opinion-map.md"]


def test_pointers_in_kinds_memento_checks_are_left_alone(tree: Tree) -> None:
    tree({"CLAUDE.md": "see docs/gone.md\n", "docs/conventions.md": "see docs/gone.md\n", "docs/opinion-map.md": "", "docs/subjects/rust.md": ""})
    assert list(check_records.check_pointers(SCHEMA, check_records.committable_files())) == []


def test_a_hard_wrapped_subject_fails_and_a_wrapped_charter_does_not(tree: Tree) -> None:
    tree({"CLAUDE.md": "one line\ncontinued\n", "docs/subjects/rust.md": "# T\n\nfirst line\ncontinued here\n", "docs/opinion-map.md": "fine\n"})
    findings = list(check_records.check_no_hard_wrap(SCHEMA, check_records.committable_files()))
    assert wheres(findings) == ["docs/subjects/rust.md:4"]


def test_an_untracked_record_file_fails_and_an_untracked_file_outside_the_record_space_does_not(tree: Tree) -> None:
    root = tree({"docs/a.md": "x"})
    (root / "docs/b.md").write_text("x", encoding="utf-8")
    (root / "src").mkdir()
    (root / "src/c.py").write_text("x", encoding="utf-8")
    assert wheres(check_records.check_untracked()) == ["docs/b.md"]


def test_an_ignored_file_is_not_untracked(tree: Tree) -> None:
    root = tree({".gitignore": "docs/orchestration_log/recon/\n"})
    (root / "docs/orchestration_log/recon").mkdir(parents=True)
    (root / "docs/orchestration_log/recon/n.md").write_text("x", encoding="utf-8")
    assert list(check_records.check_untracked()) == []


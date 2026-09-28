"""Round-trip test for session.py: close writes the session and queue rows; open runs a due probe
and hands off to the next unit, staging its practice items into a session-scoped work copy.

Run: `uv run pytest scripts/train/tests/test_session.py`. Needs `cargo` on PATH.
"""
from __future__ import annotations

import csv
import json
import re
import shlex
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import log  # noqa: E402
import probe  # noqa: E402
import record_schema  # noqa: E402
import session  # noqa: E402

CARGO_MISSING = shutil.which("cargo") is None


@pytest.fixture(autouse=True)
def isolated_paths(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    record_dir = tmp_path / "record"
    record_dir.mkdir()
    for name, columns in record_schema.FILES.items():
        (record_dir / f"{name}.csv").write_text(",".join(columns) + "\n", encoding="utf-8")
    monkeypatch.setattr(record_schema, "RECORD_DIR", record_dir)
    monkeypatch.setattr(probe, "WORK_ROOT", tmp_path / "work")
    return tmp_path


def read_rows(name: str) -> list[dict[str, str]]:
    with record_schema.file_path(name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_close_writes_session_and_queue_rows() -> None:
    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    sessions = read_rows("sessions")
    assert len(sessions) == 1
    assert sessions[0]["units"] == "unit-1"
    assert sessions[0]["gap_days"] == "0.0"

    queue = read_rows("queue")
    kinds = {row["kind"]: row for row in queue}
    assert kinds["delayed_probe"]["unit"] == "unit-1"
    assert kinds["delayed_probe"]["due_date"] == (date.today() + timedelta(days=7)).isoformat()
    assert kinds["next_unit"]["unit"] == "unit-2"


def test_open_with_no_due_probe_hands_off_to_the_next_unit(isolated_paths: Path, capsys: pytest.CaptureFixture) -> None:
    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    session.open_session(items_root=isolated_paths / "items")
    out = capsys.readouterr().out
    assert "due delayed probes run: none" in out
    assert "next unit: unit-2" in out


def make_practice_item(items_root: Path, unit: str, name: str) -> None:
    """A minimal real crate under `<unit>/<name>/` — attempt/reuse-1/reuse-2/unshown all share this shape."""
    base = items_root / unit / name
    (base / "src").mkdir(parents=True)
    (base / "Cargo.toml").write_text(
        f'[package]\nname = "{name.replace("-", "_")}_crate"\nversion = "0.1.0"\nedition = "2021"\n\n[workspace]\n',
        encoding="utf-8",
    )
    (base / "src" / "lib.rs").write_text("pub fn stub() {}\n", encoding="utf-8")


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_open_stages_the_next_units_practice_items_leaving_items_byte_identical(
    isolated_paths: Path,
) -> None:
    items_root = isolated_paths / "items"
    make_practice_item(items_root, "unit-2", "attempt")
    make_practice_item(items_root, "unit-2", "reuse-1")
    before = {p.relative_to(items_root): p.read_bytes() for p in sorted(items_root.rglob("*")) if p.is_file()}

    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    session.open_session(items_root=items_root)

    staged_attempt = probe.WORK_ROOT
    matches = list(staged_attempt.glob("*/unit-2/practice/attempt/src/lib.rs"))
    assert len(matches) == 1
    assert matches[0].read_text(encoding="utf-8") == "pub fn stub() {}\n"
    assert list(staged_attempt.glob("*/unit-2/practice/reuse-1/src/lib.rs"))

    after = {p.relative_to(items_root): p.read_bytes() for p in sorted(items_root.rglob("*")) if p.is_file()}
    assert after == before


def make_probe_b_problem(items_root: Path, unit: str, problem: str = "p1") -> None:
    """A minimal real crate under `<unit>/probe-b/<problem>/`, plus its `key/` mirror with a
    held-out test — the shape probe.py's rewritten grader expects (P3 items/README.md § Layout)."""
    cargo_toml = '[package]\nname = "probe_b_crate"\nversion = "0.1.0"\nedition = "2021"\n\n[workspace]\n'
    lib_rs = "pub fn triple(n: i32) -> i32 {\n    n * 3\n}\n"
    visible_rs = "use probe_b_crate::triple;\n\n#[test]\nfn visible() {\n    assert_eq!(triple(2), 6);\n}\n"
    heldout_rs = "use probe_b_crate::triple;\n\n#[test]\nfn heldout() {\n    assert_eq!(triple(3), 9);\n}\n"
    for base in (items_root / unit / "probe-b" / problem, items_root / unit / "key" / "probe-b" / problem):
        (base / "src").mkdir(parents=True)
        (base / "tests").mkdir(parents=True)
        (base / "Cargo.toml").write_text(cargo_toml, encoding="utf-8")
        (base / "src" / "lib.rs").write_text(lib_rs, encoding="utf-8")
        (base / "tests" / "visible.rs").write_text(visible_rs, encoding="utf-8")
    (items_root / unit / "probe-b" / problem / "spec.md").write_text("Edit: src/lib.rs\n", encoding="utf-8")
    (items_root / unit / "key" / "probe-b" / problem / "tests" / "heldout.rs").write_text(heldout_rs, encoding="utf-8")


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_open_runs_a_due_delayed_probe_then_hands_off(isolated_paths: Path, capsys: pytest.CaptureFixture) -> None:
    items_root = isolated_paths / "items"
    make_probe_b_problem(items_root, "unit-1")

    log.append_row(
        "queue",
        log.build_row("queue", {"kind": "delayed_probe", "unit": "unit-1", "due_date": "2020-01-01"}),
    )
    log.append_row(
        "queue",
        log.build_row("queue", {"kind": "next_unit", "unit": "unit-2", "due_date": date.today().isoformat()}),
    )

    session.open_session(items_root=items_root, wait=lambda: None, clock=lambda: 0.0)

    items = read_rows("items")
    assert len(items) == 1
    assert items[0]["unit"] == "unit-1"
    assert items[0]["kind"] == "probe-delayed"

    out = capsys.readouterr().out
    assert "due delayed probes run: ['unit-1']" in out
    assert "next unit: unit-2" in out


def settings_from_command(command: str) -> dict:
    tokens = shlex.split(command)
    settings_path = Path(tokens[tokens.index("--settings") + 1])
    return json.loads(settings_path.read_text(encoding="utf-8"))


def test_launch_command_carries_the_full_allowlist() -> None:
    command = session.trainer_launch_command("unit-1", "sess-1")
    settings = settings_from_command(command)

    assert "--permission-mode dontAsk" in command
    assert "--agent rust-trainer" in command

    allow, deny = settings["permissions"]["allow"], settings["permissions"]["deny"]
    assert session.KEY_DENY_PATTERN in deny
    assert "Read(**/probe-*/**)" in deny
    assert "Bash(cargo run*)" in deny
    assert "Bash(git *)" in deny
    unit_dir, crate, record = session.unit_paths("unit-1", "sess-1")
    for suffix in ("attempt.md", "example.md", "hints.yaml"):
        assert f"Read({unit_dir}/{suffix})" in allow
    # reuse-1/reuse-2/unshown/attempt come from the staged copy (CRATE), never read straight off items/
    for suffix in ("reuse-1/**", "reuse-2/**", "unshown/**", "attempt/**"):
        assert f"Read({unit_dir}/{suffix})" not in allow
    assert f"Read({crate}/**)" in allow
    assert f"Read({record}/**)" in allow
    assert f"Glob({crate}/**)" in allow
    assert "Bash(cargo check*)" in allow
    assert "Bash(cargo test*)" in allow
    # not a blanket Bash allowance — the log.py entry names the exact invocation
    assert not any(pattern == "Bash(*)" for pattern in allow)

    hook = settings["hooks"]["PreToolUse"][0]
    assert hook["matcher"] == "Bash|Read|Glob"
    assert str(session.TRAINER_GUARD) in hook["hooks"][0]["command"]
    assert f"--crate {crate}" in hook["hooks"][0]["command"]

    # the settings file itself exists, generated fresh (not committed, same as the crate tree)
    tokens = shlex.split(command)
    assert Path(tokens[tokens.index("--settings") + 1]).is_file()


def pattern_matches(pattern: str, path: str) -> bool:
    """Whether a `Tool(glob)` permission pattern's glob matches `path` — `**` any run of characters,
    a lone `*` no `/`. A static check of the pattern text session.py emits, not a live claude-CLI
    run: no nested `claude` session was spawned to confirm the real matcher behaves this way."""
    inner = pattern[pattern.index("(") + 1 : -1]
    out, i = [], 0
    while i < len(inner):
        if inner[i : i + 2] == "**":
            out.append(".*")
            i += 2
        elif inner[i] == "*":
            out.append("[^/]*")
            i += 1
        else:
            out.append(re.escape(inner[i]))
            i += 1
    return re.fullmatch("".join(out), path) is not None


def test_a_read_of_any_key_path_is_denied_by_the_pattern() -> None:
    unit_dir, _crate, _record = session.unit_paths("unit-1", "sess-1")
    key_paths = [
        f"{unit_dir}/probe-a/key/solution.rs",
        f"{unit_dir}/key/notes.md",
        f"{session.ROOT}/training/rust/items/baseline/item-1/key/tests.rs",
    ]
    for path in key_paths:
        assert pattern_matches(session.KEY_DENY_PATTERN, path), f"deny pattern misses {path}"

    settings = settings_from_command(session.trainer_launch_command("unit-1", "sess-1"))
    for path in key_paths:
        for allow_pattern in settings["permissions"]["allow"]:
            if allow_pattern.startswith(("Read(", "Glob(")):
                assert not pattern_matches(allow_pattern, path), f"{allow_pattern} wrongly admits {path}"


def test_launch_command_scopes_the_hook_to_the_named_unit_only() -> None:
    _, crate_1, _ = session.unit_paths("unit-1", "sess-1")
    _, crate_2, _ = session.unit_paths("unit-2", "sess-1")
    settings_1 = settings_from_command(session.trainer_launch_command("unit-1", "sess-1"))
    settings_2 = settings_from_command(session.trainer_launch_command("unit-2", "sess-1"))

    hook_command_1 = settings_1["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    hook_command_2 = settings_2["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    assert crate_1 in hook_command_1 and crate_2 not in hook_command_1
    assert crate_2 in hook_command_2 and crate_1 not in hook_command_2


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_open_session_prints_a_launch_command_with_the_deny_rule(
    isolated_paths: Path, capsys: pytest.CaptureFixture
) -> None:
    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    session.open_session(items_root=isolated_paths / "items")
    out = capsys.readouterr().out
    assert "--permission-mode dontAsk" in out
    assert "--settings" in out
    command_text = out[out.index("start the trainer:\n") + len("start the trainer:\n") :].strip()
    tokens = shlex.split(command_text)
    settings = json.loads(Path(tokens[tokens.index("--settings") + 1]).read_text(encoding="utf-8"))
    assert session.KEY_DENY_PATTERN in settings["permissions"]["deny"]

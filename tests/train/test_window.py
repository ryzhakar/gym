"""Tests for gym.train.window and `gym train window`: one tmux window per exercise crate, nvim
laid out by a generated script, tmux reached only through an injected runner (owner rulings
2026-10-26)."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest
from typer.testing import CliRunner

from gym.cli import app
from gym.train import window

FIXTURES = Path(__file__).parent / "fixtures" / "window"
P1 = FIXTURES / "u02-enums-match" / "probe-b" / "p1-lift-log"
P2 = FIXTURES / "u02-enums-match" / "probe-b" / "p2-pallet-handling"
ATTEMPT = FIXTURES / "u01-own-move-borrow" / "attempt"


class FakeRunner:
    """Records every argv; answers tmux queries from preset state."""

    def __init__(self, windows: tuple[str, ...] = (), session_exists: bool = True, current: str = "live"):
        self.calls: list[list[str]] = []
        self.windows = windows
        self.session_exists = session_exists
        self.current = current

    def __call__(self, argv: list[str]) -> subprocess.CompletedProcess:
        self.calls.append(argv)
        sub = argv[1]
        if sub == "has-session":
            return subprocess.CompletedProcess(argv, 0 if self.session_exists else 1, "", "")
        if sub == "list-windows":
            return subprocess.CompletedProcess(argv, 0, "".join(w + "\n" for w in self.windows), "")
        if sub == "display-message":
            return subprocess.CompletedProcess(argv, 0, self.current + "\n", "")
        return subprocess.CompletedProcess(argv, 0, "", "")


# spec location


def test_spec_inside_crate() -> None:
    assert window.find_spec(P1) == P1 / "spec.md"


def test_spec_beside_crate() -> None:
    assert window.find_spec(ATTEMPT) == ATTEMPT.parent / "attempt.md"


def test_missing_spec_refused(tmp_path: Path) -> None:
    crate = tmp_path / "u03-x" / "attempt"
    crate.mkdir(parents=True)
    with pytest.raises(window.WindowError, match="no spec"):
        window.find_spec(crate)


# Edit line


def test_edit_line_one_file() -> None:
    assert window.parse_edit_line("# T\n\nEdit: src/lib.rs\n") == ["src/lib.rs"]


def test_edit_line_three_files() -> None:
    text = "# T\n\nEdit: src/lib.rs, src/caller_side.rs,src/callee_side.rs \n"
    assert window.parse_edit_line(text) == ["src/lib.rs", "src/caller_side.rs", "src/callee_side.rs"]


def test_edit_line_missing_refused() -> None:
    with pytest.raises(window.WindowError, match="Edit:"):
        window.parse_edit_line("# T\n\nno edit line here\n")


# kind


def test_kind_predict_when_every_edit_is_prediction() -> None:
    assert window.detect_kind(["prediction.txt"]) == "predict"


def test_kind_code_otherwise() -> None:
    assert window.detect_kind(["src/lib.rs"]) == "code"
    assert window.detect_kind(["prediction.txt", "src/lib.rs"]) == "code"


# naming


def test_window_name_probe_crate_takes_unit_prefix() -> None:
    assert window.window_name(P1) == "u02-p1"


def test_window_name_attempt_crate() -> None:
    assert window.window_name(ATTEMPT) == "u01-attempt"


def test_window_name_explicit_prefix() -> None:
    assert window.window_name(P2, prefix="rb") == "rb-p2"


# scripts


def test_code_script_files_sizes_focus() -> None:
    plan = window.plan_window(ATTEMPT)
    assert plan.kind == "code"
    script = plan.script
    assert "'../attempt.md'" in script
    for name in ("src/lib.rs", "src/caller_side.rs", "src/callee_side.rs"):
        assert f"'{name}'" in script
    assert script.index("src/lib.rs") < script.index("src/caller_side.rs") < script.index("src/callee_side.rs")
    assert "terminal bacon test" in script
    assert "vertical resize 70" in script
    assert "resize 14" in script
    # spec is window 1, edit files 2..4; first edit file larger than the others, focus ends there
    assert "let s:first = s:rest * 3 / 5" in script
    assert script.rstrip().endswith("2wincmd w")


def test_code_script_single_file_has_no_share_split() -> None:
    script = window.plan_window(P2).script
    assert "'src/lib.rs'" in script
    assert "s:first" not in script
    assert script.rstrip().endswith("2wincmd w")


def test_predict_script_files_sizes_focus() -> None:
    plan = window.plan_window(P1)
    assert plan.kind == "predict"
    script = plan.script
    assert "'spec.md'" in script and "'prediction.txt'" in script and "'src/main.rs'" in script
    assert "bacon" not in script
    assert "vertical resize 80" in script
    assert script.index("prediction.txt") < script.index("botright vsplit") < script.index("src/main.rs")
    assert script.rstrip().endswith("2wincmd w")


def test_predict_right_column_stacks_every_rs(tmp_path: Path) -> None:
    crate = tmp_path / "u09-x" / "p1-many"
    shutil.copytree(P1, crate)
    (crate / "src" / "extra.rs").write_text("")
    script = window.plan_window(crate).script
    assert "'src/extra.rs'" in script and "'src/main.rs'" in script


# tmux argv


def _nvim_argv(argv: list[str]) -> list[str]:
    return argv[argv.index("nvim") :]


def test_kill_then_create(tmp_path: Path) -> None:
    runner = FakeRunner(windows=("u02-p1", "other"))
    plans = window.open_windows([P1], session="gym", prefix=None, runner=runner, script_dir=tmp_path)
    subs = [c[1] for c in runner.calls]
    assert subs.index("kill-window") < subs.index("new-window")
    kill = next(c for c in runner.calls if c[1] == "kill-window")
    assert kill[-1] == "=gym:=u02-p1"
    new = next(c for c in runner.calls if c[1] == "new-window")
    assert new[new.index("-n") + 1] == "u02-p1"
    assert new[new.index("-c") + 1] == str(P1.resolve())
    nvim = _nvim_argv(new)
    assert nvim[:3] == ["nvim", "-n", "-S"]
    assert Path(nvim[3]).read_text() == plans[0].script


def test_no_kill_when_absent(tmp_path: Path) -> None:
    runner = FakeRunner(windows=("other",))
    window.open_windows([P2], session="gym", prefix=None, runner=runner, script_dir=tmp_path)
    assert "kill-window" not in [c[1] for c in runner.calls]


def test_new_session_when_absent(tmp_path: Path) -> None:
    runner = FakeRunner(session_exists=False)
    window.open_windows([P2], session="gym", prefix=None, runner=runner, script_dir=tmp_path)
    subs = [c[1] for c in runner.calls]
    assert "new-session" in subs and "new-window" not in subs


def test_refusal_creates_nothing(tmp_path: Path) -> None:
    bad = tmp_path / "u03-x" / "p1-bare"
    bad.mkdir(parents=True)
    (bad / "spec.md").write_text("# no edit line\n")
    runner = FakeRunner()
    with pytest.raises(window.WindowError):
        window.open_windows([P1, bad], session="gym", prefix=None, runner=runner, script_dir=tmp_path)
    assert runner.calls == []


# CLI


def test_cli_prints_one_line_per_window(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    runner = FakeRunner(current="live")
    monkeypatch.setattr(window, "subprocess_runner", runner)
    monkeypatch.setenv("TMUX", "/tmp/tmux-1/default,1,0")
    result = CliRunner().invoke(app, ["train", "window", str(P1), str(P2), str(ATTEMPT)])
    assert result.exit_code == 0, result.output
    assert result.output.splitlines() == ["u02-p1 predict", "u02-p2 code", "u01-attempt code"]
    new = [c for c in runner.calls if c[1] == "new-window"]
    assert [c[c.index("-t") + 1] for c in new] == ["=live:"] * 3


def test_cli_session_default_gym_outside_tmux(monkeypatch: pytest.MonkeyPatch) -> None:
    runner = FakeRunner()
    monkeypatch.setattr(window, "subprocess_runner", runner)
    monkeypatch.delenv("TMUX", raising=False)
    result = CliRunner().invoke(app, ["train", "window", str(P2)])
    assert result.exit_code == 0, result.output
    assert "display-message" not in [c[1] for c in runner.calls]
    assert any(c[1] == "new-window" and "=gym:" in c for c in runner.calls)


def test_cli_refuses_missing_spec(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    runner = FakeRunner()
    monkeypatch.setattr(window, "subprocess_runner", runner)
    crate = tmp_path / "u03-x" / "p1-nospec"
    crate.mkdir(parents=True)
    result = CliRunner().invoke(app, ["train", "window", str(crate)])
    assert result.exit_code == 1
    assert "no spec" in result.output
    assert runner.calls == []


def test_cli_refuses_missing_edit_line(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    runner = FakeRunner()
    monkeypatch.setattr(window, "subprocess_runner", runner)
    crate = tmp_path / "u03-x" / "p1-noedit"
    crate.mkdir(parents=True)
    (crate / "spec.md").write_text("# spec\n")
    result = CliRunner().invoke(app, ["train", "window", str(crate)])
    assert result.exit_code == 1
    assert "Edit:" in result.output
    assert runner.calls == []


def test_cli_dry_run_prints_argv_and_script_running_only_queries(monkeypatch: pytest.MonkeyPatch) -> None:
    runner = FakeRunner(windows=("u02-p1",))
    monkeypatch.setattr(window, "subprocess_runner", runner)
    monkeypatch.delenv("TMUX", raising=False)
    result = CliRunner().invoke(app, ["train", "window", "--dry-run", str(P1)])
    assert result.exit_code == 0, result.output
    assert {c[1] for c in runner.calls} <= window.QUERIES
    assert "$ tmux kill-window -t =gym:=u02-p1" in result.output
    assert "tmux new-window" in result.output
    assert "'prediction.txt'" in result.output
    assert "u02-p1 predict" in result.output

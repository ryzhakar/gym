"""`gym train window`: one tmux window per exercise crate, a ready work screen of nvim panes
(spec, edit files, and bacon or the source to read), laid out by a generated Vim script.
Reads the crate and its spec only, never `key/` (owner rulings 2026-10-26)."""
from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

Runner = Callable[[list[str]], subprocess.CompletedProcess]

# One entry per exercise kind, first match wins; a kind with `match` None is the fallback.
#   match       a kind matches when every edit file's name is in this set
#   left_width  columns of the left column (spec over edit files), None: what the right leaves
#   spec_rows   rows of the spec pane, None: an equal share
#   first_share (num, den) of the edit rows the first edit file takes when there are several
#   right       {"tmux": cmd, "width": cols}, a tmux pane beside nvim (owner 2026-10-26: no
#               interactive tool inside an nvim terminal), or {"glob": pattern under the crate}
LAYOUTS: dict[str, dict] = {
    "predict": {
        "match": {"prediction.txt"},
        "left_width": 80,
        "spec_rows": None,
        "first_share": None,
        "right": {"glob": "src/**/*.rs"},
    },
    "code": {
        "match": None,
        "left_width": None,
        "spec_rows": 14,
        "first_share": (3, 5),
        "right": {"tmux": "bacon test", "width": 70},
    },
}

QUERIES = frozenset({"has-session", "list-windows", "display-message"})
UNIT_DIR = re.compile(r"u\d+(-.*)?")


class WindowError(ValueError):
    """A crate cannot be laid out: no spec, or no Edit line."""


@dataclass(frozen=True)
class Plan:
    crate: Path
    name: str
    kind: str
    script: str
    pane: Optional[dict] = None


def subprocess_runner(argv: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(argv, capture_output=True, text=True)


def find_spec(crate: Path) -> Path:
    inside = crate / "spec.md"
    if inside.is_file():
        return inside
    beside = crate.parent / f"{crate.name}.md"
    if beside.is_file():
        return beside
    raise WindowError(f"{crate}: no spec: neither {inside} nor {beside} exists")


def parse_edit_line(spec_text: str) -> list[str]:
    for line in spec_text.splitlines():
        if line.startswith("Edit:"):
            files = [part.strip() for part in line[len("Edit:"):].split(",")]
            files = [f for f in files if f]
            if files:
                return files
    raise WindowError("spec has no 'Edit:' line naming the files to edit")


def detect_kind(edit_files: list[str]) -> str:
    for kind, layout in LAYOUTS.items():
        match = layout["match"]
        if match is None or all(Path(f).name in match for f in edit_files):
            return kind
    raise AssertionError("LAYOUTS needs a fallback entry with match None")


def window_name(crate: Path, prefix: Optional[str] = None) -> str:
    if prefix is None:
        crate = crate.resolve()
        unit = next((p for p in crate.parents if UNIT_DIR.fullmatch(p.name)), crate.parent)
        prefix = unit.name.split("-", 1)[0]
    head, _, tail = crate.name.partition("-")
    short = crate.name if tail.isdigit() else head
    return f"{prefix}-{short}"


def _vim_str(text: str) -> str:
    return "'" + text.replace("'", "''") + "'"


def _open(command: str, path: str) -> str:
    return f"silent execute '{command} ' . fnameescape({_vim_str(path)})"


def layout_script(kind: str, spec: str, edit_files: list[str], right_files: list[str]) -> str:
    """Vim script laying out one crate's screen; paths relative to the crate, nvim's cwd.
    Window numbers: spec 1, edit files 2..n+1, right column after them."""
    layout = LAYOUTS[kind]
    right = layout["right"]
    n = len(edit_files)
    left = list(range(1, n + 2))
    lines = [f'" gym train window: {kind} layout, generated', _open("edit", spec)]
    lines += [_open("belowright split", f) for f in edit_files]
    if "tmux" in right:
        right_count = 0
    else:
        right_count = len(right_files)
        for i, f in enumerate(right_files):
            lines.append(_open("botright vsplit" if i == 0 else "belowright split", f))
    right_wins = list(range(n + 2, n + 2 + right_count))
    if right.get("width") and right_wins and "tmux" not in right:
        lines.append(f"{right_wins[0]}wincmd w")
        lines.append(f"vertical resize {right['width']}")
        lines += [f"{w}wincmd w | setlocal winfixwidth" for w in right_wins]
    if layout["left_width"]:
        lines.append("1wincmd w")
        lines.append(f"vertical resize {layout['left_width']}")
        lines += [f"{w}wincmd w | setlocal winfixwidth" for w in left]
    if layout["spec_rows"]:
        lines.append("1wincmd w")
        lines.append(f"resize {layout['spec_rows']}")
        lines.append("setlocal winfixheight")
    if layout["first_share"] and n > 1:
        num, den = layout["first_share"]
        spec_rows = layout["spec_rows"] or 0
        lines.append(f"let s:rest = &lines - &cmdheight - {spec_rows} - {n + 1}")
        lines.append(f"let s:first = s:rest * {num} / {den}")
        lines.append("2wincmd w")
        lines.append("execute 'resize ' . s:first")
        lines.append("setlocal winfixheight")
    lines.append("wincmd =")
    lines.append("2wincmd w")
    return "\n".join(lines) + "\n"


def plan_window(crate: Path, prefix: Optional[str] = None) -> Plan:
    crate = crate.resolve()
    if not crate.is_dir():
        raise WindowError(f"{crate}: not a directory")
    spec = find_spec(crate)
    try:
        edit_files = parse_edit_line(spec.read_text())
    except WindowError as error:
        raise WindowError(f"{spec}: {error}") from None
    kind = detect_kind(edit_files)
    right = LAYOUTS[kind]["right"]
    right_files = (
        sorted(p.relative_to(crate).as_posix() for p in crate.glob(right["glob"]) if p.is_file())
        if "glob" in right
        else []
    )
    script = layout_script(kind, os.path.relpath(spec, crate), edit_files, right_files)
    pane = right if "tmux" in right else None
    return Plan(crate=crate, name=window_name(crate, prefix), kind=kind, script=script, pane=pane)


def current_session(runner: Runner) -> str:
    """The session of `$TMUX`, else `gym`."""
    if not os.environ.get("TMUX"):
        return "gym"
    result = runner(["tmux", "display-message", "-p", "#S"])
    return result.stdout.strip() or "gym"


def open_windows(
    crates: list[Path], session: Optional[str], prefix: Optional[str], runner: Runner, script_dir: Path
) -> list[Plan]:
    """Plan every crate first (refusing before any tmux call), then per crate: kill a window of
    the same name, write the script, create the window running `nvim -n -S <script>`. Session
    None: the session of `$TMUX`, else `gym`."""
    plans = [plan_window(crate, prefix) for crate in crates]
    session = session or current_session(runner)
    session_exists = runner(["tmux", "has-session", "-t", f"={session}"]).returncode == 0
    for plan in plans:
        script_path = script_dir / f"{plan.name}.vim"
        script_path.write_text(plan.script)
        nvim = ["nvim", "-n", "-S", str(script_path)]
        if session_exists:
            listed = runner(["tmux", "list-windows", "-t", f"={session}", "-F", "#{window_name}"])
            if plan.name in listed.stdout.splitlines():
                runner(["tmux", "kill-window", "-t", f"={session}:={plan.name}"])
            runner(["tmux", "new-window", "-d", "-t", f"={session}:", "-n", plan.name, "-c", str(plan.crate), *nvim])
        else:
            runner(["tmux", "new-session", "-d", "-s", session, "-n", plan.name, "-c", str(plan.crate), *nvim])
            session_exists = True
        if plan.pane:
            target = f"={session}:={plan.name}"
            runner(["tmux", "split-window", "-d", "-h", "-l", str(plan.pane["width"]), "-t", target,
                    "-c", str(plan.crate), plan.pane["tmux"]])
    return plans

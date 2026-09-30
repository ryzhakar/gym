"""Check gym's records against the shapes and rules `.claude/memento.yaml` declares.

Usage: `gym records check`. One line per finding; exit 1 on any FAIL.
Files are the ones the next commit would hold: tracked plus untracked, minus ignored.
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import NamedTuple

import yaml

from gym.paths import ROOT

SCHEMA_PATH = ROOT / ".claude/memento.yaml"
ORCHESTRATION = ROOT / "docs/orchestration_log"
LIVING_KINDS = ["charter", "frame", "directive", "opinion_map", "subject", "fact", "map", "schema"]
POINTER_CHECKED_KINDS = ["charter", "frame", "directive", "opinion_map", "subject", "fact", "deferral"]
PROSE_KINDS = ["charter", "frame", "opinion_map", "subject", "fact"]
PATTERN_ROW_TIERS = ["journal", "bench", "archive"]
JOURNAL_FILE_PATTERNS = [re.compile(r"session.*\.md"), re.compile(r"events.*\.md"), re.compile(r"failures\.md")]

DATE = r"\d{4}-\d{2}-\d{2}"
MINUTE = rf"{DATE}T\d{{2}}:\d{{2}}"
SHA = re.compile(r"\b[0-9a-f]{7,40}\b")
PATH_TOKEN = re.compile(r"(?<![\w/.:^-])((?:\.claude|docs|scripts|history|recon)/[\w./{}*<>@:-]*[\w/])")
REVISION_POINTER = re.compile(r"\b([0-9a-f]{7,40}\^*):((?:\.claude|docs|scripts)/[\w./-]*\w)")
HEADING_REF = re.compile(
    r"(?:docs/)?(ground-truth|conventions|opinion-map|capabilities|architecture_log|subjects/[\w-]+)(?:\.md)?`?"
    r"\s*§\s*([^;,()\n`|]+)"
)
RULE_REF = re.compile(r"conventions(?:\.md)?`?\)?\s+rules?\s+((?:`[a-z0-9-]+`(?:,?\s+and\s+|,\s*)?)+)")
GROUND_PATH = re.compile(r"(?<![\w/.-])([\w*.-]+(?:/[\w*.{}-]*)+|[\w-]+\.(?:md|py|yaml|sh|json))(?![\w/])")


class Finding(NamedTuple):
    level: str
    where: str
    message: str


def fail(where: str, message: str) -> Finding:
    return Finding("FAIL", where, message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def committable_files() -> list[str]:
    """Tracked and untracked files git would commit, minus the ignored and the deleted."""
    listing = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard"],
        capture_output=True,
        text=True,
        check=True,
    )
    return sorted({path for path in listing.stdout.splitlines() if (ROOT / path).is_file()})


def home_regex(home: str) -> re.Pattern[str]:
    """The schema's home grammar: `{date}` is one ISO-date segment, `*` stays inside a segment, a trailing `/` covers every depth."""
    parts = re.split(r"(\{date\}|\*)", home)
    body = "".join(DATE if part == "{date}" else "[^/]*" if part == "*" else re.escape(part) for part in parts)
    return re.compile(body + (".+" if home.endswith("/") else "") + r"\Z")


def home_rank(home: str) -> int:
    """Resolution order: an exact filename, then a wildcard filename, then a bare directory; `{date}` settles nothing."""
    if home.endswith("/"):
        return 2
    return 1 if "*" in home else 0


def is_pattern(home: str) -> bool:
    return home.endswith("/") or any(mark in home for mark in "{*")


def kind_of(schema: dict, path: str) -> str | None:
    matches = [(home_rank(spec["home"]), kind) for kind, spec in schema["kinds"].items() if home_regex(spec["home"]).match(path)]
    return min(matches)[1] if matches else None


def kind_files(schema: dict, kind: str, files: list[str]) -> list[Path]:
    """Every file at a kind's home, whether the home is one path or a pattern."""
    home = schema["kinds"][kind]["home"]
    if not is_pattern(home):
        return [ROOT / home] if (ROOT / home).is_file() else []
    return [ROOT / path for path in files if kind_of(schema, path) == kind]


def in_record_space(path: str) -> bool:
    if path.startswith("docs/"):
        return True
    if "/" not in path and path.endswith(".md"):
        return True
    return path.startswith(".claude/") and path.count("/") == 1 and path.endswith((".md", ".yaml"))


def check_map(schema: dict, files: list[str]) -> Iterator[Finding]:
    kinds = schema["kinds"]
    map_path = ROOT / kinds["map"]["home"]
    lines = read(map_path).splitlines()
    if not any(re.fullmatch(rf"Audited {DATE}\.", line.strip()) for line in lines):
        yield fail(rel(map_path), "no dated audit line ('Audited YYYY-MM-DD.')")
    rows: dict[str, str] = {}
    for number, line in enumerate(lines, 1):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[0] in ("path", "---") or not line.startswith("|"):
            continue
        path, kind, load, _purpose = cells
        where = f"{rel(map_path)}:{number}"
        if path in rows:
            yield fail(where, f"'{path}' has a second row")
        rows[path] = kind
        if kind not in kinds:
            yield fail(where, f"kind '{kind}' is not declared in the schema")
            continue
        home = kinds[kind]["home"]
        if kinds[kind]["tier"] in PATTERN_ROW_TIERS:
            if path != home:
                yield fail(where, f"a {kind} row names its home '{home}', not '{path}'")
        elif kind_of(schema, path) != kind:
            yield fail(where, f"'{path}' does not sit at the {kind} home '{home}'")
        elif not (ROOT / path).is_file():
            yield fail(where, f"'{path}' does not exist")
        if load.split()[0] != kinds[kind]["load"]:
            yield fail(where, f"load '{load}' disagrees with the schema's '{kinds[kind]['load']}' for {kind}")
    for kind, spec in kinds.items():
        if spec["load"] not in schema["load_levels"]:
            yield fail(rel(SCHEMA_PATH), f"{kind} declares load '{spec['load']}', not one of the schema's load_levels")
    products = [entry["path"] for entry in schema.get("products", [])]
    retired = [entry["path"] for entry in schema.get("retired", [])]
    for path in files:
        if not in_record_space(path):
            continue
        kind = kind_of(schema, path)
        if kind is None:
            covered = any(path == product or (product.endswith("/") and path.startswith(product)) for product in products)
            if not covered and path not in retired:
                yield fail(path, "outside every home, and not a declared product or retired path")
        elif kinds[kind]["tier"] in PATTERN_ROW_TIERS:
            if rows.get(kinds[kind]["home"]) != kind:
                yield fail(path, f"no map row for the {kind} home '{kinds[kind]['home']}'")
        elif rows.get(path) != kind:
            yield fail(path, f"a {kind} record with no map row")


def check_retired(schema: dict) -> Iterator[Finding]:
    for entry in schema.get("retired", []):
        where = f"{rel(SCHEMA_PATH)} retired {entry['path']}"
        if not (ROOT / entry["path"]).is_file():
            yield fail(where, "the archived file does not exist")
        if "was" in entry and (ROOT / entry["was"]).exists():
            yield fail(where, f"'{entry['was']}' still exists beside its archived copy")
        for token in re.findall(r"[\w./-]+\.(?:md|yaml)", entry.get("superseded_by", "")):
            if not (ROOT / token).is_file():
                yield fail(where, f"superseded_by names '{token}', which does not exist")


def check_charter(schema: dict) -> Iterator[Finding]:
    spec = schema["kinds"]["charter"]
    path = ROOT / spec["home"]
    goal_shape = re.compile(r"^### Goal \d+ · .+ · (?P<horizon>finite|standing) · \S+$")
    sections: list[str] = []
    goals: list[tuple[str, str, set[str]]] = []
    for number, line in enumerate(read(path).splitlines(), 1):
        where = f"{rel(path)}:{number}"
        if line.startswith("@") and not (ROOT / line[1:].strip()).is_file():
            yield fail(where, f"autoload '{line[1:].strip()}' does not exist")
        elif line.startswith("## "):
            sections.append(line[3:])
        elif line.startswith("### ") and sections and sections[-1].startswith("Goals"):
            shape = goal_shape.match(line)
            if not shape:
                yield fail(where, "goal heading is not '### Goal <n> · <name> · <finite|standing> · <status>'")
                continue
            goals.append((where, shape["horizon"], set()))
        elif line.startswith("- ") and sections and sections[-1].startswith("Goals") and goals:
            field = re.match(r"- (\w+):", line)
            if field:
                goals[-1][2].add(field.group(1))
        elif line.startswith("- ") and sections and sections[-1].startswith("Prime directives"):
            ground = line.rpartition("Ground:")[2]
            if "Ground:" not in line or not (re.search(DATE, ground) or SHA.search(ground)):
                yield fail(where, "prime directive does not end in 'Ground:' with a dated owner statement or a commit")
    names = spec["sections"]
    if len(sections) != len(names) or not all(title.startswith(name) for title, name in zip(sections, names)):
        yield fail(rel(path), f"sections {sections} do not follow the schema's {names}")
    for where, horizon, fields in goals:
        wanted = [field for field in spec["goal_fields"] if field != "evidence" or horizon == "finite"]
        missing = [field for field in wanted if field not in fields]
        if missing:
            yield fail(where, f"goal lacks {', '.join(missing)}")
        if horizon == "standing" and "evidence" in fields:
            yield fail(where, "a standing goal carries no completion evidence")


def split_entries(text: str) -> Iterator[tuple[int, str, list[str]]]:
    header_line, header, body = 0, None, []
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            if header is not None:
                yield header_line, header, body
            header_line, header, body = number, line, []
        elif header is not None:
            body.append(line)
    if header is not None:
        yield header_line, header, body


def check_change_log(schema: dict) -> Iterator[Finding]:
    spec = schema["kinds"]["change"]
    path = ROOT / spec["home"]
    if not path.is_file():
        return
    width, fields = spec["label_width"], spec["fields"]
    header_shape = re.compile(rf"^## (?P<start>{DATE})(?: → {DATE})? — \S")
    label_shape = re.compile(r"^(?P<label>[A-Z][A-Z →-]*[A-Z]):(?P<pad> *)")
    previous_start = ""
    for line_number, header, body in split_entries(read(path)):
        where = f"{rel(path)}:{line_number}"
        shape = header_shape.match(header)
        if not shape:
            yield fail(where, "header is not '## YYYY-MM-DD — Title' or '## YYYY-MM-DD → YYYY-MM-DD — Title'")
            continue
        if shape["start"] < previous_start:
            yield fail(where, f"dated {shape['start']} after an entry dated {previous_start}; entries run oldest first")
        previous_start = max(previous_start, shape["start"])
        seen: list[str] = []
        blocks: dict[str, list[str]] = {}
        for offset, line in enumerate(body, 1):
            label = label_shape.match(line)
            if label and label["label"] in fields:
                name = label["label"]
                if len(name) + 1 + len(label["pad"]) != width:
                    yield fail(f"{rel(path)}:{line_number + offset}", f"{name} label is not padded to column {width}")
                if name in blocks:
                    yield fail(where, f"{name} appears twice")
                seen.append(name)
                blocks[name] = [line[width:]]
            elif label and label["pad"]:
                yield fail(f"{rel(path)}:{line_number + offset}", f"unknown field {label['label']}")
            elif line.strip() and not seen:
                yield fail(f"{rel(path)}:{line_number + offset}", "text before the first field")
            elif line.strip():
                if not line.startswith(" " * width):
                    yield fail(f"{rel(path)}:{line_number + offset}", f"continuation not indented to column {width}")
                blocks[seen[-1]].append(line.strip())
        missing = [name for name in spec["required_fields"] if name not in blocks]
        if missing:
            yield fail(where, f"missing required field(s): {', '.join(missing)}")
        if seen != sorted(seen, key=fields.index):
            yield fail(where, f"fields out of order: {' / '.join(seen)}")
        kind_value = " ".join(blocks.get("KIND", [""])).strip()
        if "KIND" in blocks and kind_value not in spec["kind_values"]:
            yield fail(where, f"KIND '{kind_value}' is not one of {spec['kind_values']}")
        for name in spec["one_line_fields"]:
            if len(blocks.get(name, [])) > 1:
                yield fail(where, f"{name} spans {len(blocks[name])} lines; it takes one")
        words = len(header.split()) + sum(len(" ".join(lines).split()) for name, lines in blocks.items() if name != "INVALIDATES")
        if words > spec["word_cap"]:
            yield fail(where, f"{words} words outside INVALIDATES, over the cap of {spec['word_cap']}")


def journal_files(name: re.Pattern[str]) -> list[Path]:
    return sorted(path for path in ORCHESTRATION.glob("history/*/*") if name.fullmatch(path.name))


def trace_line_shape(schema: dict) -> re.Pattern[str]:
    kinds = "|".join(re.escape(kind) for kind in schema["events"])
    return re.compile(rf"^(?P<minute>{MINUTE}) \| (owner|self|agent:[\w.-]+|tool:[\w.-]+) \| ({kinds}) \| \S")


def check_traces(schema: dict) -> Iterator[Finding]:
    line_shape = trace_line_shape(schema)
    for path in journal_files(JOURNAL_FILE_PATTERNS[1]):
        lines = read(path).splitlines()
        if lines and not lines[0].startswith(path.parent.name):
            yield fail(f"{rel(path)}:1", f"first line is not dated {path.parent.name}, the date naming the file")
        previous = ""
        for number, line in enumerate(lines, 1):
            shape = line_shape.match(line)
            if not shape:
                yield fail(f"{rel(path)}:{number}", "not 'YYYY-MM-DDTHH:MM | actor | kind | what'")
                continue
            if shape["minute"] < previous:
                yield fail(f"{rel(path)}:{number}", f"time {shape['minute']} goes back from {previous}")
            previous = max(previous, shape["minute"])


def check_close_blocks(schema: dict) -> Iterator[Finding]:
    for path in journal_files(JOURNAL_FILE_PATTERNS[0]):
        yield from close_block_findings(schema, path)


def close_block_findings(schema: dict, path: Path) -> Iterator[Finding]:
    spec = schema["kinds"]["digest"]
    labels, width = spec["close_labels"], spec["close_label_width"]
    for line_number, header, body in split_entries(read(path)):
        if not header.startswith("## Close"):
            continue
        where = f"{rel(path)}:{line_number}"
        if not re.fullmatch(rf"## Close — {MINUTE}", header):
            yield fail(where, "close header is not '## Close — YYYY-MM-DDTHH:MM'")
        found: list[tuple[str, int]] = []
        for line in (line for line in body if line.strip()):
            label = line[:width].strip()
            if label in labels and line[:width] == label.ljust(width):
                found.append((label, 1))
            elif line.startswith(" " * width) and found:
                found[-1] = (found[-1][0], found[-1][1] + 1)
            else:
                yield fail(where, f"line outside the close fields: {line[:60]!r}")
        if [label for label, _ in found] != labels:
            yield fail(where, f"close fields {[label for label, _ in found]} are not {labels}")
        for label, count in found:
            if label == "state" and count > spec["state_max_lines"]:
                yield fail(where, f"state runs {count} lines, over {spec['state_max_lines']}")
        head_line = next((line for line in body if line.startswith("HEAD")), "")
        if not SHA.match(head_line[width:]):
            yield fail(where, "HEAD does not start with a commit SHA")


def check_failures(schema: dict) -> Iterator[Finding]:
    labels = schema["kinds"]["failure"]["entry_labels"]
    for path in journal_files(JOURNAL_FILE_PATTERNS[2]):
        entries = list(split_entries(read(path)))
        for line_number, _header, body in entries:
            openings = [label for line in body for label in labels if line.startswith(f"{label}:")]
            if openings != labels:
                yield fail(f"{rel(path)}:{line_number}", f"paragraphs open {openings}, not {labels}")
        trace = path.parent / "events.md"
        pointers = sum(" | failure | " in line for line in read(trace).splitlines()) if trace.exists() else 0
        if pointers < len(entries):
            yield fail(rel(path), f"{len(entries)} entries but {pointers} failure lines in {rel(trace)}")


def check_spans_closed_in_digest(schema: dict) -> Iterator[Finding]:
    for trace in journal_files(JOURNAL_FILE_PATTERNS[1]):
        closes = sum(re.search(r" \| span-event \| close", line) is not None for line in read(trace).splitlines())
        digest = trace.parent / trace.name.replace("events", "session")
        blocks = sum(line.startswith("## Close") for line in read(digest).splitlines()) if digest.exists() else 0
        if closes > blocks:
            yield fail(rel(trace), f"{closes} span closes but {blocks} close blocks in {rel(digest)}")


def check_directives(schema: dict, files: list[str]) -> Iterator[Finding]:
    spec = schema["kinds"]["directive"]
    path = ROOT / spec["home"]
    if not path.is_file():
        return
    labels, width = spec["labels"], spec["label_width"]
    headings: list[str] = []
    ids: set[str] = set()
    blocks: list[tuple[int, str, list[tuple[int, str]]]] = []
    block = None
    for number, line in enumerate(read(path).splitlines(), 1):
        if line.startswith("## "):
            headings.append(line[3:].strip().lower())
            block = None
        elif line.startswith("### "):
            block = (number, line[4:].strip(), [])
            blocks.append(block)
        elif line.strip() and block is not None:
            block[2].append((number, line))
    if headings != spec["headings"]:
        yield fail(rel(path), f"headings {headings} are not the schema's {spec['headings']}")
    for number, rule_id, rule_lines in blocks:
        where = f"{rel(path)}:{number}"
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", rule_id):
            yield fail(where, f"rule id '{rule_id}' is not lowercase words joined by hyphens")
        if rule_id in ids:
            yield fail(where, f"rule id '{rule_id}' appears twice")
        ids.add(rule_id)
        order = []
        for line_number, line in rule_lines:
            label = line[:width].strip()
            if label not in labels or line[:width] != label.ljust(width):
                yield fail(f"{rel(path)}:{line_number}", f"not a '{'/'.join(labels)}' line padded to {width}")
                continue
            order.append(label)
            if label == "ground":
                yield from check_ground(f"{rel(path)}:{line_number}", line[width:], files)
        missing = [label for label in spec["required_labels"] if label not in order]
        if missing:
            yield fail(where, f"{rule_id}: missing {', '.join(missing)}")
        if order != sorted(order, key=labels.index) or len(order) != len(set(order)):
            yield fail(where, f"{rule_id}: labels {order} not in the schema's order, or repeated")


def resolve_pointer(token: str) -> Path | None:
    """The file a path token in a record names, or None when it names a pattern or a template."""
    token = re.sub(r"(@[\w.-]+|:\d+(-\d+)?|#.*)$", "", token).rstrip(".:")
    if any(mark in token for mark in "{*<"):
        return None
    if token.startswith(("history/", "recon/")):
        return ORCHESTRATION / token
    return ROOT / token


def path_is_committable(token: str, files: list[str]) -> bool:
    if "*" in token:
        return any(home_regex(token).match(path) for path in files)
    target = resolve_pointer(token)
    if target is None or not target.exists():
        return False
    return target.is_dir() or rel(target) in files


def object_exists(revision: str) -> bool:
    probe = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", revision], capture_output=True, check=False)
    return probe.returncode == 0


def check_ground(where: str, ground: str, files: list[str]) -> Iterator[Finding]:
    paths = GROUND_PATH.findall(ground)
    for token in paths:
        if not path_is_committable(token, files):
            yield fail(where, f"ground names '{token}', which is not a committable path")
    headings = HEADING_REF.findall(ground)
    has_ruling = bool(re.search(DATE, ground)) and "owner" in ground
    has_commit = any(object_exists(f"{sha}^{{commit}}") for sha in SHA.findall(ground))
    if not (paths or headings or has_ruling or has_commit):
        yield fail(where, f"ground names no committable path, SHA, record heading or dated owner ruling: {ground.strip()!r}")


def record_headings(path: Path) -> list[str]:
    return [line.lstrip("#").strip().lower() for line in read(path).splitlines() if line.startswith("#")]


def names_a_heading(wanted: str, headings: list[str]) -> bool:
    """A `§` citation runs on into its sentence, so a heading may be a prefix of what was captured."""
    return any(wanted.startswith(heading) or heading.startswith(wanted) for heading in headings if heading)


def heading_targets(schema: dict, files: list[str]) -> dict[str, Path]:
    kinds = schema["kinds"]
    targets = {
        "ground-truth": ROOT / kinds["frame"]["home"],
        "conventions": ROOT / kinds["directive"]["home"],
        "opinion-map": ROOT / kinds["opinion_map"]["home"],
        "capabilities": ROOT / kinds["fact"]["home"],
        "architecture_log": ROOT / kinds["change"]["home"],
    }
    for path in kind_files(schema, "subject", files):
        targets["subjects/" + path.stem] = path
    return targets


def check_pointers(schema: dict, files: list[str]) -> Iterator[Finding]:
    targets = heading_targets(schema, files)
    conventions = targets["conventions"]
    rule_ids = set(re.findall(r"(?m)^### ([a-z0-9-]+)$", read(conventions))) if conventions.is_file() else set()
    living = {path for kind in LIVING_KINDS for path in kind_files(schema, kind, files)}
    checked = [path for kind in POINTER_CHECKED_KINDS for path in kind_files(schema, kind, files)]
    code = [ROOT / path for path in files if path.startswith("scripts/") and path.endswith(".py")]
    for path in checked + code:
        for number, line in enumerate(read(path).splitlines(), 1):
            where = f"{rel(path)}:{number}"
            for match in RULE_REF.finditer(line):
                for rule_id in re.findall(r"`([a-z0-9-]+)`", match.group(1)):
                    if rule_id not in rule_ids:
                        yield fail(where, f"cites conventions rule '{rule_id}', which does not exist")
            if path in code:
                continue
            for record, heading in HEADING_REF.findall(line):
                if record == "conventions":
                    yield fail(where, "cites a conventions heading; conventions are cited by rule id")
                    continue
                target = targets.get(record)
                wanted = heading.strip().rstrip(".").lower()
                if target is None or not target.is_file():
                    yield fail(where, f"'{record} § {heading.strip()}' cites a record that does not exist")
                elif not names_a_heading(wanted, record_headings(target)):
                    yield fail(where, f"'{record} § {heading.strip()}' names no heading in {rel(target)}")
            for revision, revision_path in REVISION_POINTER.findall(line):
                if not object_exists(f"{revision}:{revision_path}"):
                    yield fail(where, f"points at '{revision}:{revision_path}', which git does not hold")
            for token in PATH_TOKEN.findall(line):
                target = resolve_pointer(token)
                if target is None:
                    continue
                if token.startswith("recon/") or "/recon/" in token:
                    if path in living:
                        yield fail(where, f"points into recon/, which is gitignored and carries no provenance: {token}")
                elif not target.exists():
                    yield fail(where, f"points at '{token}', which does not exist")
                elif target.is_file() and rel(target) not in files:
                    yield fail(where, f"points at '{token}', which git would not commit")


def check_no_hard_wrap(schema: dict, files: list[str]) -> Iterator[Finding]:
    """A paragraph or list item is one line; tables, fenced blocks and headings keep their breaks."""
    structural = ("#", "|", "```", "---", ">", "- ", "* ", "@")
    for kind in PROSE_KINDS:
        for path in kind_files(schema, kind, files):
            fenced, previous = False, ""
            for number, line in enumerate(read(path).splitlines(), 1):
                text = line.strip()
                if text.startswith("```"):
                    fenced = not fenced
                elif not fenced and text and previous and not text.startswith(structural) and not re.match(r"\d+\. ", text):
                    if not previous.startswith(("#", "|", "```", "---", ">", "@")):
                        yield fail(f"{rel(path)}:{number}", "prose continues a line above; authored prose carries no hard wrap")
                previous = "" if fenced and not text.startswith("```") else text


def check_budgets(schema: dict) -> Iterator[Finding]:
    per_word = schema["token_estimate"]["tokens_per_word"]
    for kind, spec in schema["kinds"].items():
        path = ROOT / spec["home"]
        if "budget_tokens" not in spec or not path.is_file():
            continue
        estimate = round(len(read(path).split()) * per_word)
        if estimate > spec["budget_tokens"]:
            yield fail(rel(path), f"~{estimate} tokens, over the {kind} budget of {spec['budget_tokens']}")


def check_history_admission(files: list[str]) -> Iterator[Finding]:
    for path in files:
        parts = path.split("/")
        if parts[:3] != ["docs", "orchestration_log", "history"]:
            continue
        if len(parts) != 5 or not re.fullmatch(DATE, parts[3]) or not any(name.fullmatch(parts[4]) for name in JOURNAL_FILE_PATTERNS):
            yield fail(path, "history/ admits only <date>/session*, events* and failures.md; other artifacts go to recon/")


def check_nul_bytes(files: list[str]) -> Iterator[Finding]:
    for path in files:
        if in_record_space(path) and b"\x00" in (ROOT / path).read_bytes():
            yield fail(path, "contains NUL bytes")


def load_schema() -> dict:
    return yaml.safe_load(read(SCHEMA_PATH))


def main() -> int:
    schema = load_schema()
    files = committable_files()
    checks = [
        check_charter(schema),
        check_map(schema, files),
        check_retired(schema),
        check_change_log(schema),
        check_traces(schema),
        check_close_blocks(schema),
        check_failures(schema),
        check_spans_closed_in_digest(schema),
        check_directives(schema, files),
        check_no_hard_wrap(schema, files),
        check_pointers(schema, files),
        check_budgets(schema),
        check_history_admission(files),
        check_nul_bytes(files),
    ]
    findings = [finding for check in checks for finding in check]
    for finding in findings:
        print(f"{finding.level}  {finding.where}  {finding.message}")
    print(f"records: {len(findings)} FAIL")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

"""The four record checks `memento check` lacks: the map's audit line, retired entries, pointers and
hard wraps in the opinion map and the subjects, and untracked record files.

Usage: `gym records check`, after `memento check`. One line per finding; exit 1 on any FAIL.
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
CHECKED_KINDS = ["opinion_map", "subject"]

DATE = r"\d{4}-\d{2}-\d{2}"
PATH_TOKEN = re.compile(r"(?<![\w/.:^-])((?:\.claude|docs|scripts|history|recon)/[\w./{}*<>@:-]*[\w/])")
REVISION_POINTER = re.compile(r"\b([0-9a-f]{7,40}\^*):((?:\.claude|docs|scripts)/[\w./-]*\w)")
HEADING_REF = re.compile(
    r"(?:docs/)?(ground-truth|conventions|opinion-map|capabilities|architecture_log|subjects/[\w-]+)(?:\.md)?`?"
    r"\s*§\s*([^;,()\n`|]+)"
)
RULE_REF = re.compile(r"conventions(?:\.md)?`?\)?\s+rules?\s+((?:`[a-z0-9-]+`(?:,?\s+and\s+|,\s*)?)+)")


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


def check_audited(schema: dict) -> Iterator[Finding]:
    map_path = ROOT / schema["kinds"]["map"]["home"]
    if not any(re.fullmatch(rf"Audited {DATE}\.", line.strip()) for line in read(map_path).splitlines()):
        yield fail(rel(map_path), "no dated audit line ('Audited YYYY-MM-DD.')")


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


def resolve_pointer(token: str) -> Path | None:
    """The file a path token in a record names, or None when it names a pattern or a template."""
    token = re.sub(r"(@[\w.-]+|:\d+(-\d+)?|#.*)$", "", token).rstrip(".:")
    if any(mark in token for mark in "{*<"):
        return None
    if token.startswith(("history/", "recon/")):
        return ORCHESTRATION / token
    return ROOT / token


def object_exists(revision: str) -> bool:
    probe = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", revision], capture_output=True, check=False)
    return probe.returncode == 0


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
    checked = [path for kind in CHECKED_KINDS for path in kind_files(schema, kind, files)]
    for path in checked:
        for number, line in enumerate(read(path).splitlines(), 1):
            where = f"{rel(path)}:{number}"
            for match in RULE_REF.finditer(line):
                for rule_id in re.findall(r"`([a-z0-9-]+)`", match.group(1)):
                    if rule_id not in rule_ids:
                        yield fail(where, f"cites conventions rule '{rule_id}', which does not exist")
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
                    yield fail(where, f"points into recon/, which is gitignored and carries no provenance: {token}")
                elif not target.exists():
                    yield fail(where, f"points at '{token}', which does not exist")
                elif target.is_file() and rel(target) not in files:
                    yield fail(where, f"points at '{token}', which git would not commit")


def check_no_hard_wrap(schema: dict, files: list[str]) -> Iterator[Finding]:
    """A paragraph or list item is one line; tables, fenced blocks and headings keep their breaks."""
    structural = ("#", "|", "```", "---", ">", "- ", "* ", "@")
    for kind in CHECKED_KINDS:
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


def check_untracked() -> Iterator[Finding]:
    """A record file git does not hold yet; memento only warns, gym refuses."""
    listing = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True, check=True
    )
    for path in sorted(listing.stdout.splitlines()):
        if in_record_space(path) and (ROOT / path).is_file():
            yield fail(path, "untracked record file; git add it or commit it")


def load_schema() -> dict:
    return yaml.safe_load(read(SCHEMA_PATH))


def main() -> int:
    schema = load_schema()
    files = committable_files()
    checks = [
        check_audited(schema),
        check_retired(schema),
        check_pointers(schema, files),
        check_no_hard_wrap(schema, files),
        check_untracked(),
    ]
    findings = [finding for check in checks for finding in check]
    for finding in findings:
        print(f"{finding.level}  {finding.where}  {finding.message}")
    print(f"records: {len(findings)} FAIL")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

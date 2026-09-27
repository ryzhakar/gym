"""Check a Rust map instance against `maps/rust/schema.yaml` (fable-plan.md § 5, rules 1-8).

Usage: `uv run python scripts/map/check_map.py --map maps/rust`.
One line per finding; exit 1 on any FAIL. Slice 1 needs rules 1-3 and 6-8; rules
4-5 gate only `status: closed` Questions, so an open Question never fails them.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterator
from datetime import date
from pathlib import Path
from typing import Any, NamedTuple

import yaml

ENTITY_KINDS = ["question", "position", "argument", "value", "voice", "claim", "source", "convention", "domain", "concept"]


class Finding(NamedTuple):
    level: str
    where: str
    message: str


def fail(where: str, message: str) -> Finding:
    return Finding("FAIL", where, message)


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_schema(map_dir: Path) -> dict:
    return load_yaml(map_dir / "schema.yaml")


def kind_dir(map_dir: Path, kind: str, schema: dict) -> Path:
    return map_dir / schema["kinds"][kind]["home"]


def entity_files(map_dir: Path, kind: str, schema: dict) -> list[Path]:
    directory = kind_dir(map_dir, kind, schema)
    return sorted(directory.glob("*.yaml")) if directory.is_dir() else []


def rel(map_dir: Path, path: Path) -> str:
    return str(path.relative_to(map_dir.parent))


class Entity(NamedTuple):
    kind: str
    id: str
    path: Path
    data: dict


def load_entities(map_dir: Path, schema: dict) -> tuple[list[Entity], list[Finding]]:
    """Parse every entity file (rule 1's 'every file parses'). A file that fails to
    parse, or is not a mapping, is dropped and reported; every other rule then
    runs on what did load."""
    entities: list[Entity] = []
    findings: list[Finding] = []
    for kind in ENTITY_KINDS:
        for path in entity_files(map_dir, kind, schema):
            where = rel(map_dir, path)
            try:
                data = load_yaml(path)
            except yaml.YAMLError as error:
                findings.append(fail(where, f"does not parse as YAML: {error}"))
                continue
            if not isinstance(data, dict):
                findings.append(fail(where, "does not parse as a mapping"))
                continue
            entities.append(Entity(kind, path.stem, path, data))
    return entities, findings


def load_checks(map_dir: Path, schema: dict) -> dict[str, list[dict]]:
    """`checks/<entity-id>.yaml` files: each holds a list of check records, keyed
    by the entity id its filename names (schema.yaml: `check: {home: checks, list: true}`)."""
    directory = kind_dir(map_dir, "check", schema)
    if not directory.is_dir():
        return {}
    result: dict[str, list[dict]] = {}
    for path in sorted(directory.glob("*.yaml")):
        data = load_yaml(path)
        result[path.stem] = data if isinstance(data, list) else []
    return result


# --- Rule 1: file parses, id equals filename, id unique, fields known, required present, enums legal ---


def check_shape(entities: list[Entity], schema: dict) -> Iterator[Finding]:
    seen_ids: dict[str, str] = {}
    for kind, entity_id, path, data in entities:
        spec = schema["kinds"][kind]
        where = str(path)
        if data.get("id") != entity_id:
            yield fail(where, f"id {data.get('id')!r} does not equal the filename '{entity_id}'")
        if entity_id in seen_ids:
            yield fail(where, f"id '{entity_id}' also used by {seen_ids[entity_id]}")
        seen_ids[entity_id] = where
        known_fields = {"id", *spec["fields"]}
        for field in data:
            if field not in known_fields:
                yield fail(where, f"field '{field}' is not in the schema for kind '{kind}'")
        for field in spec["required"]:
            if not data.get(field):
                yield fail(where, f"missing required field '{field}'")
        for field, field_spec in spec["fields"].items():
            if field not in data or data[field] is None:
                continue
            if field_spec["type"] == "enum":
                yield from check_enum(where, kind, field, data[field], field_spec)


def check_enum(where: str, kind: str, field: str, value: Any, field_spec: dict) -> Iterator[Finding]:
    legal = set(field_spec["values"]) | set(field_spec.get("allow", []))
    values = value if isinstance(value, list) else [value]
    for one in values:
        if one not in legal:
            yield fail(where, f"{kind}.{field} value '{one}' is not one of {sorted(legal)}")


# --- Rule 2: every relation id resolves to an existing file of the right kind ---


def check_relations(entities: list[Entity], schema: dict) -> Iterator[Finding]:
    ids_by_kind = {kind: {e.id for e in entities if e.kind == kind} for kind in ENTITY_KINDS}
    for kind, entity_id, path, data in entities:
        spec = schema["kinds"][kind]
        where = str(path)
        for field, field_spec in spec["fields"].items():
            target_kind = field_spec.get("relation")
            if target_kind is None or field not in data or data[field] is None:
                continue
            allowed = set(field_spec.get("allow", []))
            values = data[field] if isinstance(data[field], list) else [data[field]]
            for target_id in values:
                if target_id in allowed:
                    continue
                if target_id not in ids_by_kind[target_kind]:
                    yield fail(where, f"{field} '{target_id}' does not resolve to a {target_kind}")


# --- Rule 3: Claim shape ---


def parse_date(value: Any) -> date | None:
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        return None


def check_claims(entities: list[Entity], schema: dict) -> Iterator[Finding]:
    claims = {e.id: e for e in entities if e.kind == "claim"}
    for entity_id, entity in claims.items():
        where = str(entity.path)
        data = entity.data
        if parse_date(data.get("date")) is None:
            yield fail(where, f"date '{data.get('date')}' is not ISO (YYYY-MM-DD)")
        quote = data.get("quote")
        if quote is not None and len(str(quote)) > 300:
            yield fail(where, f"quote is {len(str(quote))} characters, over the 300-character cap")
        if not str(data.get("locator", "")).strip():
            yield fail(where, "locator is empty")
        superseded_by = data.get("superseded_by")
        if superseded_by:
            later = claims.get(superseded_by)
            if later is None:
                continue  # already reported as an unresolved relation by check_relations
            this_date, later_date = parse_date(data.get("date")), parse_date(later.data.get("date"))
            if later.data.get("voice") != data.get("voice"):
                yield fail(where, f"superseded_by '{superseded_by}' is a different Voice's Claim")
            elif this_date and later_date and later_date <= this_date:
                yield fail(where, f"superseded_by '{superseded_by}' is not later-dated than this Claim")


# --- Rules 4 and 5: a closed Question's evidence minimum ---


def check_agree_or_resolved(check_records: list[dict], kind: str) -> bool:
    matching = [record for record in check_records if record.get("check") == kind]
    return any(record.get("agree") or record.get("resolution") not in (None, "unresolved") for record in matching)


def check_itt_pass(check_records: list[dict]) -> bool:
    return any(record.get("check") == "itt" and (record.get("grader") or {}).get("verdict") == "pass" for record in check_records)


def check_closed_questions(entities: list[Entity], checks: dict[str, list[dict]]) -> Iterator[Finding]:
    by_kind = {kind: [e for e in entities if e.kind == kind] for kind in ENTITY_KINDS}
    positions_of = {q.id: [] for q in by_kind["question"]}
    for position in by_kind["position"]:
        positions_of.setdefault(position.data.get("question"), []).append(position)
    claims_of = {p.id: [] for p in by_kind["position"]}
    for claim in by_kind["claim"]:
        claims_of.setdefault(claim.data.get("position"), []).append(claim)
    arguments_of = {p.id: [] for p in by_kind["position"]}
    for argument in by_kind["argument"]:
        arguments_of.setdefault(argument.data.get("position"), []).append(argument)

    for question in by_kind["question"]:
        if question.data.get("status") != "closed":
            continue
        where = str(question.path)
        positions = positions_of.get(question.id, [])
        if len(positions) < 2:
            yield fail(where, f"closed with {len(positions)} Position(s), needs >=2")
        if not question.data.get("domains"):
            yield fail(where, "closed with no Domain")
        if not question.data.get("concepts"):
            yield fail(where, "closed with no Concept")
        for position in positions:
            yield from check_closed_position(position, claims_of.get(position.id, []), arguments_of.get(position.id, []), checks)


def check_closed_position(position: Entity, claims: list[Entity], arguments: list[Entity], checks: dict[str, list[dict]]) -> Iterator[Finding]:
    where = str(position.path)
    resolved_claims = [claim for claim in claims if claim.data.get("position") != "unresolved"]
    distinct_voices = {claim.data.get("voice") for claim in resolved_claims}
    if len(resolved_claims) < 2 or len(distinct_voices) < 2:
        yield fail(where, f"{len(resolved_claims)} resolved Claim(s) from {len(distinct_voices)} distinct Voice(s), needs >=2 Claims from >=2 Voices")
    for claim in resolved_claims:
        if not check_agree_or_resolved(checks.get(claim.id, []), "fill-position"):
            yield fail(str(claim.path), "no fill-position check showing agree or a resolution")
    if not any(argument.data.get("values") for argument in arguments):
        yield fail(where, "no Argument with >=1 Value")
    if not check_agree_or_resolved(checks.get(position.id, []), "fill-tag"):
        yield fail(where, "tag has no fill-tag check")
    if not check_itt_pass(checks.get(position.id, [])):
        yield fail(where, "summary has no passing itt check")


# --- Rule 6: Voice ---


def check_voices(entities: list[Entity]) -> Iterator[Finding]:
    for entity in entities:
        if entity.kind != "voice":
            continue
        track_record = entity.data.get("track_record") or []
        if not any(isinstance(line, dict) and line.get("url") for line in track_record):
            yield fail(str(entity.path), "no track_record line with a url")


# --- Rule 7: Convention ---


def check_conventions(entities: list[Entity]) -> Iterator[Finding]:
    for entity in entities:
        if entity.kind != "convention":
            continue
        prevalence = entity.data.get("prevalence") or []
        if not any(isinstance(line, dict) and line.get("url") and line.get("date") for line in prevalence):
            yield fail(str(entity.path), "no prevalence line with a url and a date")


# --- Rule 8: report ---


def report(entities: list[Entity]) -> str:
    lines = ["", "counts per kind:"]
    for kind in ENTITY_KINDS:
        lines.append(f"  {kind}: {sum(1 for e in entities if e.kind == kind)}")
    lines.append("per stratum (domain):")
    questions = [e for e in entities if e.kind == "question"]
    claims = [e for e in entities if e.kind == "claim"]
    voices = [e for e in entities if e.kind == "voice"]
    domains = sorted({d for q in questions for d in (q.data.get("domains") or [])} | {e.id for e in entities if e.kind == "domain"})
    resolved_claims = {claim.id for claim in claims if claim.data.get("position") != "unresolved"}
    for domain in domains:
        in_domain = [q for q in questions if domain in (q.data.get("domains") or [])]
        open_count = sum(1 for q in in_domain if q.data.get("status") == "open")
        closed_count = sum(1 for q in in_domain if q.data.get("status") == "closed")
        lines.append(f"  {domain}: questions open={open_count} closed={closed_count}")
    lines.append(f"claims confirmed (resolved to a Position): {len(resolved_claims)} / {len(claims)}")
    lines.append(f"voices: {len(voices)}")
    return "\n".join(lines)


def run_checks(map_dir: Path) -> list[Finding]:
    schema = load_schema(map_dir)
    entities, parse_findings = load_entities(map_dir, schema)
    checks = load_checks(map_dir, schema)
    findings = list(parse_findings)
    findings += list(check_shape(entities, schema))
    findings += list(check_relations(entities, schema))
    findings += list(check_claims(entities, schema))
    findings += list(check_closed_questions(entities, checks))
    findings += list(check_voices(entities))
    findings += list(check_conventions(entities))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", required=True, type=Path, dest="map_dir")
    args = parser.parse_args()
    findings = run_checks(args.map_dir)
    for finding in findings:
        print(f"{finding.level}  {finding.where}  {finding.message}")
    entities, _ = load_entities(args.map_dir, load_schema(args.map_dir))
    print(report(entities))
    print(f"\nmap: {len(findings)} FAIL")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

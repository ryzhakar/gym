"""gym records event/close with `--span`: a span keeps its own events-<span>.md and session-<span>.md.

Every test writes to a tmp copy of the journal (the `history` fixture), never to the live one.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest
from typer.testing import CliRunner

from gym.records import check_records, close_span
from gym.records import event as event_module
from gym.records.cli import app

runner = CliRunner()
Clock = Callable[[str], None]
DAY = "docs/orchestration_log/history/2099-01-02/"


def snapshot(history: Path) -> dict[str, bytes | None]:
    """Every path under history/ with its bytes; a directory maps to None."""
    return {str(path.relative_to(history)): path.read_bytes() if path.is_file() else None for path in sorted(history.rglob("*"))}


def journal_findings() -> list[check_records.Finding]:
    """The journal checks `gym records check` runs, over the tree the history fixture stands up."""
    schema = check_records.load_schema()
    files = sorted(str(path.relative_to(check_records.ROOT)) for path in check_records.ORCHESTRATION.glob("history/*/*"))
    return [
        *check_records.check_traces(schema),
        *check_records.check_close_blocks(schema),
        *check_records.check_failures(schema),
        *check_records.check_spans_closed_in_digest(schema),
        *check_records.check_history_admission(files),
    ]


def open_span(span: str | None, text: str = "open; begins") -> Path:
    trace, _line = event_module.append_event("self", "span-event", text, span=span)
    return trace


@pytest.mark.parametrize("span", ["a", "alpha", "a1", "2099-01-02", "a-b-c"])
def test_an_opening_creates_the_spans_own_trace_in_todays_directory(history: Path, at: Clock, span: str) -> None:
    at("2099-01-02T09:00")

    trace, line = event_module.append_event("self", "span-event", "open; alpha begins", span=span)

    assert trace == history / "2099-01-02" / f"events-{span}.md"
    assert trace.read_text(encoding="utf-8") == line + "\n"
    assert not (history / "2099-01-02" / "events.md").exists()


def test_a_later_event_finds_the_spans_trace_among_several_dates(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    alpha = open_span("alpha")
    at("2099-01-03T09:00")
    beta = open_span("beta")
    at("2099-01-04T09:00")
    shared = open_span(None, "open; shared begins")
    shared_before = shared.read_bytes()

    at("2099-01-05T09:00")
    to_alpha, alpha_line = event_module.append_event("owner", "decision", "alpha goes on", span="alpha")
    to_beta, beta_line = event_module.append_event("owner", "decision", "beta goes on", span="beta")
    to_shared, shared_line = event_module.append_event("owner", "decision", "shared goes on")

    assert (to_alpha, to_beta, to_shared) == (alpha, beta, shared)
    assert alpha.read_text(encoding="utf-8").splitlines()[-1] == alpha_line
    assert beta.read_text(encoding="utf-8").splitlines()[-1] == beta_line
    assert shared.read_bytes() == shared_before + (shared_line + "\n").encode()
    assert alpha_line not in shared.read_text(encoding="utf-8")
    assert len(alpha.read_text(encoding="utf-8").splitlines()) == 2


def test_the_newest_date_holding_the_spans_trace_wins(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    older = open_span("alpha")
    older_before = older.read_bytes()
    at("2099-01-07T09:00")
    newer = open_span("alpha")

    at("2099-01-08T09:00")
    trace, _line = event_module.append_event("owner", "decision", "alpha goes on", span="alpha")

    assert trace == newer
    assert older.read_bytes() == older_before


def test_without_a_span_the_shared_trace_is_used_as_before(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    shared = open_span(None, "open; shared begins")
    at("2099-01-02T09:30")

    trace, _line = event_module.append_event("owner", "decision", "shared goes on")

    assert shared == history / "2099-01-02" / "events.md"
    assert trace == shared
    assert [path.name for path in shared.parent.iterdir()] == ["events.md"]


def test_without_a_span_and_without_a_trace_the_refusal_reads_as_before(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(event_module, "ORCHESTRATION", tmp_path)

    with pytest.raises(SystemExit) as shared:
        event_module.current_trace(opening=False)
    with pytest.raises(SystemExit) as span:
        event_module.current_trace(opening=False, span="alpha")

    assert shared.value.code == "no trace exists; open a span first: event.py self span-event 'open; ...'"
    assert "events-alpha.md" in str(span.value.code)
    assert "gym records event --span alpha self span-event 'open; ...'" in str(span.value.code)


def test_an_event_for_a_span_that_never_opened_is_refused_and_writes_nothing(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    open_span(None, "open; shared begins")
    before = snapshot(history)

    with pytest.raises(SystemExit) as refusal:
        event_module.append_event("owner", "decision", "to nobody", span="ghost")

    assert "events-ghost.md" in str(refusal.value.code)
    assert snapshot(history) == before


def test_span_events_and_close_leave_the_shared_pair_untouched(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    open_span(None, "open; shared begins")
    at("2099-01-02T09:05")
    assert close_span.run("shared state", "none", "shared next") == 0
    before = snapshot(history)
    assert "2099-01-02/events.md" in before and "2099-01-02/session.md" in before

    at("2099-01-02T10:00")
    open_span("alpha")
    at("2099-01-02T10:05")
    event_module.append_event("owner", "decision", "alpha goes on", span="alpha")
    at("2099-01-02T10:10")
    assert close_span.run("alpha state", "none", "alpha next", span="alpha") == 0

    after = snapshot(history)
    assert {path: data for path, data in after.items() if path in before} == before
    assert set(after) - set(before) == {"2099-01-02/events-alpha.md", "2099-01-02/session-alpha.md"}


def test_close_writes_the_spans_session_with_a_close_block_and_a_close_line_in_its_trace(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    trace = open_span("alpha")
    at("2099-01-03T10:00")

    assert close_span.run("one state line", "none", "first step", span="alpha") == 0

    session = trace.parent / "session-alpha.md"
    width = check_records.load_schema()["kinds"]["digest"]["close_label_width"]
    assert session.read_text(encoding="utf-8") == (
        "# 2099-01-02\n"
        "\n## Close — 2099-01-03T10:00\n\n"
        f"{'HEAD'.ljust(width)}abc1234 (clean)\n"
        f"{'state'.ljust(width)}one state line\n"
        f"{'open'.ljust(width)}none\n"
        f"{'next'.ljust(width)}first step\n"
    )
    assert trace.read_text(encoding="utf-8").splitlines()[-1] == "2099-01-03T10:00 | self | span-event | close; HEAD abc1234 (clean); next: first step"
    assert not (trace.parent / "session.md").exists()


def test_a_second_close_appends_to_the_same_session_without_a_second_heading(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    trace = open_span("alpha")
    at("2099-01-02T10:00")
    close_span.run("first", "none", "one", span="alpha")
    at("2099-01-02T11:00")
    close_span.run("second", "none", "two", span="alpha")

    text = (trace.parent / "session-alpha.md").read_text(encoding="utf-8")

    assert text.count("# 2099-01-02\n") == 1
    assert text.count("## Close — ") == 2


def test_close_for_a_span_that_never_opened_is_refused_and_writes_nothing(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    open_span(None, "open; shared begins")
    before = snapshot(history)

    with pytest.raises(SystemExit) as refusal:
        close_span.run("state", "none", "next", span="ghost")

    assert "events-ghost.md" in str(refusal.value.code)
    assert snapshot(history) == before


def test_close_without_a_span_still_writes_the_shared_session(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    trace = open_span(None, "open; shared begins")
    at("2099-01-02T10:00")

    assert close_span.run("state", "none", "next") == 0

    assert sorted(path.name for path in trace.parent.iterdir()) == ["events.md", "session.md"]


BAD_SPANS = ["Alpha", "ALPHA-1", "a_b", "-a", "a-", "a--b", "a b", "", "a/b", "../x", "a.b", "alpha\n", "é", "events.md"]


@pytest.mark.parametrize("span", BAD_SPANS)
def test_a_bad_suffix_is_refused_on_event_with_exit_1_and_nothing_is_written(history: Path, at: Clock, span: str) -> None:
    at("2099-01-02T09:00")
    open_span(None, "open; shared begins")
    before = snapshot(history)

    result = runner.invoke(app, ["event", f"--span={span}", "self", "span-event", "open; begins"])

    assert result.exit_code == 1
    assert "refused" in result.output
    assert "[a-z0-9]+(-[a-z0-9]+)*" in result.output
    assert snapshot(history) == before


@pytest.mark.parametrize("span", BAD_SPANS)
def test_a_bad_suffix_is_refused_on_close_with_exit_1_and_nothing_is_written(history: Path, at: Clock, span: str) -> None:
    at("2099-01-02T09:00")
    open_span(None, "open; shared begins")
    before = snapshot(history)

    result = runner.invoke(app, ["close", f"--span={span}", "--state", "s", "--open", "none", "--next", "n"])

    assert result.exit_code == 1
    assert "refused" in result.output
    assert snapshot(history) == before


def test_the_cli_routes_event_and_close_to_the_spans_files(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    opened = runner.invoke(app, ["event", "--span", "alpha", "self", "span-event", "open;", "alpha", "begins"])
    at("2099-01-02T10:00")
    closed = runner.invoke(app, ["close", "--span", "alpha", "--state", "s", "--open", "none", "--next", "n"])

    day = history / "2099-01-02"
    assert opened.exit_code == 0 and closed.exit_code == 0
    assert opened.output.startswith(f"{day / 'events-alpha.md'}: 2099-01-02T09:00 | self | span-event | open; alpha begins")
    assert closed.output.startswith(f"{day / 'session-alpha.md'}: close block written")
    assert sorted(path.name for path in day.iterdir()) == ["events-alpha.md", "session-alpha.md"]


@pytest.mark.parametrize("span", ["alpha", "events", "review-events", "events-events", "a1-b2"])
def test_check_passes_on_a_tree_holding_a_suffixed_pair_with_and_without_a_close_block(history: Path, at: Clock, span: str) -> None:
    assert journal_findings() == [], "the copy of the live journal already fails before any span file is added"
    at("2099-01-02T09:00")
    open_span(span)
    at("2099-01-02T09:30")
    event_module.append_event("owner", "decision", "work goes on", span=span)
    assert journal_findings() == []

    at("2099-01-02T10:00")
    close_span.run("state", "none", "next", span=span)

    day = history / "2099-01-02"
    assert (day / f"session-{span}.md").is_file()
    assert journal_findings() == []


def test_check_flags_a_close_line_with_no_close_block_in_the_spans_session(history: Path, at: Clock) -> None:
    at("2099-01-02T09:00")
    trace = open_span("alpha")
    at("2099-01-02T10:00")
    event_module.append_event("self", "span-event", "close; HEAD abc1234 (clean); next: none", span="alpha")

    findings = journal_findings()

    assert [finding.where for finding in findings] == [str(trace.relative_to(check_records.ROOT))]
    assert "1 span closes but 0 close blocks in" in findings[0].message
    assert "session-alpha.md" in findings[0].message


def test_the_schema_homes_and_the_map_admit_suffixed_names() -> None:
    schema = check_records.load_schema()
    files = [DAY + "events-alpha.md", DAY + "session-alpha.md"]

    assert check_records.kind_of(schema, files[0]) == "trace"
    assert check_records.kind_of(schema, files[1]) == "digest"
    assert list(check_records.check_map(schema, files)) == []
    assert list(check_records.check_history_admission(files)) == []

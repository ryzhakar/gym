"""research sub-app: absorbs scripts/research/ (cache, books, bundle, search, sendback)."""

from pathlib import Path
from typing import List

import typer

from gym.research import books as books_mod
from gym.research import bundle as bundle_mod
from gym.research import cache as cache_mod
from gym.research import search as search_mod
from gym.research import sendback as sendback_mod

app = typer.Typer(help="Research sourcing: caching, books, bundles, search, sendback.")

TEAM_CHOICES = ("team-a", "team-b")


def _validate_team(team: str) -> str:
    if team not in TEAM_CHOICES:
        raise typer.BadParameter(f"invalid choice: {team!r} (choose from {TEAM_CHOICES})")
    return team


@app.command("books")
def books_cmd(
    team: str = typer.Argument(..., help="team-a or team-b", callback=_validate_team),
    batch: int = typer.Option(1, "--batch"),
    out: Path = typer.Option(books_mod.BUNDLES, "--out"),
) -> None:
    """Cut batch-1 books-courses rows into ~150k-char text bundles."""
    books_mod.build(team, batch, out)


@app.command("bundle")
def bundle_cmd(
    team: str = typer.Argument(..., help="team-a or team-b", callback=_validate_team),
    batch: int = typer.Option(1, "--batch"),
    out: Path = typer.Option(bundle_mod.BUNDLES, "--out"),
) -> None:
    """Cut a fetched batch into read-sized text bundles for extraction agents."""
    bundle_mod.build(team, batch, out)


@app.command("sendback")
def sendback_cmd(
    team: str = typer.Argument(..., help="team-a or team-b, e.g. team-a"),
    pass_name: str = typer.Argument(
        ..., help='pass to build: "R" (first send-back) or "T" (third pass)'
    ),
) -> None:
    """Build re-extraction bundles for batch-1 rows still logged 'nothing new'."""
    sendback_mod.build(team, pass_name)


cache_app = typer.Typer(help="Durable, append-only fetch cache for research agents.")
app.add_typer(cache_app, name="cache")


@cache_app.command("get")
def cache_get(doi_or_url: str = typer.Argument(...)) -> None:
    """Cache hit -> print text path; miss -> fetch, save, print path."""
    raise typer.Exit(code=cache_mod.cmd_get(doi_or_url))


@cache_app.command("ingest-tmp")
def cache_ingest_tmp() -> None:
    """Pull DOIs out of /tmp/*.pdf, cache each."""
    raise typer.Exit(code=cache_mod.cmd_ingest_tmp())


@cache_app.command("fetch-csv")
def cache_fetch_csv(
    csv_path: str = typer.Argument(...),
    status_csv: str = typer.Argument(cache_mod.DEFAULT_STATUS_CSV),
) -> None:
    """Fetch every row's url by source-class route; write a status csv."""
    raise typer.Exit(code=cache_mod.cmd_fetch_csv(csv_path, status_csv))


@cache_app.command("fetch-book")
def cache_fetch_book(url: str = typer.Argument(...)) -> None:
    """books-courses: fetch the whole book (print.html or a table-of-contents crawl)."""
    raise typer.Exit(code=cache_mod.cmd_fetch_book(url))


search_app = typer.Typer(help="Serial OpenAlex/Crossref search plus saturation post-processing.")
app.add_typer(search_app, name="search")


@search_app.command("run")
def search_run(
    queries: Path = typer.Argument(...),
    out: Path = typer.Argument(...),
    db: str = typer.Option("both", "--db", help="openalex, crossref, or both"),
    append: bool = typer.Option(False, "--append"),
) -> None:
    """Search every query, write one results csv."""
    if db not in ("openalex", "crossref", "both"):
        raise typer.BadParameter(f"invalid choice: {db!r} (choose from openalex, crossref, both)")
    search_mod.cmd_run(queries, out, db, append)


@search_app.command("found")
def search_found(
    out: Path = typer.Argument(...),
    found_md: Path = typer.Argument(...),
    sources: Path = typer.Option(search_mod.DEFAULT_SOURCES, "--sources"),
) -> None:
    """Distinct DOIs from a run, marked new/seen."""
    search_mod.cmd_found(out, found_md, sources)


@search_app.command("screen-list")
def search_screen_list(
    need: str = typer.Argument(...),
    files: List[Path] = typer.Argument(
        ..., help="results.csv... out.csv (last is the output)"
    ),
    sources: Path = typer.Option(search_mod.DEFAULT_SOURCES, "--sources"),
) -> None:
    """Union of distinct DOIs across capture files, for relevance screening."""
    if len(files) < 2:
        raise typer.BadParameter("screen-list needs at least one results.csv and an out.csv")
    *results_paths, out_path = files
    search_mod.cmd_screen_list(need, results_paths, out_path, sources)


@search_app.command("tally")
def search_tally(
    screen: Path = typer.Argument(...),
    results: List[Path] = typer.Argument(...),
) -> None:
    """Per-capture relevant counts, overlap, Chapman estimate, unseen fraction."""
    search_mod.cmd_tally(screen, results)

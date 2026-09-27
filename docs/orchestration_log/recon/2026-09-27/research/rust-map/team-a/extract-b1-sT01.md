For each source: where do competent Rust practitioners disagree?

Team a · batch 1 · third pass · slice T01 · bundle samples/bundles/b1-team-a-T01.txt · no fetches made.

## f000256 — Rust and WebAssembly (unknown, living document, en)

### Nothing new
The bundled text is the book's intro page only (table of contents, audience, reading order, contribution note, and the banner "This project and website is no longer maintained"), and it declares no Position on any decision.

Caveat: the frame row names the whole book. Chapters that plausibly hold declared Positions ("Why Rust and WebAssembly?", "Crates You Should Know", "Which Crates Will Work Off-the-Shelf") are separate pages. They are not in the bundle and were not read, because the dispatch forbids following links. This verdict covers the intro page only.

## f000508 — SE-0410: Atomics (2023-10-23, en)

### Nothing new
It is a Swift Evolution review of Swift's atomics API, and no Voice in it shows a public Rust track record in the source, so under the Voice bar (lead clarification 2026-09-27) its declared Positions are not Claims on Rust Questions.

Disclosed, not logged: the thread does hold declared, reasoned Positions on points that Rust concurrency code also decides. These are explicit ordering at every call versus a per-type default (@wadetregaskis 2023-10-23T21:42:02Z vs @Alejandro 2023-10-26T16:31:13Z), avoiding atomics in production (@lorentey 2023-10-25T23:14:07Z vs @wadetregaskis 2023-10-26T00:37:52Z), lock-freedom versus a spin bit (@lorentey vs @wadetregaskis), userspace spinlocks (@John_McCall 2023-11-03T19:05:58Z, @David_Smith 2023-11-04T07:10:12Z), back-off in compare-exchange loops (@John_McCall vs @dfunckt 2023-11-03T17:21:58Z) and traditional condition variables (@John_McCall 2023-11-02T20:44:24Z). Rust itself appears only in passing (@lorentey 2023-10-26T01:43:23Z, @Alejandro 2023-11-01T22:53:30Z, @John_McCall 2023-11-03T16:39:15Z).

## f000545 — Zen mode (2023-11-04, en)

### Nothing new
It is an editor UI feature request: which Zed chrome can be hidden, and settings profiles. The one maintainer statement (@JosephTLyons 2023-11-06T14:44:33Z, on keeping unsaved-buffer visibility before hiding tabs) is a product decision, with no Rust decision or Rust content anywhere in the thread.

## f000801 — Semantic search using OpenAI, pg_embedding and Neon (2024-01-24, en)

### Nothing new
It is a TypeScript/Next.js tutorial with no Rust content, and its one declared decision is a language-agnostic architecture choice, not a Rust practitioner's decision: store embeddings in Postgres (pg_embedding or pgvector) rather than "introduce an external vector store".

Caveats: the page byline reads "Aug 25, 2023" while the frame date is 2024-01-24. The author is Mahmoud Abdelwahab, and the source shows no Rust track record for him.

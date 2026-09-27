## f004772 — Add clickable path and symbol breadcrumb navigation (2026-06-05, en)

### Questions
- Q: When a UI component needs asynchronously-fetched data to render, should that data live in a cache on a shared owner object (populated by a hover/eager prefetch, read synchronously at render), or should the component itself own the async fetch and render a loading state until it resolves?
  concepts: state-ownership, async-data-fetching, API-design; domains_live: desktop-cli-ui; positions_seen: component-owns-async-lifecycle, cache-on-shared-owner

- Q: Should a test exercise a feature only by calling its internal methods directly against a bespoke test harness, or must at least one test dispatch the real keystroke/action through the actual UI entry point?
  concepts: testing-philosophy, integration-vs-unit-testing; domains_live: desktop-cli-ui, core; positions_seen: test-via-real-entry-point, test-via-internal-methods

- Q: Should code carry comments that narrate what a simple, self-evident line or private helper does, or should comments be reserved for non-obvious rationale, with narrating comments treated as noise to remove?
  concepts: code-comments, documentation, readability; domains_live: core, desktop-cli-ui; positions_seen: no-narrating-comments, comments-explain-behavior

- Q: When one project's open-source code is copied, stripped of branding, and rehosted by another developer without prior coordination, is that ordinary open-source practice or a breach of collaborative norms ("bad form")? — recurs here as: when a contributor's PR reuses another (unmerged) PR's code without first crediting or coordinating with its author, is that normal iterative open development or a lapse requiring attribution?
  concepts: open-source-governance, attribution, collaboration-norms; domains_live: core; positions_seen: branding-and-coordination-matter, no-entitlement-forking-is-core-of-oss

### Claims
- voice: SomeoneToIgnore | position: component-owns-async-lifecycle | date: 2026-08-06 | locator: comment @SomeoneToIgnore 2026-08-06T16:47:14Z | paraphrase: argues the hand-rolled outline cache, its hover-triggered prefetch, and its version-keyed invalidation are accidental complexity that exists only because the popover builder is synchronous; the fix is to let the menu entity spawn its own async fetch and render a loading state, "how every picker in Zed works" and how the PR's own path dropdown already behaves | quote: "let the menu entity fetch its own data asynchronously... That is how every picker in Zed works." | practiced_evidence: none
- voice: ysalitrynskyi | position: component-owns-async-lifecycle | date: 2026-08-07 | locator: comment @ysalitrynskyi 2026-08-07T17:45:21Z | paraphrase: reworked along the reviewer's architecture note rather than point-fixing; one async menu entity now fetches its own data per step, eliminating the cache, prefetch, and re-anchoring flag "by construction, not patched" | quote: "One async menu entity now serves both listings: fetches its own data (buffer_outline_items / expand_entry per step), no outline cache, no prefetch, no re-anchoring flag." | practiced_evidence: zed-industries/zed PR 58618 (post-rework)
- voice: SomeoneToIgnore | position: test-via-real-entry-point | date: 2026-08-06 | locator: comment @SomeoneToIgnore 2026-08-06T16:39:43Z | paraphrase: objects that tests drive the navigation/re-anchoring functions as plain method calls against a bespoke harness, so they would keep passing even if the real keybinding wiring broke; wants at least one test to dispatch the actual action via a keystroke against the real strip | quote: "At least one test should dispatch editor::OpenBreadcrumbs via a keystroke against the real strip." | practiced_evidence: none
- voice: SomeoneToIgnore | position: test-via-real-entry-point | date: 2026-08-07 | locator: comment @SomeoneToIgnore 2026-08-07T22:48:19Z | paraphrase: notes that even after a gesture-handling fix, "nothing tests the actual gesture" — the toggle/switch tests still drive the methods directly rather than the deferred mouse-event path itself | quote: "nothing tests the actual gesture: the toggle/switch tests drive the methods directly, the deferred up-out path itself has zero coverage." | practiced_evidence: none
- voice: SomeoneToIgnore | position: no-narrating-comments | date: 2026-08-07 | locator: comment @SomeoneToIgnore 2026-08-07T19:29:54Z | paraphrase: flags doc comments that narrate one-line private helpers and per-field docs as a repeating pattern across the file, arguing they should simply be deleted rather than kept or improved | quote: "doc comments narrating one-line private helpers... Same pattern all over the file... removing it all is way better than having them." | practiced_evidence: none
- voice: ysalitrynskyi | position: no-narrating-comments | date: 2026-08-18 | locator: comment @ysalitrynskyi 2026-08-18T21:51:50Z | paraphrase: complies by deleting the narrating comments across the touched files | quote: "Removed the duplicate and stripped the narrating comments across the files these changes touch." | practiced_evidence: zed-industries/zed PR 58618
- voice: SomeoneToIgnore | position: branding-and-coordination-matter | date: 2026-08-02 | locator: comment @SomeoneToIgnore 2026-08-02T15:31:14Z | paraphrase: points out a function copy-pasted almost verbatim, bugs included, from a different open PR (#62051), and asks that a co-authored-by credit be added if code was really copied from it | quote: "How come a different PR has the very same function, almost verbatim, copy-pasted from [...] Including all the worst bugs of it... If you have really copied parts of the other PR, do add a co-authored-by metadata to this PR and include @interkelstar into that." | practiced_evidence: none
- voice: ysalitrynskyi | position: branding-and-coordination-matter | date: 2026-08-02 | locator: comment @ysalitrynskyi 2026-08-02T18:58:14Z | paraphrase: concedes the point and adds attribution after the fact, crediting both prior PRs the navigation core derived from | quote: "Co-authored-by: Vlad Gevsky is now on the commits (including the base one), and the PR body credits both #62051 and #50719." | practiced_evidence: zed-industries/zed PR 58618 commits

---

## f004815 — Transaction Processing in the Data Plane (2026-06-17, en)

### Nothing new
`nothing new`: a solo technical article (Frank McSherry, Materialize) working through SQL-based transaction resolution and its performance tuning; no other Voice appears to contest any position — the appendix (co-written with Claude) reports measurements and fixes, not a disagreement between practitioners.

---

## f004865 — An iroh powered smart fan (2026-07-02, en)

### Nothing new
`nothing new`: a solo tutorial (Rüdiger Klaehn, iroh) walking through an ESP32 + iroh + irpc project end to end; states the author's own design choices (protocol evolution via appended enum variants, secret-gated RPC) with no contesting Voice present in this source.

---

## f004904 — What Is a Live Context Graph? (2026-07-16, en)

### Nothing new
`nothing new`: a vendor product/marketing post (Materialize) explaining a data-architecture pattern for AI-agent context; no Rust-specific content and no Voice with a public Rust track record states a contested position.

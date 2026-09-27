Framing: For each source, where do competent Rust practitioners disagree?

Note on dates: five sources below are gh-api-thread caches whose plain-text body strips per-comment usernames and timestamps, keeping only the thread's own date and any explicit `@mentions`. Where a Claim's voice is not self-signed or unambiguously named by a reply addressing them, no Claim is written — only a `positions_seen` label — and the Claim date used is the source's own date, not an individual comment timestamp.

## f000047 — Rust Web Programming, 1st Edition (2023-01-15, en)
### Nothing new
`nothing new` — UNREACHABLE: paywalled domain (packtpub.com), not attempted per owner ruling (not a scraping project); no content read.

## f000058 — Zero To Production In Rust: An introduction to backend development (2024-01-01, en)
### Nothing new
`nothing new` — UNREACHABLE: paywalled domain (amazon.com), not attempted per owner ruling (not a scraping project); no content read.

## f000083 — Embedded Software with Rust (2026-01-15, en)
### Nothing new
`nothing new` — UNREACHABLE: paywalled domain (manning.com), not attempted per owner ruling (not a scraping project); no content read.

## f000092 — Rust Projects - Write a Redis Clone (2026-09-10, en)
### Nothing new
`nothing new` — UNREACHABLE: paywalled domain (leanpub.com), not attempted per owner ruling (not a scraping project); no content read.

## f000120 — Xccelerate: Smart Contract and Solana dApps Development with Rust (unknown, en)
### Nothing new
`nothing new` — UNREACHABLE: paywalled domain (edx.org), not attempted per owner ruling (not a scraping project); no content read.

## f000149 — Small Rust Tutorial For MLOps (unknown, en)
### Nothing new
`nothing new` — cached capture is a table of contents and two link-out mentions only; no prose body was captured, so no disagreement is visible in this source.

## f000217 — nalgebra (unknown (living document), en)
### Nothing new
`nothing new` — cached capture (via Wayback, live fetch failed) is the one-paragraph "About nalgebra" landing blurb only; no argued position or disagreement is present.

## f000227 — Real-Time Interrupt-driven Concurrency (unknown (living document), en)
### Nothing new
`nothing new` — cached capture is a bare redirect stub ("If you are not redirected automatically, follow this link."), 75 characters, no article content was captured.

## f000256 — Rust and WebAssembly (unknown (living document), en)
### Nothing new
`nothing new` — cached capture is the book's intro/table-of-contents page only (notes the project "is no longer maintained"); no contested point appears in the captured text.

## f000508 — SE-0410: Atomics (2023-10-23, en)
### Nothing new
`nothing new` — full 728-line Swift Evolution review thread read; it is an extensive Swift standard-library API-design debate (naming, `var`/`let` and reference semantics, ordering views, memory-fence granularity), but every identified participant (Joe Groff, wadetregaskis, lorentey, John McCall, Doug Gregor, others) speaks as a Swift/C++ practitioner with no established Rust track record in this source, and the one Rust mention is a passing aside about C++/Rust precedent for a return type, not a debate; out of subject for the Rust map.

## f000530 — Explicit color conversion methods (2023-10-30, en)
### Questions
- Q: When Rust's lack of method overloading forces a choice for a type-conversion API surface (e.g. building a `Color` from `Vec4`, `[f32; 4]`, `Vec3`, `[f32; 3]` across several color spaces), should the API expose one explicitly-named method per source-type-and-color-space combination, or a smaller set of generic methods parameterized by a trait bound (`impl Into<T>`) or an enum discriminant?
  concepts: traits (`Into`), generics, enums, naming conventions, API surface size, absence of method overloading; domains_live: desktop-cli-ui; positions_seen: explicit-named-methods (st0rmbtw, PR author); generic `impl Into<T>` conversion (unattributed reviewer, raised as a question then partly walked back — "This only works for Vec4"); single constructor + `ColorSpace` enum discriminant (MrGVSV)
### Claims
- voice: st0rmbtw | position: one explicitly-named method per source type and color space | date: 2023-10-30 | locator: PR body, Objective/Changelog section | paraphrase: Proposes replacing the generic `Color::from(T)`/`T::from(Color)` conversions with one explicitly-named method per source type and per color space, so the target color space is always visible at the call site rather than inferred from context. | quote: "Added a new `Color::rgba_from_array([f32; 4]) -> Color` method." | practiced_evidence: bevyengine/bevy#10321 (own PR)
- voice: MrGVSV | position: single constructor plus a `ColorSpace` enum discriminant | date: 2023-10-30 | locator: PR comment, mid-thread (identity inferred from a later reply addressed "@MrGVSV I like the idea with the enum...") | paraphrase: Suggests a `ColorSpace` enum passed as a second constructor argument instead of one method per color space, to avoid multiplying method names for every combination. | quote: "I'm still wondering if it would make sense to introduce a `ColorSpace` enum and just specify that as a second parameter so we don't have to introduce a bunch of new methods for each color space." | practiced_evidence: none (idea not adopted per the PR's own changelog, which ships the one-method-per-combination design)

## f000538 — Dynamic Prop Labels (2023-11-01, en)
### Nothing new
`nothing new` — thread is implementation debugging (compiler-version support, wasm test failures, bundle-size and SSR benchmark diffs); the one meta-remark ("I have reviewed my own code - what does that mean?") is a passing aside, not a position anyone takes a stand against; no disagreement present.

## f000543 — Serializing FormData while form 'onsubmit'. (2023-11-04, en)
### Questions
- Q: When a UI framework's form-submission API hands back untyped, string-keyed values (e.g. a `HashMap<String, Vec<String>>`) for deserialization into a caller-defined struct via serde, should the ambiguity between a single value and a multi-value field (e.g. a multi-select) be resolved by an explicit schema/cardinality marker in the data, or by a permissive/heuristic deserializer that infers list-vs-scalar from the observed value count per field?
  concepts: serde deserialization, generic/untyped form data, ambiguous cardinality, API ergonomics vs. correctness; domains_live: frontend; positions_seen: reviewer (unattributed) — add an explicit list/scalar marker to the wire format, or make the deserializer polymorphic over single-value-vs-list; bunnyBites — infer list-vs-scalar from the observed value count per field, without changing the data shape
### Claims
- voice: bunnyBites | position: disambiguate scalar vs. list by observed value count (no schema change) | date: 2023-11-04 | locator: PR comment responding to review | paraphrase: For multi-valued elements like a `<select multiple>`, the deserializer should infer list-vs-scalar for a field from how many values were observed for it, rather than adding an explicit list/scalar marker to the wire format. | quote: "I think for multi-valued elements like select, we would expect the same result as the 'values' (vector/array of values), which we can get to know based on the length of values." | practiced_evidence: DioxusLabs/dioxus#1610 (own PR implementing `get_parsed_values`)

## f000545 — Zen mode (2023-11-04, en)
### Nothing new
`nothing new` — this is a feature request for editor UI customization (hiding tabs/gutter/statusbar) in the Zed editor; the one exchange resembling disagreement ("isn't SHIFT+ESC already delivering this?" / rebuttal that Zed's zoom is modal while true zen mode is config-controlled) is about editor UX conventions generic to any editor, not about the Rust language, its libraries, or its practices; out of subject for the Rust map.

## f000701 — Get error about missing "tracing" dependency when trying to use #[component] macro (2024-01-02, en)
### Questions
- Q: When a proc-macro conditionally emits a call into a crate (here, `tracing::instrument`) behind a feature flag inherited transitively through another crate's feature, should the macro hardcode an unqualified path that silently requires every downstream crate to independently declare that dependency in its own Cargo.toml, or should it use a fully-qualified/re-exported path so the hidden transitive requirement never surfaces as a downstream compile error?
  concepts: proc-macros, Cargo feature unification, hidden/transitive dependencies, macro hygiene; domains_live: frontend; positions_seen: DanielJoyce — treat it as a bug to fix by feature-gating (have `ssr` also enable `tracing`, or rework the macro's `cfg_attr`); a later, unattributed commenter — fix by using a fully-qualified `::tracing` path so the macro never assumes the invoking crate declared the dependency itself
### Claims
- voice: DanielJoyce | position: fix via feature-gating, not via requiring every downstream crate to declare the dependency | date: 2024-01-02 | locator: issue comment, mid-thread | paraphrase: Traces the root cause to `leptos_macro`'s `view!` macro unconditionally emitting `tracing::instrument` under `debug_assertions`/`ssr`, and proposes fixing it by having the `ssr` feature also enable `tracing`, or by reworking the macro's `cfg_attr` gating, rather than requiring every downstream crate to add `tracing` itself. | quote: "Fix is to have ssr feature also turn on tracing, or rework the cfg_attribute. Have not tested. ymmv" | practiced_evidence: none (issue reporter, does not ship the fix in this thread)

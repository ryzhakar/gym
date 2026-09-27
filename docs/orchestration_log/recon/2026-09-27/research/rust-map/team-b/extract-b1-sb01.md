## f000233 — Asynchronous Programming in Rust (unknown (living document), en)
### Nothing new
`nothing new` — the page is the book's own front matter, describing what async is and why it exists; it states no decision a practitioner must make, only motivation and a roadmap of missing parts.

## f000256 — Rust and WebAssembly (unknown (living document), en)
### Nothing new
`nothing new` — an unmaintained book's table of contents and audience note; no decision or conflict is stated on this page.

## f000267 — Zebra (unknown (living document), en)
### Nothing new
`nothing new` — install/build instructions and a GCC-15 workaround for a Zcash node; no decision point or disagreement appears on this page.

## f000464 — Quantized Implementations are slow (2023-10-06, en)
### Nothing new
`nothing new` — a benchmarking/troubleshooting thread where the maintainer (LaurentMazare) explains why quantized matmul is memory- vs compute-bound on Apple Accelerate; no second Voice argues a competing position, so no contested decision surfaces.

## f000493 — Variable `MeshPipeline` View Bind Group Layout (2023-10-17, en)
### Questions
- Q: Should combinatorial pipeline state be represented as an explicit generated array/struct of bool-driven variants, or as bitflags with named constants?
  concepts: bitflags, enums, combinatorial state, macros; domains_live: core; positions_seen: bitflags-preferred, explicit-array-generation
### Claims
- voice: superdump | position: bitflags-preferred | date: 2023-10-17 | locator: PR #10156, 2nd comment | paraphrase: the bool-per-combination approach used here "felt a bit off"; bit flags can generate combinations procedurally, take less space, and are arguably clearer with named constants (citing the bitflag crate) | quote: "Bit flags take a lot less space, and are arguably clearer when using named constants like the bitflag crate offers." | practiced_evidence: none
- voice: coreh | position: explicit-array-generation | date: 2023-10-17 | locator: PR #10156, 3rd comment | paraphrase: the two approaches are mostly the same in principle, but with 32 combinations here versus 6 in the prior PR, enumerating by hand is more daunting, which is why the code generates the array instead | quote: "The amount of combinations here (32) makes this a little bit more daunting to fully enumerate like that (6) which is why I added the code to generate it in an array." | practiced_evidence: https://github.com/bevyengine/bevy/pull/10156 (merged)

Note: the fetched bundle text for this PR carried comment bodies without author handles; `gh api repos/bevyengine/bevy/issues/10156/comments` was fetched to resolve exact Voice handles (nicopap, superdump, coreh, pcwalton), since a Claim requires an exact name and none of these could be reconstructed from memory.

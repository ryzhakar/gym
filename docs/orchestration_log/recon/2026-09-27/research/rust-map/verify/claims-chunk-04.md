| claim_id | verdict | corrected_locator | corrected_date | corrected_paraphrase | practiced | gap_url | note |
|---|---|---|---|---|---|---|---|
| a-sa14-f004947-c1 | CONFIRMED | | | | unknown | | quote exact, § What pvcli can do |
| a-sa14-f004985-c1 | CONFIRMED | | | | unknown | | quote exact, § Design decisions / Use Rust when possible |
| a-sa14-f004985-c2 | CONFIRMED | | | | unknown | | quote exact, § How we built it / Yes, but evals |
| a-sa14-f004985-c3 | CONFIRMED | | | | unknown | | quote exact, § Design decisions / Exception handling |
| a-sa14-f005079-c1 | CONFIRMED | | | | unknown | | quote exact, bjorn3 comment 2026-09-07T21:21:42Z |
| a-sa14-f005079-c2 | CONFIRMED | | | | unknown | | quote matches (omits leading "Personally"), alexcrichton comment 2026-09-08T18:52:06Z |
| a-sa14-f005079-c3 | CONFIRMED | | | | unknown | | quote exact, alexcrichton comment 2026-09-08T14:23:10Z |
| a-sa14-f005079-c4 | CONFIRMED | | | | unknown | | all 4 comments verified verbatim (fcntl_setfd, fstat, getsockname, socket_type sockopt) at listed timestamps |
| a-sa14-f005079-c5 | CONFIRMED | | | | unknown | | quote exact, alexcrichton comment 2026-09-09T04:31:28Z |
| a-sa14-f005079-c6 | CONFIRMED | | | | unknown | | source comment has typo "therea re"; claim quote silently normalizes to "there are" — meaning unaffected |
| a-sa14-f005149-c1 | CONFIRMED | | | | unknown | | quote exact, § Enter Snafu: The Hybrid Approach; post is co-authored (dig, b5, ramfox), b5 is credited co-author |
| a-sa14-f005149-c2 | CONFIRMED | | | | unknown | | quote exact, § Error enums are scoped to functions not modules |
| a-sa14-f005149-c3 | CONFIRMED | | | | unknown | | quote exact, § Errors for public traits should contain a Custom variant |
| a-sa14-f005162-c1 | CONFIRMED | | | | unknown | | quote exact, § Rust for Microcontrollers; 1675/1050-instruction figures both verified; gap:voice-unverified stands (byline is "Jonathan", no surname on page) |
| a-sa14-f005360-c7 | CONFIRMED | | | | unknown | | quote exact, @pm comment 2024-10-13T14:37:28 (-05:00); gap:voice-unverified stands |
| a-sa14-f005454-c3 | CONFIRMED | | | | unknown | | quote exact, @sunshowers comment 2025-02-24T16:37:04 |
| a-sa15-f005516-c1 | CONFIRMED | | | | unknown | | quote matches lobste.rs blockquote citing Cantrill's YouTube talk exactly as locator describes ("blockquote citing") |
| a-sa15-f005604-c1 | CONFIRMED | | | | unknown | | quote exact, § Technology choice; claim date 2023-03-02 matches article's own dateline (source.yaml's date field of 2025-11-03 is a fetch-date mismatch, not a claim fault) |
| a-sa15-f005821-c1 | UNFAITHFUL | § Performance results (ARM64/x86-64 tables); the WASM 1.2–4.6x figures are in the later § One more thing section | | ARM64/x86-64 benchmark portions confirmed verbatim. The WASM portion overstates the source: the post never ties the WASM slowdown to "register spills to the stack" — that codegen observation is made earlier about native x86 tail-call output. The stated reason for the WASM numbers is only "patterns which generate good assembly don't map well to the WASM stack machine, and the JITs aren't smart enough to lower it to optimal machine code." | unknown | | numeric figures (1.2x Firefox, 3.7x Chrome, 4.6x wasmtime) all verified against the table |
| a-sa15-f005821-c2 | CONFIRMED | | | | unknown | | quote exact, opening paragraphs linking "Experimenting with LLMs" |
| a-sa15-f005857-c1 | CONFIRMED | | | | unknown | | quote exact, § Building a UI and § Putting it all together |
| a-sa15-f005948-c1 | CONFIRMED | opening paragraph (first sentence of the post) + § Edge cases and errors (second sentence) | | | unknown | | quote exact but spans two locations: "This was tricky!..." is the post's opening line, before the "Edge cases and errors" heading named in the claim; 99.7%/502 figure also verified |
| a-sa15-f006797-c1 | CONFIRMED | | | | unknown | | quote exact, § Se buscan probadores |
| a-sa16-f007175-c1 | CONFIRMED | | | | unknown | | quote exact, § Modularity of HandleSimpleExec |
| a-sa16-f007175-c2 | CONFIRMED | | | | unknown | | quote exact, § Disadvantages / Dynamic Loading |
| a-sa16-f007483-c1 | CONFIRMED | | | | unknown | | quote exact, § Native Libraries closing line |
| a-sa16-f007483-c2 | CONFIRMED | | | | unknown | | quote exact, § Scripting language closing line |
| a-sa16-f007483-c3 | CONFIRMED | | | | unknown | | quote exact, § WASM closing line |
| a-sa16-f007483-c4 | CONFIRMED | | | | unknown | | quote exact, § Expression engine closing line |
| a-sa17-f007736-c1 | CONFIRMED | | | | unknown | | quote exact |
| a-sa17-f007797-c1 | CONFIRMED | | | | unknown | | quote exact |
| a-sa17-f007846-c1 | CONFIRMED | | | | unknown | | quote exact, § Sharing an Iterator Over the Available IDs → § The Final Solution |
| a-sa17-f008217-c1 | CONFIRMED | | | | unknown | | quote exact, § The role of the supervisor in Hubris |
| a-sa17-f008217-c2 | CONFIRMED | | | | unknown | | quote exact, § Who supervises the supervisor? |
| a-sa18-f008389-c1 | CONFIRMED | | | | unknown | | quote exact, § How procedural macros made it better |
| a-sa18-f008583-c1 | CONFIRMED | | | | unknown | | quote exact, § Error logging |
| a-sa18-f008651-c1 | CONFIRMED | | | | unknown | | quote exact, § Another "abstraction" to the repository layer; closing "would you consider this to be extreme?" line verified |
| a-sa18-f008694-c1 | CONFIRMED | | | | unknown | | quote exact, "atomic levels and data dependencies" onward; two-stage fingerprint / name-resolution mechanism verified further down the talk script |
| a-sa18-f008787-c1 | CONFIRMED | | | | unknown | | quote exact; 24MB/7.1GB/300x, <100ms/~3s, wgpu/ndarray/WASM/Tauri all verified (source fetched via Wayback Machine snapshot) |
| a-sa18-f009026-c1 | CONFIRMED | | | | unknown | | quote exact, § Final words; 360 configs / 90 scenarios, io_uring vs epoll, and 8/12-thread anomaly all verified. Page carries no visible dateline to check against claim's 2026-08-05 |
| a-sa18-f009104-c1 | CONFIRMED | | | | unknown | | quote exact, § These features make me uneasy |
| a-sa18-f009104-c2 | CONFIRMED | | | | unknown | | quote exact, § I'm okay with named parameters now; patterns-not-names, function-value name erasure, left-to-right evaluation order (consume(data, data.len()) example), and rename-breaks-callers all verified further in the section |

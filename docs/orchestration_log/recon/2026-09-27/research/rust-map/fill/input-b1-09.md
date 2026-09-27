# Blind fill input, batch 1, file 09 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `pac-crate-per-chip-vs-shared`

One shared PAC crate with features, or one per chip?

Positions:
- `pac-crate-per-chip-vs-shared--single-crate-with-features`: One shared crate
- `pac-crate-per-chip-vs-shared--alt1`: A separate PAC crate per chip

Claims:
- `a-sa01-f001838-c1` · Voice: CBJamo · Source: https://github.com/embassy-rs/embassy/pull/3243 (`f001838`) · Date: 2024-08-09 · Locator: PR comment, mid-thread (rp-pac#5 follow-up)
  - Quote: "I had assumed it'd be hard to do, but it wasn't too bad. I just updated the update.sh to make both and hand wrote a tiny lib.rs. Features did indeed clean up with the single pac."
  - Paraphrase: After a reviewer argued for the `stm32-metapac` pattern (one PAC crate covering related chips, feature-gated) over separate per-chip crates, the PR author reports it was easier than expected and that Cargo features "cleaned up" once unified into a single `rp-pac`.
- `b-sb06-f001838-c1` · Voice: Dirbaio · Source: https://github.com/embassy-rs/embassy/pull/3243 (`f001838`) · Date: 2024-08-09 · Locator: PR #3243, comment 2024-08-09T07:14:06Z
  - Quote: "I think we should add rp235x to `rp-pac` (`stm32-metapac` style) instead of making separate crates per chip (`nrfxxx-pac` style). It's much less annoying to release and manage Cargo features."
  - Paraphrase: prefers adding rp235x support to the existing `rp-pac` crate (the `stm32-metapac` pattern) rather than a new per-chip crate (the `nrfxxx-pac` pattern already used elsewhere in the embassy org), since it's much less annoying to release and manage Cargo features

## Question `paid-maintainers-for-infrastructure`

Volunteers or funded maintainers for critical Rust infrastructure?

Positions:
- `paid-maintainers-for-infrastructure--fund-maintainers`: Fund dedicated maintainers
- `paid-maintainers-for-infrastructure--alt1`: Rely on volunteer maintainers

Claims:
- `a-sR15-f009751-c2` · Voice: Jonas Böttiger (@joboet) · Source: https://blog.rust-lang.org/2026/08/26/announcing-our-first-maintainers-in-residence (`f009751`) · Date: 2026-08-26 · Locator: bio section "Jonas Böttiger (@joboet)"
  - Quote: "Getting funding for my work is a dream come true. It will allow me to continue doing the thing I love instead of worrying about whether I should rather invest all that time in a money-earning job with much less positive impact on the world around me."
  - Paraphrase: funding removes the tradeoff between doing the maintenance work he loves and taking a better-paid job elsewhere
- `a-sR15-f009751-c1` · Voice: Alejandra González (@blyxyas) · Source: https://blog.rust-lang.org/2026/08/26/announcing-our-first-maintainers-in-residence (`f009751`) · Date: 2026-08-26 · Locator: bio section "Alejandra González (@blyxyas)"
  - Quote: "Funding is the system that helps me pour my heart into a project without worrying about making ends meet. Having those needs met is a game-changer and boosts my productivity."
  - Paraphrase: being funded lets her put her full effort into the project without financial anxiety, directly boosting her productivity
- `b-sR13-f009755-c1` · Voice: Jakub Beránek, on behalf of the Rust Funding team · Source: https://blog.rust-lang.org/2026/09/22/announcing-a-maintainer-in-residence-scott-schafer-for-the-cargo-team (`f009755`) · Date: 2026-09-22 · Locator: "Why Cargo?" section
  - Quote: "Even though we know that a single full-time maintainer will not completely solve the maintenance struggles of the Cargo team, we hope that it will improve the situation"
  - Paraphrase: the Cargo team "struggled with meeting its maintenance demands" after members left or lost funding, so the Funding team used Leadership Council and AWS money to open a new full-time Maintainer in Residence position; explicitly framed as partial relief, not a full fix

## Question `parser-combinator-vs-generator`

Should Rust developers write parsers with a combinator library (nom) rather than a grammar-based generator (pest, lalrpop) or a hand-rolled recursive-descent parser?

Positions:
- `parser-combinator-vs-generator--p1`: Nom-style parser combinators are the effective way to build parsers in Rust: small composable functions, no unnecessary allocation, and richer error reporting via VerboseError/context than a naive hand-rolled parser would give you
- `parser-combinator-vs-generator--alt1`: A grammar-based generator (pest, lalrpop)
- `parser-combinator-vs-generator--alt2`: a hand-rolled recursive-descent parser

Claims:
- `b-sR13-f007973-c1` · Voice: Nazmul Idris (r3bl_tui maintainer) · Source: https://developerlife.com/2023/02/20/guide-to-nom-parsing (`f007973`) · Date: 2023-02-20 · Locator: "Getting to know nom using lots of examples" section
  - Quote: "nom is very efficient and fast, it does not allocate memory when parsing if it doesn't have to"
  - Paraphrase: "nom is very efficient and fast, it does not allocate memory when parsing if it doesn't have to, and it makes it very easy for you to do the same"; the article goes on to show context/convert_error as the way to get human-readable error messages out of a combinator chain

## Question `persistent-collections-cheap-clone`

Should Rust's collections behave like true persistent (structural-sharing) values with cheap clone, rather than accepting the current model where clone is a full deep copy?

Positions:
- `persistent-collections-cheap-clone--p1`: Rust would benefit from persistent, structural-sharing vector types (RRB trees) that make clone cheap (O(log n) path-copying) instead of the O(n) deep copy that ordinary owned collections force today
- `persistent-collections-cheap-clone--alt1`: Keep deep-copy clone semantics

Claims:
- `b-sR13-f008801-c1` · Voice: Araz Abishov · Source: https://abishov.com/blog/pvec-rs-visualizing-structural-sharing (`f008801`) · Date: 2026-02-12 · Locator: opening paragraphs, before "A quick intro to persistent vectors"
  - Quote: "Rust collections already behave like values; they just have an expensive clone."
  - Paraphrase: "Ownership means you must clone a vector if you want to keep using it after passing it somewhere else. As Niko Matsakis pointed out, Rust collections already behave like values; they just have an expensive clone. What if that clone could be nearly free?" — this framing motivates building pvec-rs

## Question `pin-for-non-relocatable-cpp-types`

For C++ types that cannot be relocated via a simple memcpy (self-referential types, e.g. small-string-optimized `std::string`), should Rust FFI bindings represent them using `Pin`, given Rust's general assumption that all types are memcpy-movable?

Positions:
- `pin-for-non-relocatable-cpp-types--p1`: Yes pin is the emerging convention
- `pin-for-non-relocatable-cpp-types--alt1`: Treat the types as memcpy-movable like other Rust types

Claims:
- `b-sb24-f011312-c5` · Voice: Taylor · Source: https://youtube.com/watch?v=Z5M4NIWoMJQ (`f011312`) · Date: 2025-10-03 · Locator: [25:34]-[27:36]
  - Quote: "Thankfully, there's growing support for using Russ's pin type to represent values that can't be memcopy relocated."
  - Paraphrase: unsafe Rust code has long assumed all types can be relocated by bitwise memcopy, but most C++ types run a move constructor (e.g. small-string-optimized `std::string` stores a pointer into its own inline buffer); there's growing support for representing such non-memcopy-movable values with `Pin`, though the same aliasing/projection/auto-ref ergonomics gaps still apply to them

## Question `pin-project-vs-pin-project-lite`

For pin projection, should a crate use the `pin-project` procedural-macro crate or the `pin-project-lite` declarative-macro crate?

Positions:
- `pin-project-vs-pin-project-lite--p1`: Pin-project-lite to avoid proc-macro deps, pin-project otherwise
- `pin-project-vs-pin-project-lite--alt1`: Always `pin-project`
- `pin-project-vs-pin-project-lite--alt2`: always `pin-project-lite`

Claims:
- `b-bk01-f000233-c9` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Pinning" § Macros for pin projection
  - Quote: "Pin-project-lite is recommended if you want to avoid adding the procedural macro dependencies, and pin-project is recommended otherwise."
  - Paraphrase: pin-project-lite is a declarative-macro alternative to the pin-project procedural macro, recommended when a project wants to avoid adding procedural-macro dependencies, at the cost of being less expressive and giving no custom error messages; pin-project is recommended otherwise.

## Question `pin-vs-move-constructors`

Should Rust have solved self-referential futures with a `Move` marker trait or C++-style move constructors instead of `Pin`?

Positions:
- `pin-vs-move-constructors--p1`: Pin's phased/place-based design over Move-trait or move-constructor alternatives
- `pin-vs-move-constructors--alt1`: A `Move` marker trait
- `pin-vs-move-constructors--alt2`: C++-style move constructors

Claims:
- `b-bk01-f000233-c10` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Pinning" § Alternatives and extensions
  - Quote: "The fundamental problem with this approach is that pinning today is a phased concept ... and types apply to the whole lifetime of values."
  - Paraphrase: explains and defends why Rust did not solve self-referential futures with a `Move` marker trait (rejected: pinning is phased per-place while traits apply to a value's whole lifetime, and a Move trait would create widely "infectious" bounds plus backward-compatibility breakage) or C++-style move constructors (rejected: breaks Rust's invariant that objects can always be bitwise-moved, silently breaking unsafe code, and cannot fix up references held from outside the moved object).

## Question `platform-gating-feature-vs-target-cfg`

should platform-specific code be gated behind a Cargo feature flag, or behind a `#[cfg(target...)]`/target-triple check once the platform is a proper Rust target?

Positions:
- `platform-gating-feature-vs-target-cfg--p1`: Prefer target-based gating over feature flags once the target is stabilized
- `platform-gating-feature-vs-target-cfg--alt1`: Gate with a Cargo feature flag

Claims:
- `b-sR05-f002151-c2` · Voice: brooksmtownsend (wasmCloud engineer; contributor to mio/tokio-rs WASI socket support) · Source: https://github.com/leptos-rs/leptos/pull/3063 (`f002151`) · Date: 2024-10-11 · Locator: leptos-rs/leptos#3063, comment 2024-10-11T13:37:26Z. · L1290-L1291.
  - Quote: "Once `wasm32-wasip2` is a stable target in Rust (coming in 1.82 afaik) the use of feature flags could be simplified, using the target directive instead."
  - Paraphrase: prefer target-based gating over feature flags once the target is stabilized.

## Question `platform-logic-module-vs-inline`

When adding a small piece of platform-specific logic used by only one call site, should it be factored into its own module/abstraction, or kept inline in the one file that uses it to minimize `#[cfg]` surface and review burden?

Positions:
- `platform-logic-module-vs-inline--p1`: Keep platform-specific logic inline rather than a separate abstraction
- `platform-logic-module-vs-inline--alt1`: Factor it into its own module or abstraction

Claims:
- `a-sa14-f005079-c5` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/14294 (`f005079`) · Date: 2026-09-09 · Locator: comment 2026-09-09T04:31:28Z
  - Quote: "Personally I would prefer to keep all the `serve.rs`-related code in `serve.rs` and avoid extra abstractions here (which have more #[cfg] which is more to validate, etc)."
  - Paraphrase: prefers keeping all `serve.rs`-related code in `serve.rs`, marking the helper `unsafe` with a `// SAFETY` comment at the call site, over introducing a separate module with more `#[cfg]`s to validate

## Question `plugin-system-mechanism`

How should a Rust application implement a plugin system: native dynamic libraries, an embedded scripting language, WebAssembly, or an expression/rules engine?

Positions:
- `plugin-system-mechanism--p1`: Native dylib rejected
- `plugin-system-mechanism--p2`: Scripting language preferred
- `plugin-system-mechanism--p3`: Wasm too immature
- `plugin-system-mechanism--p4`: Expression engine for bounded untrusted eval

Claims:
- `a-sa16-f007483-c2` · Voice: Sylvain Kerkour · Source: https://kerkour.com/rust-plugin-system (`f007483`) · Date: 2026-08-18 · Locator: § Scripting language, closing paragraph
  - Quote: "For all these reasons I recommend embedding QuickJS to build a plugin system as the default approach, and to evaluate the other methods only if there are too many drawbacks for your specific use case."
  - Paraphrase: Recommends embedding QuickJS (over V8/deno_core and over Lua) as the default plugin approach: small binary size, no JIT, faster cold starts, easier integration.
- `a-sa16-f007483-c3` · Voice: Sylvain Kerkour · Source: https://kerkour.com/rust-plugin-system (`f007483`) · Date: 2026-08-18 · Locator: § WASM, closing paragraph
  - Quote: "I think that WebAssembly is currently too immature to be used for a plugin system and will make the life of developers wanting to create plugins hard."
  - Paraphrase: Judges WebAssembly currently too immature for a Rust plugin system despite its sandboxing strength, citing uneven cross-language WASM support and churning toolchains/targets (WASI p1, p2).
- `a-sa16-f007483-c4` · Voice: Sylvain Kerkour · Source: https://kerkour.com/rust-plugin-system (`f007483`) · Date: 2026-08-18 · Locator: § Expression engine, closing paragraph
  - Quote: "expressions evaluating to a bool is the easiest and safest way to achieve that, but for most projects I would recommend integrating QuickJS."
  - Paraphrase: For his own project he forked CEL to a boolean-only subset because non-Turing expression languages give bounded, predictable-runtime evaluation of untrusted user input; recommends QuickJS instead for most other projects.
- `a-sa16-f007483-c1` · Voice: Sylvain Kerkour · Source: https://kerkour.com/rust-plugin-system (`f007483`) · Date: 2026-08-18 · Locator: § Native Libraries
  - Quote: "For all these reasons I don't recommend using dynamic libraries as plugins."
  - Paraphrase: Rejects native dynamic libraries as a Rust plugin mechanism: no stable ABI, no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder for users to share/audit than scripts.

## Question `pointer-addr-vs-as-usize`

When converting a raw pointer to an integer for a low-level hook/tracking API, should you cast with `as usize` or use the provenance-preserving `.addr()`?

Positions:
- `pointer-addr-vs-as-usize--p1`: Prefer `.addr()` over `as usize` for pointer-to-integer conversion
- `pointer-addr-vs-as-usize--alt1`: Cast with `as usize`

Claims:
- `a-sa11-f004512-c1` · Voice: renkenono · Source: https://github.com/esp-rs/esp-hal/pull/5296 (`f004512`) · Date: 2026-04-01 · Locator: comment 2026-04-01T19:13:38Z; 2026-04-01T21:50:33Z
  - Quote: "Casting the pointer to `usize` has implicit behavior e.g., in relation to provenance... I'd recommend using `addr()` instead"
  - Paraphrase: flags that casting a pointer to `usize` has implicit behavior around provenance, recommends `.addr()` since provenance isn't needed here and it "has a more explicitly defined behavior"

## Question `polonius-scope-cut`

When a new borrow-checker algorithm (Polonius) trades full expressiveness parity with the old implementation for an easier path to production-readiness, should the project accept the narrower formulation (and its known false positive on one loop/region case) to ship sooner, or hold out for full expressiveness?

Positions:
- `polonius-scope-cut--p1`: Cut scope for shippability
- `polonius-scope-cut--alt1`: Hold out for full expressiveness parity

Claims:
- `a-sa20-f009698-c3` · Voice: @lqd · Source: https://blog.rust-lang.org/2025/05/26/april-project-goals-update (`f009698`) · Date: 2025-05-05 · Locator: "Scalable Polonius support on nightly" section, comment posted 2025-05-05
  - Quote: "we're currently discussing whether we can cut scope here, as this formulation accepts NLL problem case 3. We'll need to evaluate what limits this formulation imposes on expressiveness... and whether it indeed has an easier path to becoming production ready."
  - Paraphrase: reports the current datalog-based approximation of Polonius handles all UI tests except a case where loop control flow connects regions live before/after the loop, producing a false positive their older, slower, more comprehensive approach used to accept correctly; the team is actively discussing whether to cut scope and accept this formulation (which accepts "NLL problem case 3") in exchange for an easier path to production, while still evaluating what expressiveness limits it would impose outside that case

## Question `portable-async-vs-sync-io`

Should a portable crate needing I/O expose synchronous or async I/O, and how should it abstract wasm vs native?

Positions:
- `portable-async-vs-sync-io--p1`: For I/O that a portable library must perform itself, go async (generic over a Future type), or split by target with a trait plus #[cfg]-gated impls — never synchronous
- `portable-async-vs-sync-io--alt1`: Synchronous I/O

Claims:
- `b-bk02-f000256-c6` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "How to Add WebAssembly Support to a General-Purpose Crate" → Avoid Synchronous I/O
  - Quote: "If you must perform I/O in your library, then it cannot be synchronous. There is only asynchronous I/O on the Web."
  - Paraphrase: states synchronous I/O is a non-option on the Web, then names two concrete alternative architectures — a function generic over `F: Future`, or a trait implemented once per target behind `#[cfg(target_arch = "wasm32")]` — without picking one as universally superior.

## Question `portable-kernels-performance-cost`

Can one compute framework abstract kernel programming over both GPU and CPU without sacrificing performance, or does hardware-portable abstraction necessarily cost performance versus a hardware-specific implementation?

Positions:
- `portable-kernels-performance-cost--p1`: Comptime specialization avoids the tradeoff
- `portable-kernels-performance-cost--alt1`: Hardware portability necessarily costs performance

Claims:
- `a-sa09-f004016-c2` · Voice: nathanielsimard · Source: https://burn.dev/blog/burn-end-of-the-year-review (`f004016`) · Date: 2025-12-19 · Locator: § "CubeCL Architecture"
  - Quote: "The common consensus in the industry is that it is impossible to abstract GPU and CPU programming without sacrificing performance. However, through intentional design, we have succeeded in proving otherwise."
  - Paraphrase: claims CubeCL disproves the assumed GPU/CPU portability-performance tradeoff by using `comptime` to specialize kernels per plane size and line size, including setting plane size to 1 for the CPU runtime rather than simulating GPU execution

## Question `porting-to-rust-safety`

Does a straight port of C or C++ to Rust give memory safety?

Positions:
- `porting-to-rust-safety--naive-port-not-safe`: No; restructure or risk new UB
- `porting-to-rust-safety--alt1`: A straight port yields memory safety once it compiles

Claims:
- `b-sb24-f011312-c4` · Voice: Taylor · Source: https://youtube.com/watch?v=Z5M4NIWoMJQ (`f011312`) · Date: 2025-10-03 · Locator: [17:27]-[18:27]
  - Quote: "This is a huge issue for gradual C++ to Rust migration... This is terrible. Rust, you were supposed to destroy the undefined behavior, not join it."
  - Paraphrase: pure Rust can't create mutably-aliasing references, so if a ported function relies on C++'s permissive aliasing (e.g. a mutable reference/field that in fact aliases other pointers), naively translating it into Rust and letting the optimizer assume exclusivity can silently change program behavior and introduce new undefined behavior that wasn't present in the original C++
- `a-sa21-f011069-c4` · Voice: Aleksandr Petrosyan · Source: https://youtube.com/watch?v=LO7tvIed-YQ (`f011069`) · Date: 2023-11-15 · Locator: ~00:10:50-00:11:10
  - Quote: "Getting rid of memory leaks turned out to be a lot harder... because of the... way in which the code was organized didn't really allow me to refactor it into a safe version."
  - Paraphrase: Chose Rust partly to eliminate memory leaks and undefined behavior, but found this harder than expected because the existing C-style code's organization didn't allow refactoring into a safe version — implying a straight port that preserves the original architecture does not by itself deliver Rust's safety benefits.

## Question `postfix-await`

Should `.await` be a postfix operator (`fut.await`) or a prefix operator, as in Python/JavaScript (`await fut`)?

Positions:
- `postfix-await--p1`: Postfix `.await`
- `postfix-await--alt1`: Prefix `await`

Claims:
- `b-bk01-f000233-c1` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Async and Await" § await
  - Quote: "This is in contrast to languages like Python or JavaScript, where await is a prefix operator"
  - Paraphrase: postfix `.await` is more ergonomic than prefix await in chains of method calls and field accesses; contrasts `fetch().await?.status_code` against the prefix-syntax equivalent `(await fetch())?.status_code`, calling the postfix form more natural to read in longer chains.

## Question `pre-1-0-api-default-stability`

Before a crate's 1.0 release, should an unreviewed API surface (e.g. the interrupt API) default to stable unless a blocker is raised, or stay marked unstable until the team explicitly agrees it is ready?

Positions:
- `pre-1-0-api-default-stability--p1`: Stable unless flagged
- `pre-1-0-api-default-stability--p2`: Unstable until agreed ready

Claims:
- `b-sb08-f002517-c1` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/2900 (`f002517`) · Date: 2025-01-10 · Locator: comment 2025-01-10T12:44:33Z
  - Quote: "if there isn't anything else then I don't see any issue in exposing this as stable, at least for now."
  - Paraphrase: without a known blocking issue, sees no problem exposing the interrupt API as stable for now, having assumed the team was already aligned
- `b-sb08-f002517-c2` · Voice: Dominaezzz · Source: https://github.com/esp-rs/esp-hal/pull/2900 (`f002517`) · Date: 2025-01-10 · Locator: comment 2025-01-10T12:26:08Z
  - Quote: "The PRs targeting interrupts so far have done so under the assumption that they won't be stabilized."
  - Paraphrase: objects that interrupts are being stabilized, since prior PRs assumed they would stay unstable and some interrupt enum variants don't make sense for the CPU-driven driver
- `b-sb08-f002517-c3` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/2900 (`f002517`) · Date: 2025-01-10 · Locator: comment 2025-01-10T13:08:42Z
  - Quote: "After some push back, I'm 180'ing. I agree with the general consensus that the interrupt API might not be ready."
  - Paraphrase: after push back, reverses course and agrees the interrupt API isn't ready, marking it unstable for now

## Question `pre-1-0-canary-releases`

Before a crate's 1.0 release, should breaking changes ship frequently in a fast pre-release ("canary") channel to get user feedback quickly, or should a team hold changes until they are fully finished before cutting each release?

Positions:
- `pre-1-0-canary-releases--p1`: Frequent canary releases for fast feedback
- `pre-1-0-canary-releases--alt1`: Hold changes until they are fully finished before each release

Claims:
- `b-sb10-f003188-c1` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-90-the-canary-series (`f003188`) · Date: 2025-06-27 · Locator: blog body, paragraph beginning "Last time we published a release blog"
  - Quote: "we realized that waiting until we had everything worked through and finished before releasing was not actually the best way for us to get a stable release into the hands of our users."
  - Paraphrase: waiting until everything was fully finished before releasing was not the best way to get a stable release into users' hands; three-week cycles and fast canary releases before 1.0 get feedback quickly and let the team move with confidence

## Question `predicate-rules-vs-first-match`

Should conditional configuration logic be expressed as independent boolean-predicate rules whose interaction is implicit, or as an ordered list of rules where the first matching condition wins?

Positions:
- `predicate-rules-vs-first-match--p1`: Ordered first match wins
- `predicate-rules-vs-first-match--alt1`: Independent boolean-predicate rules

Claims:
- `b-sb09-f003030-c8` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-06-11 · Locator: comment @bugadani 2025-06-11T07:49:35Z
  - Quote: "What if we turned this into a match-style \"first condition wins\" situation?"
  - Paraphrase: after bjoernQ's predicate-function design produced a real bug (two mutually exclusive conditions both false), proposes redesigning the conditional rules as an ordered list evaluated first-match-wins.

## Question `proc-macro-derives-vs-reflection-shape`

Per-trait proc-macro derives, or runtime reflection shape data (facet)?

Positions:
- `proc-macro-derives-vs-reflection-shape--proc-macros-costly`: Proc macros are costly and unsolved
- `proc-macro-derives-vs-reflection-shape--ship-shape-data`: Ship shape data; reflection avoids annotation gaps
- `proc-macro-derives-vs-reflection-shape--reflection-doesnt-clearly-win`: Reflection's runtime cost is real and a JIT is no general answer

Claims:
- `a-sa25-f011413-c1` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: ~00:02:04–00:02:37
  - Quote: "why is a pure AST transform shaped as a rust source we have to compile and optimize and run and... [grant] it full disk and network access just in case"
  - Paraphrase: procedural macros are a pure AST transform shaped as Rust source that the compiler must compile, optimize, run, and grant disk/network access to "just in case"; many people have tried to fix this and nothing has stuck
- `b-sb24-f011413-c1` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: [02:09]-[04:09]
  - Quote: "Instead of trying to turn our types into more code... we might consider shipping data about our types."
  - Paraphrase: every new Rust behavior (Debug, Display, Deserialize, ...) tends to spawn its own trait and proc-macro derive; proc macros are costly (compile/optimize/run arbitrary code with disk/network access) and each new derive macro has to independently win ecosystem-wide adoption because of orphan rules; facet instead derives a single associated `SHAPE` constant per type (name, offset, alignment, type id, variants, attributes, doc comments, ...) that many downstream behaviors (a colorized Debug, structural diffing, CLI parsing, JSON Schema export, TypeScript codegen) can all consume from one derive
- `a-sa25-f011413-c4` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: ~00:06:23–00:07:00
  - Quote: "Uh I was wrong... performance is worse. Runtime performance is worse... it by by design it is much slower and that's a fact of life. You can do nothing to change that."
  - Paraphrase: he expected reflection to trade only build time for runtime speed, but measured build times as "a wash" and runtime performance as unconditionally worse ("100%" in the case shown), calling this inherent to reflection-based systems
- `b-sb24-f011413-c3` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: [05:09]-[09:12]
  - Quote: "This is a negative result that I have to report... the build times are like meh... performance is worse. Runtime performance is worse. We were right about that."
  - Paraphrase: he expected reflection to trade worse runtime performance for meaningfully better build times versus Serde's generated code, but build times turned out roughly the same either way, and runtime performance is unambiguously worse by design; a Cranelift JIT built on the reflected type data can beat Serde in a microbenchmark, but shipping a JIT is not viable for many targets (Apple platform policy, user-visible binary bloat, warmup cost)
- `a-sa25-f011413-c5` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: ~00:10:31–00:11:03
  - Quote: "obviously shipping a jit is not an option for everyone... if you're shipping for Apple platforms, Apple's going to get really mad at you"
  - Paraphrase: a JIT (Cranelift) can close or beat the reflection performance gap, but shipping one isn't viable broadly — rejected outright on Apple platforms, and disliked by users due to unexplained binary size and warm-up cost
- `b-sb24-f011413-c2` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: [08:11]-[10:12]
  - Quote: "it would be nice if Serde was actually able to like do that for us without the annotation, right? But that would mean... you would have to specialize on the T... which is not a thing in Rust stable and should not be a thing in Rust nightly either."
  - Paraphrase: Serde needs an explicit `#[serde(with = ...)]` annotation to serialize `Vec<u8>` as raw bytes instead of a numeric sequence, because Rust has no stable (or nightly-safe) specialization to detect the element type automatically; a reflection-based serializer can inspect the concrete element type at runtime and pick the right encoding without any annotation

## Question `proc-macro-emitted-paths-hidden-deps`

When a proc-macro conditionally emits a call into a crate (here, `tracing::instrument`) behind a feature flag inherited transitively through another crate's feature, should the macro hardcode an unqualified path that silently requires every downstream crate to independently declare that dependency in its own Cargo.toml, or should it use a fully-qualified/re-exported path so the hidden transitive requirement never surfaces as a downstream compile error?

Positions:
- `proc-macro-emitted-paths-hidden-deps--p1`: Fix via feature-gating, not via requiring every downstream crate to declare the dependency
- `proc-macro-emitted-paths-hidden-deps--alt1`: Require every downstream crate to declare the dependency
- `proc-macro-emitted-paths-hidden-deps--alt2`: emit a fully qualified or re-exported path

Claims:
- `a-01-f000701-c1` · Voice: DanielJoyce · Source: https://github.com/leptos-rs/leptos/issues/2156 (`f000701`) · Date: 2024-01-02 · Locator: issue comment, mid-thread
  - Quote: "Fix is to have ssr feature also turn on tracing, or rework the cfg_attribute. Have not tested. ymmv"
  - Paraphrase: Traces the root cause to `leptos_macro`'s `view!` macro unconditionally emitting `tracing::instrument` under `debug_assertions`/`ssr`, and proposes fixing it by having the `ssr` feature also enable `tracing`, or by reworking the macro's `cfg_attr` gating, rather than requiring every downstream crate to add `tracing` itself.

## Question `profile-before-optimizing`

Guide optimization by profiling data or by hypothesis?

Positions:
- `profile-before-optimizing--p1`: Profile first(recommended)
- `profile-before-optimizing--p2`: Let profiling data override the developer's hypothesis about where time is spent, every time

Claims:
- `b-bk02-f000256-c7` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Time Profiling" → Growing our Game of Life Universe; and → Making Time Run Faster
  - Quote: "Always let profiling guide your focus, since time may be spent in places you don't expect it to be."
  - Paraphrase: narrates two cases inside its own tutorial where the expected bottleneck was wrong — the fillStyle canvas setter, not tick(), ate 40% of frame time; and vector allocation, the author's stated hypothesis, turned out to have "negligible cost" — using both to argue profiling must drive optimization, not intuition.
- `a-sB02-f000256-c6` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Time Profiling" — "Making Time Run Faster"
  - Quote: "Looking at the timings, it is clear that my hypothesis is incorrect... Another reminder to always guide our efforts with profiling!"
  - Paraphrase: a stated hypothesis (allocating/freeing a cells vector each tick is the bottleneck) was measured and found false — the cost was actually in computing the next generation — used as the reason to always let profiling guide optimization effort rather than intuition.

## Question `project-decision-speed-vs-inclusion`

Should the Rust project prioritize speed of consensus / shipping over slower, more inclusive decision-making (e.g. long-nightly-gated APIs, stabilization pace)?

Positions:
- `project-decision-speed-vs-inclusion--p1`: Process speed risks exclusion
- `project-decision-speed-vs-inclusion--alt1`: Pick progress and faster consensus over inclusive process

Claims:
- `b-sb19-f005743-c9` · Voice: lake · Source: https://lobste.rs/s/67tqpz (`f005743`) · Date: 2026-06-02 · Locator: comment at 2026-06-02T13:04:24-05:00
  - Quote: "We must learn to recognize when having a consensus is more important than having the right consensus, and in these cases, to pick progress over stagnation."
  - Paraphrase: reads the (quoted, unnamed) source article as calling the community to sideline collaborative/inclusive decision-making in favor of faster "progress"; contrasts with frustration over long-stalled nightly-only APIs and floats wanting a BDFL model

## Question `project-discussions-area`

Should a Rust project keep a GitHub Discussions area for support and design talk, or remove it?

Positions:
- `project-discussions-area--p1`: Removing the discussion area lost knowledge
- `project-discussions-area--alt1`: Remove the discussion area

Claims:
- `b-sT05-f002499-c10` · Voice: yanshay · Source: https://github.com/esp-rs/esp-hal/issues/2884 (`f002499`) · Date: 2026-02-03 · Locator: comment 2026-02-03T10:18:50Z (P.S.)
  - Quote: "no alternative location for such discussion now with the removal of the discussion area"
  - Paraphrase: design talk is forced into an ill-fitting issue after the discussion area's removal
- `b-sT05-f002499-c9` · Voice: Dominaezzz · Source: https://github.com/esp-rs/esp-hal/issues/2884 (`f002499`) · Date: 2026-01-29 · Locator: comment 2026-01-29T15:21:38Z; 2026-02-03T11:59:00Z
  - Quote: "a lot of what I'm explaining now used to exist in a discussion but it's all been deleted now"
  - Paraphrase: explanations (incl. one by "Igor" on bus arbitration) lived in a deleted discussion

## Question `project-priorities-communication`

How should an open-source Rust project's priorities be decided and communicated to its community?

Positions:
- `project-priorities-communication--p1`: Project direction should be communicated through a lightweight, non-authoritative "Goals" system (staffed/unstaffed as a focus signal) rather than a fixed roadmap or the prior ad hoc culture
- `project-priorities-communication--alt1`: A fixed roadmap
- `project-priorities-communication--alt2`: ad hoc "build first, then seek attention"

Claims:
- `b-sR11-f004993-c2` · Voice: Carter Anderson (@cart, Bevy creator and Project Lead) · Source: https://bevy.org/news/bevys-sixth-birthday (`f004993`) · Date: 2026-08-10 · Locator: "Bevy Project Goals #" section
  - Quote: "This is notably not a 'roadmap' ... This is also not authoritative."
  - Paraphrase: the initial rollout felt "dictatorial" because staffed/unstaffed was framed as active/inactive; loosened so any approved Goal can get a Working Group even unstaffed, while staffing still signals leadership focus

## Question `properties-syntax`

Should Rust support "properties" (field-access syntax that silently compiles to a getter/setter method call, as in Python/C#/Swift)?

Positions:
- `properties-syntax--p1`: Reject properties
- `properties-syntax--alt1`: Add properties

Claims:
- `b-sb19-f007207-c2` · Voice: Jimmy Hartzell · Source: https://thecodedmessage.com/posts/rust-features-2 (`f007207`) · Date: 2025-07-21 · Locator: § "Limitations of the Proposal"
  - Quote: "it should be clear that it's doing a field access (cheap and with few potential unseen consequences) rather than a method call (which could do anything including crash, or block your thread on a network request)."
  - Paraphrase: field access should stay visibly cheap and side-effect-free; hiding a method call behind `foo.x` syntax is undesirable, especially in a systems language

## Question `ptx-build-host-vs-multi-arch`

Should a GPU-targeting Rust crate's build script compile device code (PTX) only for the build host's own compute capability, or build/distribute for multiple architectures to stay portable across heterogeneous multi-GPU systems?

Positions:
- `ptx-build-host-vs-multi-arch--p1`: Compile for build host only
- `ptx-build-host-vs-multi-arch--p2`: Needs portable multi arch support

Claims:
- `b-sb08-f002518-c2` · Voice: haricot · Source: https://github.com/huggingface/candle/pull/2704 (`f002518`) · Date: 2025-10-25 · Locator: comment 2025-10-25T10:29:20Z
  - Quote: "the current build script only compiles for the compute capacity active on the build host, which may break portability across heterogeneous multi-GPU systems, it seems."
  - Paraphrase: compiling only for the build host's compute capability may break portability across systems with multiple different GPUs
- `b-sb08-f002518-c1` · Voice: ivarflakstad · Source: https://github.com/huggingface/candle/pull/2704 (`f002518`) · Date: 2025-10-25 · Locator: comment 2025-10-25T10:12:19Z
  - Quote: "The ptx is compiled for your machine via `build.rs` at compile time. It is not one binary distributed to everyone."
  - Paraphrase: PTX is compiled per-machine via build.rs at build time, not distributed as one binary to all users

## Question `public-naming-brevity-vs-clarity`

Should a public name favor brevity or clarity?

Positions:
- `public-naming-brevity-vs-clarity--clarity-over-brevity`: Name for clarity and the literal mechanism
- `public-naming-brevity-vs-clarity--alt1`: Favor brevity or memorability

Claims:
- `b-sR04-f001617-c1` · Voice: osiewicz · Source: https://github.com/zed-industries/zed/pull/13253 (`f001617`) · Date: 2024-06-19 · Locator: PR #13253, comment 2024-06-19T11:34:20Z
  - Quote: "I think it makes sense to spell out `snippets` explicitly in the name to make it a bit easier on the users."
  - Paraphrase: declined a suggestion to shorten the language-server's name to the abbreviation "scls", preferring to spell out "snippets" so users can infer what the name means.
- `b-sR04-f001515-c1` · Voice: dignifiedquire · Source: https://iroh.computer/blog/iroh-0-17-0-everything-is-a-little-better (`f001515`) · Date: 2024-05-24 · Locator: § "The MagicEndpoint is dead, long live the Endpoint"
  - Quote: "Fun names are great, but sometimes they get in the way, and while we all loved MagicEndpoint as a name, it just became too long."
  - Paraphrase: renamed the public type `MagicEndpoint` to plain `Endpoint`, reasoning that a fun/evocative name became a liability once it got too long, even though the team liked it.

## Question `pump-events-timeout-poll`

When an external caller drives a Rust windowing event loop via `pump_events` with a timeout, should any non-negative `Some(duration)` timeout force `ControlFlow::Poll`, or only a zero-duration timeout?

Positions:
- `pump-events-timeout-poll--p1`: Any `Some(duration)` timeout passed to `pump_events` should force `ControlFlow::Poll`
- `pump-events-timeout-poll--p2`: Special-case only `Duration::ZERO` to force `ControlFlow::Poll`; leave other durations to winit's own handling

Claims:
- `a-sR08-f002685-c2` · Voice: tronical (Olivier Goffart, Slint co-founder/maintainer) · Source: https://github.com/slint-ui/slint/issues/7657 (`f002685`) · Date: 2025-02-20 · Locator: GitHub issue comment, 2025-02-20T13:08
  - Quote: "I'll do this workaround only for `Zero`... I'll leave it to the winit implementation to handle that correctly"
  - Paraphrase: reconsidered the broader fix and narrowed the workaround to only the zero-duration case, reasoning it doesn't make sense to return `Wait` when a nonzero duration like `Some(2s)` was explicitly requested — that should be winit's own responsibility to handle correctly
- `a-sR08-f002685-c1` · Voice: sigmaSd · Source: https://github.com/slint-ui/slint/issues/7657 (`f002685`) · Date: 2025-02-20 · Locator: GitHub issue comment, 2025-02-20T10:24
  - Quote: "any duration as long that its Some, should make the controlflow Poll"
  - Paraphrase: proposed broadening the workaround so that every non-nil duration, not just zero, forces Poll

## Question `pure-rust-crypto-stopgap`

When targeting an unusual/constrained platform where the standard C-backed crypto backend won't build, is it acceptable to reach for a pure-Rust crypto implementation as a stopgap, even knowing a hardware-accelerated backend would be the "right" choice for production?

Positions:
- `pure-rust-crypto-stopgap--p1`: Pure-Rust crypto backend as an acceptable stopgap, not the end state
- `pure-rust-crypto-stopgap--alt1`: Use a hardware-accelerated or C-backed backend and wait for platform support

Claims:
- `a-sa11-f004471-c1` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/iroh-on-esp32 (`f004471`) · Date: 2026-03-24 · Locator: § Crypto provider
  - Quote: "The latter would be the right thing to do for a production system, but for now we are going to just do a pure rust version."
  - Paraphrase: explains that both `ring` and `aws-lc-rs` fail on Xtensa because they wrap C code with platform-specific assembly; since rustls providers are pluggable, forks a pure-Rust backend (`rustls-rustcrypto`) down to only the two primitives iroh needs (disabling RSA, disabling certificate verification for the relay connection) to fit the binary-size budget, while stating hardware-accelerated crypto "would be the right thing to do for a production system"

## Question `quantization-speedup-candle`

Does quantization reliably speed up inference in candle, or only for some model architectures?

Positions:
- `quantization-speedup-candle--p1`: Quantization helps memory bound only
- `quantization-speedup-candle--alt1`: Quantization reliably speeds up inference across models

Claims:
- `b-sR01-f000464-c1` · Voice: LaurentMazare · Source: https://github.com/huggingface/candle/issues/1043 (`f000464`) · Date: 2023-10-08 · Locator: issue comment, 2023-10-08T11:39:13Z
  - Quote: "my guess would be that it's much less memory bound in this case and in this case it's pretty hard to outperform the work done by apple on accelerate"
  - Paraphrase: T5's cross-attention involves much larger matmuls than llama/mistral, making it compute- rather than memory-bound on M1/M2; quantization's usual speedup comes from being memory-bound, so it's hard to beat Apple Accelerate (possibly Neural-Engine-backed) here even after tuning min/max-len parameters.

## Question `query-engine-batching-parallelism`

Should a Rust vectorized query engine process rows fully sequentially in large batches (cache-friendly, low interpretation overhead), fully in parallel per-row, or partition data into parallel batched streams?

Positions:
- `query-engine-batching-parallelism--p1`: Partition-based batch execution (vectorized batches within a partition, parallelized across partitions) captures the benefits of both fully-sequential and fully-parallel row processing
- `query-engine-batching-parallelism--alt1`: Fully sequential large batches
- `query-engine-batching-parallelism--alt2`: fully parallel per-row processing

Claims:
- `a-sR08-f003580-c1` · Voice: Yevgen Safronov, Nikita Lapkov, Jérôme Schneider (Cloudflare, R2 SQL) · Source: https://blog.cloudflare.com/r2-sql-deep-dive (`f003580`) · Date: 2025-09-25 · Locator: "Apache DataFusion" section
  - Quote: "DataFusion's architecture allows us to achieve a balance on this scale, reaping benefits from both ends."
  - Paraphrase: contrasted a fully-sequential "tight loop" (cache-friendly, low interpretation overhead) against fully-parallel per-row processing (better core utilization), and endorsed DataFusion's partition model as achieving both at once

## Question `quic-framing-one-stream-vs-per-message`

On a QUIC stream, should a protocol send several length-prefixed messages over one stream, or one message per stream written with `write_all` and read to the end before closing?

Positions:
- `quic-framing-one-stream-vs-per-message--p1`: Length prefixed framing on one stream
- `quic-framing-one-stream-vs-per-message--alt1`: One message per stream, written with `write_all` and read to the end

Claims:
- `a-sT08-f003375-c1` · Voice: n0 (post by ramfox, matheus23, b5) · Source: https://iroh.computer/blog/message-framing-tutorial (`f003375`) · Date: 2025-08-12 · Locator: § Intro and § Framed Messages, paragraphs on `write_all`/`read_all`
  - Quote: "This is fine while you are getting familiar, but when you go to write your protocols you will want something more sophisticated."
  - Paraphrase: writing one chunk with `write_all`, reading it all, then closing the stream is fine while learning, but real protocols should send multiple logical messages per stream, each prefixed by its length, so the protocol is designed as messages rather than bytes and variable-length messages are handled

## Question `rate-limiter-algorithm`

for a rate limiter, should you use a fixed-window counter, a token bucket, or a sliding window?

Positions:
- `rate-limiter-algorithm--p1`: Use a fixed-window counter for the rate limiter, accepting its known boundary-burst weakness, rather than a token bucket or sliding window
- `rate-limiter-algorithm--alt1`: A token bucket
- `rate-limiter-algorithm--alt2`: a sliding window

Claims:
- `b-sb22-f008906-c5` · Voice: Luciano Mammino · Source: https://loige.co/writing-middlewares-for-rust-lambda-functions (`f008906`) · Date: 2026-05-03 · Locator: section "Fixed window vs token bucket vs sliding window: what we are giving up"
  - Quote: "This is sometimes called the window boundary burst, and it is the textbook reason people move on from fixed windows in production-grade rate limiters."
  - Paraphrase: a motivated client can double its effective rate by firing requests at the edges of two adjacent fixed windows; token bucket and sliding window both eliminate that edge but cost an extra DynamoDB round trip (read-modify-write, or two reads) versus one atomic `ADD`; the post sticks with the fixed window "mostly because it keeps the DynamoDB schema minimal and easy to follow," leaving the algorithm swap as a follow-up

## Question `reactive-keyed-child-notification`

When a reactive container's parent field is written as a whole (replaced or patched), should the reactivity system notify all of its keyed-child subscriptions by default (accepting some unnecessary re-notifications), or should notification require writing through the specific keyed accessor (precise, but silently misses updates if the user writes the parent instead)?

Positions:
- `reactive-keyed-child-notification--p1`: Default notify all children favor no false negatives
- `reactive-keyed-child-notification--alt1`: Notify only through the specific keyed accessor

Claims:
- `b-sb13-f003963-c1` · Voice: gbj · Source: https://github.com/leptos-rs/leptos/pull/4473 (`f003963`) · Date: 2026-02-06 · Locator: comment 2026-02-06T17:19:48Z
  - Quote: "I think your intuition is correct that \"false negatives\" (broken reactivity) here are worse than \"false positives\" (notifications that are technically unnecessary). I think going ahead with my Option 1 ... is probably the way to go."
  - Paraphrase: concludes that broken reactivity (false negatives) is worse than unnecessary notifications (false positives), so the library should track the parent path by default and notify all keyed children on a parent write
- `b-sb13-f003963-c2` · Voice: TiemenSch · Source: https://github.com/leptos-rs/leptos/pull/4473 (`f003963`) · Date: 2026-02-04 · Locator: comment 2026-02-04T13:10:55Z
  - Quote: "I would expect that fully setting a new value is allowed to trigger all children and it would be OK to have the user patch/update specific fields instead to avoid too many false positives."
  - Paraphrase: independently reasons that fully replacing a value should be allowed to trigger all children, leaving precise-but-manual updates as an opt-in path rather than the default

## Question `readability-vs-manual-optimization`

When a compiler backend (LLVM/Cranelift) could optimize an eager computation away, should code still be written in the more efficient/lazy form?

Positions:
- `readability-vs-manual-optimization--p1`: Readability over manual optimization when backend cleans up
- `readability-vs-manual-optimization--alt1`: Write the manually optimized (lazy) form anyway

Claims:
- `b-sb05-f001582-c2` · Voice: fitzgen · Source: https://github.com/bytecodealliance/wasmtime/pull/8763 (`f001582`) · Date: 2024-06-11 · Locator: comment 2024-06-11T16:35:49Z
  - Quote: "I think it probably doesn't matter much either way in this case, since there isn't anything here that could prevent LLVM from cleaning this up itself"
  - Paraphrase: eager vs. lazy default computation doesn't matter much here since LLVM can likely optimize it away, but the change is worth making for reader clarity

## Question `reduction-accumulation-precision`

Should numeric reductions in a Rust ML kernel (e.g. softmax) accumulate in a higher-precision type than the input/output dtype?

Positions:
- `reduction-accumulation-precision--p1`: Accumulate in float for precision
- `reduction-accumulation-precision--alt1`: Accumulate in the input/output dtype

Claims:
- `a-sR04-f001096-c1` · Voice: ivarflakstad · Source: https://github.com/huggingface/candle/pull/1819 (`f001096`) · Date: 2025-01-13 · Locator: comment "Should probably accumulate with float in softmax to preserve precision. Shouldn't affect performance at all."
  - Quote: "Should probably accumulate with float in softmax to preserve precision."
  - Paraphrase: numeric reductions should accumulate in float32 even when the surrounding tensors are lower precision, to avoid precision loss, at negligible performance cost

## Question `reflection-security-risk`

Does giving Rust code reflection-like or dynamic-loading capability introduce a security/soundness risk category that Rust's design has otherwise avoided?

Positions:
- `reflection-security-risk--p1`: Universally implemented reflection is suspicious
- `reflection-security-risk--p2`: Rust lacks reflection and that closes off a footgun class

Claims:
- `a-sa28-f012469-c7` · Voice: durka42 — track record uncertain in this source (recurring #rust-internals/IRC participant, no confirmed authored crate/book found here); logged with this caveat · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2015-12-01 · Locator: post by @XMPPwocky dated 2015-12-01T00:17:43Z, quoting an IRC/forum exchange about the (now-deprecated) `Reflect` marker trait
  - Quote: "it's like tapping the Marauder's Map with your wand and saying 'I solemnly swear I am up to no good'"
  - Paraphrase: reacts to the `Reflect` trait (auto-implemented for all types) as inherently ominous
- `a-sa28-f012469-c8` · Voice: vitalyd — track record uncertain in this source (recurring, substantive technical poster; no confirmed authored crate/book found here); logged with this caveat · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2017-09-12 · Locator: post by @vitalyd dated 2017-09-12T12:52:15Z
  - Quote: "Rust doesn't have dynamic class loading and reflection, but someone could build a serde serializable type to do custom remote command/process execution. It would be deliberate and not some oversight though, but still possible given enough will."
  - Paraphrase: distinguishes a Java/Struts-style deserialization RCE footgun (enabled by reflection + dynamic class loading) from Rust, where the same outcome would require someone to deliberately build a serde-serializable type to do it — not an accidental byproduct of a language feature

## f009123 — [Pre-RFC] Scoped `impl Trait for Type` (2023-11-26, en)

### Questions

- Q: Should scoped trait implementations be nameable, or must they stay anonymous?
  concepts: trait coherence; orphan rules; scoped impls; trait implementation naming; domains_live: core; positions_seen: anonymous-impls-required-for-coherence; named-impls-for-clarity

### Claims

- voice: Tamschi | position: anonymous-impls-required-for-coherence | date: 2023-12-05 | locator: reply to scottmcm/Nadrieril, 2023-12-05T20:39:46.548Z | paraphrase: Opposes naming scoped implementations; anonymity keeps coherence checking simple within one scope, lets the module double as an error-message name, and avoids new breaking-change rules that naming would introduce when an implementation is later broadened. | quote: "Regarding proper-naming implementations: I'm very strongly opposed to it, since I think it is squarely detrimental here, mainly in terms of clarity but also syntactically and for ease of use." | practiced_evidence: none (author of the pre-RFC and, later, RFC 3634)
- voice: scottmcm | position: named-impls-for-clarity | date: 2023-11-29 | locator: reply, 2023-11-29T03:31:09.374Z | paraphrase: Wants names for non-global impls so two implementations of the same trait/type can coexist in one module, and so compiler error messages can use a normal path instead of "the impl from this module". | quote: "I feel like they wanted names, and with names you even define two impls ... I think it would be nice to give normal paths to named things in those errors." | practiced_evidence: none
- voice: Nadrieril | position: named-impls-for-clarity | date: 2023-12-05 | locator: reply, 2023-12-05T13:43:01.887Z | paraphrase: Suggests an explicit naming mechanism so the implicit scoped-impl behavior desugars from something writable, making the proposal easier to explain even if users rarely write the explicit form. | quote: "I would suggest that you provide an explicit mechanism to specify a type along with explicitly chosen impls." | practiced_evidence: none

---

## f009196 — {Instant,SystemTime}::{MIN,MAX} (2024-08-15, en)

### Questions

- Q: Should `Instant` expose fixed extremal values (MIN/MAX), given it has no fixed reference epoch?
  concepts: time APIs; Instant; SystemTime; monotonic clocks; saturating arithmetic; domains_live: core; positions_seen: oppose-instant-extrema-fraught; instant-extrema-fraught-prefer-saturating-ops; support-instant-bound-for-saturating-arithmetic
- Q: When a scheduled timer/interval's next wake time would overflow the maximum representable `Instant`, should the runtime panic or silently never become ready again?
  concepts: time APIs; panics vs graceful degradation; async runtimes (Tokio Interval); domains_live: distributed; cloud-workers; core; positions_seen: panic-on-overflow; never-ready-without-panic

### Claims

- voice: the8472 | position: oppose-instant-extrema-fraught | date: 2024-08-15 | locator: reply, 2024-08-15T23:11:10.007Z | paraphrase: SystemTime::MIN/MAX might be reasonable, but Instant values aren't portable and aren't stable across reboots, so exposing extrema is more hazardous than SystemTime's case. | quote: "For SystemTime this might be reasonable to have, but the values wouldn't be portable. I think Instant would be more hazardous..." | practiced_evidence: none
- voice: farnz | position: oppose-instant-extrema-fraught | date: 2024-08-16 | locator: reply, 2024-08-16T08:43:34.961Z | paraphrase: Instant's current API contract does not guarantee a fixed reference time; a conforming implementation could start/stop its reference timer dynamically, so a MIN value wouldn't reliably denote a stable point in time. | quote: "This assumes that there is a fixed reference time for Instant, which isn't technically required at the moment." | practiced_evidence: none
- voice: burntsushi | position: instant-extrema-fraught-prefer-saturating-ops | date: 2024-08-16 | locator: reply, 2024-08-16T13:04:57.183Z | paraphrase: SystemTime::MIN/MAX seem reasonable; Instant::MIN/MAX seem fraught for the reasons already raised, so proposes adding saturating arithmetic methods directly on Instant instead of exposing its extrema. | quote: "SystemTime::MIN and SystemTime::MAX seem reasonable to me... Instant::MIN and Instant::MAX seem fraught, for reasons already discussed." | practiced_evidence: none
- voice: kevincox | position: support-instant-bound-for-saturating-arithmetic | date: 2024-08-16 | locator: reply, 2024-08-16T13:23:59.223Z | paraphrase: Wants an Instant minimum/maximum (or equivalent) to support saturating arithmetic in a token-bucket rate limiter, where moving a timestamp below the representable minimum should saturate rather than panic. | quote: "For my use case it is preferable to saturate." | practiced_evidence: rl_core crate (own crate, named but not linked in-thread)
- voice: kevincox | position: panic-on-overflow | date: 2024-08-17 | locator: reply, 2024-08-17T19:19:10.352Z | paraphrase: Argues the best behaviour is to keep a sleeping future alive but never fire it early, panicking only in the extremely unlikely case that Instant::now itself reaches Instant::MAX, since no reasonable behaviour exists past that point. | quote: "Panic if Instant::now reaches Instant::MAX... you never run a timer too early but you also don't panic upfront." | practiced_evidence: none
- voice: bjorn3 | position: never-ready-without-panic | date: 2024-08-17 | locator: reply, 2024-08-17T18:40:14.074Z | paraphrase: Criticizes Tokio's existing `far_future()` hack (used in `Interval::poll_tick`) as unnecessary; when a period is too large or the clock is nearly exhausted, the correct behaviour is to never register the future as ready again, not to wait based on a MAX-derived time that undershoots. | quote: "The only options are to panic or have the future never be ready ever again." | practiced_evidence: tokio-rs/tokio source, `far_future()` in tokio/src/time/instant.rs (cited in-thread)

---

## f009292 — Pre-RFC: #[derive] support for arithmetic traits (Add, Sub, Mul, Div) on structs (2025-09-02, en)

### Questions

- Q: Should std provide `#[derive]` support for arithmetic operator traits (Add/Sub/Mul/Div) on structs, applying field-wise semantics automatically?
  concepts: derive macros; operator overloading; newtypes; affine spaces; std-vs-ecosystem scope; domains_live: core; positions_seen: support-fieldwise-derive; oppose-semantics-too-ambiguous; oppose-prefer-delegation-mechanism; ecosystem-crates-suffice
- Q: How should Rust reduce boilerplate for simple trait implementations — new dedicated impl syntax, compiler-inferred associated types, or ecosystem derive-macro crates?
  concepts: trait implementation ergonomics; associated types; macros; derive_more; domains_live: core; positions_seen: new-impl-shorthand-syntax; infer-associated-types; ecosystem-crates-suffice

### Claims

- voice: vangata-ve | position: support-fieldwise-derive | date: 2025-09-02 | locator: OP, 2025-09-02T17:06:42.006Z | paraphrase: Manually implementing Add/Sub/Mul/Div for structs where field-wise operation is the obviously sensible behaviour is needless busywork; std should support deriving them the way it does Clone/Debug/Copy. | quote: "This is pointless busywork when the only sensible behavior is to perform the operation field by field." | practiced_evidence: none
- voice: 2e71828 | position: oppose-semantics-too-ambiguous | date: 2025-09-02 | locator: reply, 2025-09-02T17:47:25.304Z | paraphrase: Doubts unconstrained field-wise derive is broadly useful, since most wrapper structs that need arithmetic (complex numbers, quaternions, matrices) have their own non-field-wise rules. | quote: "My main concern is whether unconstrained field-wise projection of these operators is really all that common." | practiced_evidence: none
- voice: jdahlstrom | position: oppose-semantics-too-ambiguous | date: 2025-09-02 | locator: reply, 2025-09-02T19:56:12.974Z | paraphrase: Invokes affine-space math (points vs. vectors/translations) to argue field-wise addition is often meaningless, e.g. adding two geographic coordinates, so a naive derive would default to semantically wrong behaviour. | quote: "Addition and scalar multiplication make sense for vectors, but for points they are meaningless in general." | practiced_evidence: none
- voice: Vorpal | position: oppose-semantics-too-ambiguous | date: 2025-09-05 | locator: reply, 2025-09-05T08:06:03.300Z | paraphrase: Even for simple newtypes there is no single correct semantics (e.g. whether Radians/Degrees arithmetic should wrap modulo 2π/360), unlike Clone or Debug where the standard derive is almost always right. | quote: "It is not obvious what the derives for arithmetic operators should do. There isn't a single right answer." | practiced_evidence: none
- voice: kornel | position: oppose-prefer-delegation-mechanism | date: 2025-09-02 | locator: reply, 2025-09-02T20:24:36.828Z | paraphrase: A basic field-wise arithmetic derive can only encode one relationship between fields (e.g. a Point), so it doesn't generalize to matrices, quaternions or complex numbers; a delegation syntax or generalized derive-construction macro would serve better. | quote: "This may be better solved by delegation syntax or generalised macros for constructing derives." | practiced_evidence: none
- voice: porky11 | position: ecosystem-crates-suffice | date: 2026-01-16 | locator: reply, 2026-01-16T20:01:40.626Z | paraphrase: derive_more already covers this well; the core language/std should stay minimal and leave most conveniences to libraries, which is the point of having a package manager. | quote: "No need to have it in the core fo the language. That's kind of the point of the Rust package manager, that the core language includes the important things while most things are outsourced to libraries." | practiced_evidence: none
- voice: zackw | position: new-impl-shorthand-syntax | date: 2025-09-08 | locator: reply, 2025-09-08T15:59:48.016Z | paraphrase: Proposes syntactic sugar such as `impl Display (self, f) for Type { ... }` for traits with exactly one required method, removing an indentation level and the need to look up the method's exact signature, beyond what derive alone offers. | quote: "I wonder if we could come up with a generalization of this macro that would be suitable as official syntactic sugar." | practiced_evidence: none (references an unpublished personal macro)
- voice: scottmcm | position: infer-associated-types | date: 2025-09-08 | locator: reply, 2025-09-08T23:27:35.279Z | paraphrase: Rather than new impl syntax, wants the compiler to infer associated types (e.g. `Iterator::Item`) from the method body, which would simplify implementing Add, Sub, IntoIterator and Deref without adding new surface syntax. | quote: "there's really no need... for me to have to write the type Item = i32; because it's the only possible thing given that next." | practiced_evidence: none

---

## f009316 — Idea: trait methods with un-overridable implementations (2026-01-07, en)

### Questions

- Q: Should Rust add `final`/non-overridable trait methods, and if so, must such methods still participate in dynamic dispatch (vtables) for soundness?
  concepts: trait objects; dyn dispatch; vtables; sealed traits; specialization; TypeId; domains_live: core; positions_seen: support-final-methods; skeptical-limited-value-vs-free-functions; final-methods-need-vtable-for-soundness

### Claims

- voice: newpavlov | position: support-final-methods | date: 2026-01-07 | locator: OP, 2026-01-07T21:26:16.248Z | paraphrase: Proposes a `#[non_overridable]` attribute for trait extension methods whose override could cause correctness bugs, potentially excluding such methods from vtables to shrink them. | quote: "I think something like #[non_overridable] could be a useful addition to the language." | practiced_evidence: none
- voice: josh | position: support-final-methods | date: 2024-08-13 | locator: linked RFC (joshtriplett/rfcs "final"), cited 2026-01-07T21:42:35.707Z | paraphrase: Points to an already-drafted RFC ("Trait method impl restrictions", using the reserved `final` keyword) letting any trait forbid overriding specific methods or associated functions. | quote: "Support restricting implementation of individual methods within traits, using the already reserved `final` keyword." | practiced_evidence: rust-lang/rust tracking issue #131179 (linked)
- voice: afetisov | position: skeptical-limited-value-vs-free-functions | date: 2026-01-08 | locator: reply, 2026-01-08T14:37:33.435Z | paraphrase: Doubts final methods offer real benefit beyond "minor sugar", since any trait bound or call used inside a final method can just as well be replicated with a corresponding free function. | quote: "Surely there are other benefits, besides minor sugar, for a new feature? Personally I can't think of any." | practiced_evidence: none
- voice: SkiFire13 | position: final-methods-need-vtable-for-soundness | date: 2026-01-08 | locator: reply, 2026-01-08T21:16:18.959Z | paraphrase: Constructs a concrete example where a final method called through `dyn Trait` observably differs from an equivalent generic free function (via `TypeId::of::<Self>` vs. the erased type), showing final methods cannot simply desugar to free functions and must remain reachable via the vtable. | quote: "The .baz() method prints () because it's being monomorphized for () and inserted into the vtable, while the baz function call prints dyn playground::Foo..." | practiced_evidence: Rust Playground link demonstrating the divergent output (cited in-thread)
- voice: eggyal | position: final-methods-need-vtable-for-soundness | date: 2026-03-12 | locator: linked rust-lang/rust issue (opened 2026-03-10), cited 2026-03-12T06:00:48.747Z | paraphrase: Filed an I-unsound bug showing nightly's experimental `final` associated functions behave inconsistently with `dyn Trait` dispatch (an `assert_ne!` on `TypeId::of` via `dyn Trait` fails), confirming the vtable/soundness concern is a live, unresolved implementation problem rather than a purely theoretical one. | quote: "`final` methods should work the same as without it (if it works without it)" | practiced_evidence: rust-lang/rust issue tagged I-unsound, C-bug (linked)

---

## f009343 — Code compiles on playground but fails when passed via stdin to rustc (2026-06-11, en)

### Questions

- Q: Should rustc warn (or emit a note) whenever it is invoked without an explicit `--edition`, given how much edition-dependent behaviour has accumulated?
  concepts: Rust editions; rustc CLI; tooling ergonomics; cargo/rustc coordination; domains_live: core; desktop-cli-ui; positions_seen: support-warn-on-missing-edition
- Q: Should crates and their build scripts (build probes like autocfg) be free to auto-detect and use nightly-only compiler/library features by default, or must nightly-feature usage always require the final binary author's explicit opt-in?
  concepts: nightly features; build scripts / build probes; cargo unstable flags (-Zallow-features); stability guarantees; autocfg; domains_live: core; desktop-cli-ui; positions_seen: nightly-features-must-be-explicit-opt-in; build-probes-should-default-to-detecting-and-using-nightly-features

### Claims

- voice: kpreid | position: support-warn-on-missing-edition | date: 2026-06-11 | locator: reply, 2026-06-11T18:43:32.982Z | paraphrase: Given how significant edition differences have become, rustc should warn whenever invoked with no `--edition`, since almost no one today intends the 2015 default; notes a prior attempt stalled because many UI test suites set no edition and would gain new warnings. | quote: "rustc ought to warn whenever it is invoked without an --edition, because almost nobody writing a rustc invocation today should be using the 2015 edition." | practiced_evidence: none
- voice: ekuber | position: support-warn-on-missing-edition | date: 2026-06-21 | locator: linked PR rust-lang/rust#158102 (opened 2026-06-18), own reply 2026-06-21T22:53:55.156Z | paraphrase: Implemented the warning as an undismissable "note" rather than a lint specifically so `forbid`/`deny(warnings)` setups used by build probes aren't broken by it. | quote: "I implemented this as an undismisable note, which could also be a warning... The only people affected would be those explicitly comparing textual compiler output in scripts." | practiced_evidence: rust-lang/rust PR #158102 (linked)
- voice: RalfJung | position: nightly-features-must-be-explicit-opt-in | date: 2026-06-30 | locator: reply, 2026-06-30T12:20:20.661Z | paraphrase: Argues nearly all build probes are subtly broken because cargo doesn't give them enough information, and more fundamentally that nightly features should be opt-in, not opt-out; libraries auto-detecting and using them by default harms nightly users and compiler maintainers debugging regressions. | quote: "nightly features should be opt-in, not opt-out. That's how the entire Rust nightly feature system is designed." | practiced_evidence: none
- voice: epage | position: nightly-features-must-be-explicit-opt-in | date: 2026-06-29 | locator: reply, 2026-06-29T17:46:02.300Z | paraphrase: States the Rust Project's general principle that unstable features should only affect those who opted in, and that libraries auto-enabling nightly features runs counter to that principle. | quote: "there is a general principle within the Rust Project that unstable features only impact those who have opted in... Libraries auto-enabling features are running counter to that principle." | practiced_evidence: none
- voice: Nemo157 | position: nightly-features-must-be-explicit-opt-in | date: 2026-06-29 | locator: reply, 2026-06-29T15:30:35.384Z | paraphrase: Wants to use nightly for unrelated ergonomic toolchain features while explicitly not consenting to dependencies silently using other unstable library or compiler features just because a nightly compiler was detected. | quote: "dependencies see that I am using a nightly compiler and attempt to use other unstable library or compiler features that I don't want them to." | practiced_evidence: none
- voice: kpreid | position: nightly-features-must-be-explicit-opt-in | date: 2026-06-29 | locator: reply, 2026-06-29T15:39:25.162Z | paraphrase: When switching to nightly for unrelated reasons (debug flags, a newer compiler), does not want dependencies to implicitly change behaviour by using unstable features; would want any such blanket opt-in to be a separate, explicit flag, never implied by nightly usage alone. | quote: "I don't want my project's dependencies to also implicitly change to making use of unstable features." | practiced_evidence: none
- voice: MusicalNinjaDad | position: build-probes-should-default-to-detecting-and-using-nightly-features | date: 2026-06-29 | locator: reply, 2026-06-29T15:04:10.084Z | paraphrase: As a "Group B" ergonomics-motivated developer, argues build probes defaulting to detect-and-use available nightly features is preferable to requiring manual opt-in flags, while acknowledging safety-critical ("Group A") users need a documented way to fully opt out. | quote: "Personally, I prefer a crate that documents clearly if they auto-detect & use nightly features to one that makes me go through that hassle, and choose accordingly." | practiced_evidence: MusicalNinjaDad/rust, `ninja-build_rs/src/nightly.rs` (linked in-thread)

---

## f009632 — Next Steps on the Rust Trademark Policy (2024-11-06, en)

### Nothing new

`nothing new`: this is a Leadership Council announcement soliciting community feedback on a draft trademark policy; the post states process history and next steps but no Voice takes or argues a position in the text itself, so no Claim can be drawn from it.

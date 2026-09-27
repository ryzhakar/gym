For each source: where do competent Rust practitioners disagree?

Team a · batch 1 · third pass · slice T03 · bundle samples/bundles/b1-team-a-T03.txt, cut at 150,000 chars; read in full from cache key 0aa26ff7823a (165 posts, no new fetch).

## f001094 — SE-0427: Noncopyable Generics (2024-03-08, en)

### Nothing new
It is a Swift Evolution review of Swift's `~Copyable` generics, and every contested point in it is a Swift language-design decision: the `~` spelling versus `?Copyable`, `!Copyable` or `-Copyable`; whether extensions infer `Copyable`; whether `Copyable & ~Copyable` is an error or a warning; and whether a `~Copyable` type can regain `Copyable` in an extension. No Voice shows a Rust connection in the source. Under rule 9 its Positions are therefore not Claims, and they are not mapped onto Rust Questions.

Disclosed, not logged: Rust appears only as outside reference, never as self-reported use or a Rust decision. The references are @jrose 2024-03-10T18:50:47Z ("Rust's route of penalizing var") and 2024-03-16T19:21:20Z (Rust macros), @ben-cohen 2024-03-15T16:05:52Z ("familiar to people used to writing Rust"), and @brendon 2024-03-20T17:39:56Z ("aping Rust's syntax and using ?Copyable").

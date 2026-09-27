## f011092 — Building the next generation of compute primitives in Rust (talk by Luca Casonato, Deno) (2024-02-13, en)

Note: the bundle's transcript text is visibly cut mid-sentence partway through (around the ~26:50 mark, discussing third-party cloud SDKs); a WebFetch re-fetch of the YouTube URL returned only page chrome, no additional caption text, so the remainder of the talk is unreachable and not reconstructed from memory. Extraction below covers only the available ~00:00-26:50 portion.

### Questions

- Q: Should a secure multi-tenant runtime that executes untrusted user code (e.g. a serverless JavaScript isolate hypervisor) be built in a language like Rust rather than a garbage-collected language like Go?
  concepts: memory safety without a garbage collector; multi-tenant isolation/sandboxing; FFI/embedding a C++ engine (V8); async runtime scheduling; domains_live: cloud-workers; distributed; core; positions_seen: rust-for-reliability-and-explicit-performance

### Claims

- voice: Luca Casonato | position: rust-for-reliability-and-explicit-performance | date: 2024-02-13 | locator: transcript ~00:01:46-00:10:30 (talk, timestamps approximate from auto-captions) | paraphrase: Describes Deno's own history of first trying Go for its multi-tenant sandboxed runtime, and rejecting it because it lacked the reliability, strictness, customizability and performance needed to safely execute untrusted code for many tenants; chose Rust (with some C++ for the embedded V8 engine) instead, citing exhaustive Result/Option-based error handling, transparent/explicit allocation cost (no hidden allocations without an explicit `.clone()`), no conflict between a host garbage collector and V8's own GC in the same process, and easy C++ interop needed to embed V8 safely via `rusty_v8`-style bindings. | quote: "[Go] does not have the same reliability or strictness or customizability or performance that languages like rust or even C++ for that matter do" | practiced_evidence: Deno runtime, 500,000+ lines of Rust across the organization's GitHub (~70-80% open source), safe Rust bindings to V8, and crates the speaker's team maintains (rust-url, wgpu contribution) — practiced, per the talk's own account of Deno's codebase

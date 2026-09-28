# Classify a response

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `Status` below 200 is `"info"`, 200 to 299 `"success"`, 300 to 399 `"moved"`, 400 to 499 `"client error"`, 500 and above `"server error"`. `Timeout` is `"retry"`. `Redirect` is `"follow"`.
- Keep `Response` and the signature of `class` as written.
- The match keeps at most seven arms.
- No `panic!`, `unreachable!`, `todo!` or `unimplemented!`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.

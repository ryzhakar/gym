# b2-life · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- The body of `key_of` is correct. The edit site is its signature.
- `key_of` keeps returning a borrowed `&str`, not an owned `String`.
- The test file is locked.

Cap: 2.5 minutes. Compiler and `rustc --explain` allowed. Nothing else.

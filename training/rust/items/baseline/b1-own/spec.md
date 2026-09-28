# b1-own · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `keep_long` must return the total number of words and the words longer than `min` bytes, in order.
- The kept strings must be the original strings, moved, not copies. A held-out test checks their heap addresses.
- Do not change the signature of `keep_long`. The test file is locked.

Cap: 2.5 minutes. Compiler and `rustc --explain` allowed. Nothing else.

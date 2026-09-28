# Find the brightest colour channel

Edit: src/lib.rs

- `brightest` returns the largest channel value. Each channel is hexadecimal text that fits in a `u8`, such as `"ff"` or `"0a"`.
- The current code is right for good input. Make it return an error instead of panicking.
- No channels: `Empty`.
- A channel that is not a hexadecimal `u8`: `BadChannel`, with the index of the first such channel, counting from 0.
- Keep `ChannelError` and the signature of `brightest` as written.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.

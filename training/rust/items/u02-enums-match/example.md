# u02 worked example · enums and match

Four subgoals. Every problem in this unit is solved by working through them in this order.

1. **Name the cases.** One variant per case, and each variant carries only the data its case has.
2. **Cover every case.** One arm per variant. When an arm is missing, the compiler's non-exhaustive error names it. A `_` arm is safe only where every variant added later should get the same answer.
3. **Order arms from specific to general.** The first arm that matches wins. Literal values, ranges and guards come before the plain binding of the same variant.
4. **Bind what the arm uses.** Destructure the fields the arm needs, use `@` to keep a value that was tested against a range, and use `..` for the rest.

## The problem

A window receives input events: a key press (a `char`), a mouse click at (x, y), a scroll by some amount, and close. Two functions are needed:

- `describe(e) -> String`:
  - `"quit key"` for `q`, `"key <c>"` for any other key
  - `"corner click"` at (0, 0), `"diagonal click <x>"` when x equals y, `"click <x>,<y>"` otherwise
  - `"no scroll"` for 0, `"small scroll <d>"` for 1 to 3, `"scroll <d>"` otherwise
  - `"close"`
- `click_pos(e) -> Option<(i32, i32)>`: where a click happened; `None` for every other event.

## Subgoal 1 · Name the cases

The problem statement lists four cases, and each has its own data: a `char`, two coordinates, an amount, and nothing at all.

```rust
pub enum Event {
    Key(char),
    Click { x: i32, y: i32 },
    Scroll(i32),
    Close,
}
```

The alternative is one struct with a kind tag and a field for every case's data, such as `kind: u8, ch: char, x: i32, y: i32, amount: i32`. That struct can hold a close event that carries a character, and nothing stops code from reading `x` off a key press. With the enum, a `Close` carries nothing and a `Key` has no `x` to read.

## Subgoal 2 · Cover every case

A first version with the close arm forgotten:

```rust
pub fn describe(e: Event) -> String {
    match e {
        Event::Key(c) => format!("key {c}"),
        Event::Click { x, y } => format!("click {x},{y}"),
        Event::Scroll(d) => format!("scroll {d}"),
    }
}
```

```
error[E0004]: non-exhaustive patterns: `Event::Close` not covered
9 |     match e {
  |           ^ pattern `Event::Close` not covered
```

The compiler lists the missing variant. The fix is an arm that names it, `Event::Close => "close".to_string()`. The compiler's help offers a `todo!()` arm, which compiles and then panics when the case arrives.

`click_pos` has one interesting variant and three dull ones. Naming the dull ones keeps the check alive: if a fifth variant is added later, this match stops compiling instead of quietly answering `None`.

```rust
pub fn click_pos(e: Event) -> Option<(i32, i32)> {
    match e {
        Event::Click { x, y } => Some((x, y)),
        Event::Key(_) | Event::Scroll(_) | Event::Close => None,
    }
}
```

The `_` inside `Key(_)` ignores a field, not a variant.

## Subgoal 3 · Order arms from specific to general

`Key(c)` matches every key, `q` included. Put before `Key('q')`, it makes the `q` arm dead:

```
warning: unreachable pattern
18 |         Event::Key(c) => format!("key {c}"),
   |         ------------- matches all the relevant values
19 |         Event::Key('q') => "quit key".to_string(),
   |         ^^^^^^^^^^^^^^^ no value can reach this
```

For clicks there are three arms, from narrowest to widest: the one point (0, 0), then any point where x equals y (a guard), then every click. For scrolls: the value 0, then the range 1 to 3, then everything else.

## Subgoal 4 · Bind what the arm uses

```rust
pub fn describe(e: Event) -> String {
    match e {
        Event::Key('q') => "quit key".to_string(),
        Event::Key(c) => format!("key {c}"),
        Event::Click { x: 0, y: 0 } => "corner click".to_string(),
        Event::Click { x, y } if x == y => format!("diagonal click {x}"),
        Event::Click { x, y } => format!("click {x},{y}"),
        Event::Scroll(0) => "no scroll".to_string(),
        Event::Scroll(d @ 1..=3) => format!("small scroll {d}"),
        Event::Scroll(d) => format!("scroll {d}"),
        Event::Close => "close".to_string(),
    }
}
```

- `Click { x: 0, y: 0 }` tests both fields and binds nothing.
- `Click { x, y } if x == y` binds both fields, and the guard reads them. The diagonal arm could print `y` in place of `x`: they are equal there.
- `Scroll(d @ 1..=3)` tests the amount against a range and keeps it as `d`.
- A guard does not count toward exhaustiveness. If the final `Click { x, y }` arm had a guard of its own, E0004 would come back.

`cargo test`: green.

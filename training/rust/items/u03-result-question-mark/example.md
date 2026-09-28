# u03 worked example · Result and `?`

Four subgoals. Every problem in this unit is solved by working through them in this order.

1. **List the fallible steps.** Every call that returns a `Result` or an `Option`, with its error type, plus every check the function makes itself.
2. **Pick the function's error type.** One enum with a variant for each failure the caller has to tell apart.
3. **Convert each failure into that type.** `map_err` on a `Result`, `ok_or` on an `Option`, an early `return Err(…)` for a check of your own.
4. **Propagate with `?` and return `Ok` at the end.** No `unwrap`, `expect` or `panic!` on anything the input controls.

## The problem

Parse `"HH:MM"` into minutes since midnight: `"07:30"` gives `450`. The caller needs to know why a bad input is bad: no colon, a bad hour, a bad minute, or numbers out of range (hour 24 or more, minute 60 or more).

## Subgoal 1 · List the fallible steps

| step | call | returns |
|---|---|---|
| split at `:` | `text.split_once(':')` | `Option<(&str, &str)>` |
| hour | `hour.parse::<u32>()` | `Result<u32, ParseIntError>` |
| minute | `minute.parse::<u32>()` | `Result<u32, ParseIntError>` |
| range | none: the function's own check | — |

Two error types come out of std, `None` and `ParseIntError`, and the range check adds a failure std knows nothing about.

## Subgoal 2 · Pick the function's error type

Four failures the caller should tell apart, so four variants. Both parse steps produce the same std error type, which is exactly why each gets a variant of its own: `ParseIntError` alone would not say which number was bad.

```rust
use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum TimeError {
    NoColon,
    BadHour(ParseIntError),
    BadMinute(ParseIntError),
    OutOfRange,
}
```

## Subgoal 3 · Convert each failure into that type

`?` on a value whose error is not already `TimeError` fails to compile. On the `Option`:

```
error[E0277]: the `?` operator can only be used on `Result`s, not `Option`s, in a function that returns `Result`
12 |     let (hour, minute) = text.split_once(':')?;
   |                                              ^ use `.ok_or(...)?` to provide an error compatible with `Result<u32, TimeError>`
```

On the parse:

```
error[E0277]: `?` couldn't convert the error to `TimeError`
13 |     let hour = hour.parse::<u32>()?;
   |                     --------------^ the trait `From<ParseIntError>` is not implemented for `TimeError`
```

One conversion per step:

- `ok_or(TimeError::NoColon)` turns `None` into `Err(TimeError::NoColon)` and `Some(v)` into `Ok(v)`.
- `map_err(TimeError::BadHour)` turns `Err(e)` into `Err(TimeError::BadHour(e))`. A tuple variant's name is a function from its field to the enum, so it can be passed straight to `map_err`.
- The range check has no std call to convert. It returns early.

## Subgoal 4 · Propagate with `?` and return `Ok` at the end

```rust
pub fn minutes(text: &str) -> Result<u32, TimeError> {
    let (hour, minute) = text.split_once(':').ok_or(TimeError::NoColon)?;
    let hour = hour.parse::<u32>().map_err(TimeError::BadHour)?;
    let minute = minute.parse::<u32>().map_err(TimeError::BadMinute)?;
    if hour >= 24 || minute >= 60 {
        return Err(TimeError::OutOfRange);
    }
    Ok(hour * 60 + minute)
}
```

Each `?` either unwraps an `Ok` and goes on, or returns the `Err` from `minutes` there and then. The lines read as the happy path, and every failure leaves at the step that caused it.

The `unwrap` version of the same function compiles and passes every happy-path test. On `"7:xx"` it stops the whole program:

```
called `Result::unwrap()` on an `Err` value: ParseIntError { kind: InvalidDigit }
```

A caller handed a `TimeError` can recover. A caller whose program panicked cannot.

`cargo test`: green.

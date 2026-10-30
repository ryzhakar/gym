//! Sensor readings such as `"12.5kg"`. See attempt.md.

/// The number in `reading` with `unit` cut off its end: `"12.5kg"` and `"kg"` give `"12.5"`.
/// A reading that does not end in `unit` comes back whole.
pub fn number_of(reading: &str, unit: &str) -> &str {
    match reading.strip_suffix(unit) {
        Some(number) => number,
        None => reading,
    }
}

/// The first line of `log`, or `fallback` when `log` has no lines.
pub fn first_reading(log: &str, fallback: &str) -> &str {
    match log.lines().next() {
        Some(line) => line,
        None => fallback,
    }
}

/// `a` when it ends in `unit`, otherwise `b`.
pub fn prefer_unit<'a>(a: &'a str, b: &'a str, unit: &'a str) -> &'a str {
    match a.strip_suffix(unit) {
        Some(_) => a,
        None => b,
    }
}

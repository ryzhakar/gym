/// The text of `line` after the first `marker`; all of `line` when `marker` does not occur.
pub fn after<'a>(line: &'a str, marker: &str) -> &'a str {
    match line.split_once(marker) {
        Some((_, rest)) => rest,
        None => line,
    }
}

/// `line` with the two sides around the first `marker` swapped; all of `line` when `marker` does not occur.
pub fn swap(line: &str, marker: &str) -> String {
    match line.split_once(marker) {
        Some((left, right)) => format!("{right}{marker}{left}"),
        None => String::from(line),
    }
}

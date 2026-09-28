/// Returns the part of `line` before the first `sep`, or all of `line` when `sep` does not occur.
pub fn key_of(line: &str, sep: &str) -> &str {
    match line.find(sep) {
        Some(i) => &line[..i],
        None => line,
    }
}

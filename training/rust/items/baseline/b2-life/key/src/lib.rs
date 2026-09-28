/// Returns the part of `line` before the first `sep`, or all of `line` when `sep` does not occur.
pub fn key_of<'a>(line: &'a str, sep: &str) -> &'a str {
    match line.find(sep) {
        Some(i) => &line[..i],
        None => line,
    }
}

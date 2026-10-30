pub fn tail(line: &str) -> &str {
    let text = line;
    match text.split_once(' ') {
        Some((_, rest)) => rest,
        None => text,
    }
}

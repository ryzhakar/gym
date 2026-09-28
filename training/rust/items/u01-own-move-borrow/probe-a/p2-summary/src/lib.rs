/// Total bytes over all lines.
pub fn byte_total(lines: Vec<String>) -> usize {
    let mut total = 0;
    for line in &lines {
        total += line.len();
    }
    total
}

/// `"<number of lines> lines, <total bytes> bytes"`.
pub fn summary(lines: Vec<String>) -> String {
    let bytes = byte_total(lines);
    format!("{} lines, {bytes} bytes", lines.len())
}

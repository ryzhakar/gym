pub fn bin_before<'a>(stock_line: &'a str, marker: &str) -> &'a str {
    match stock_line.find(marker) {
        Some(at) => &stock_line[..at],
        None => stock_line,
    }
}

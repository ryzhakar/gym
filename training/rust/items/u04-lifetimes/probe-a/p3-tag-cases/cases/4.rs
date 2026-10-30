pub fn line_longer_than<'a>(text: &'a str, min: &str) -> &'a str {
    for line in text.lines() {
        if line.len() > min.len() {
            return line;
        }
    }
    text
}

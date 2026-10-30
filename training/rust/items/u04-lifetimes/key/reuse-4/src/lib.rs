//! A service log. Each line reads `LEVEL source: message`, e.g. `WARN disk: 91% full`.

#[derive(Debug)]
pub struct Entry<'a> {
    level: &'a str,
    source: &'a str,
    message: &'a str,
}

impl<'a> Entry<'a> {
    /// One log line, or `None` if it does not read `LEVEL source: message`.
    pub fn parse(line: &'a str) -> Option<Entry<'a>> {
        let (level, rest) = line.split_once(' ')?;
        let (source, message) = rest.split_once(": ")?;
        Some(Entry { level, source, message })
    }

    pub fn level(&self) -> &'a str {
        self.level
    }

    pub fn source(&self) -> &'a str {
        self.source
    }

    pub fn message(&self) -> &'a str {
        self.message
    }
}

/// Every line of `log` that parses, in order.
pub fn entries(log: &str) -> Vec<Entry<'_>> {
    let mut found = Vec::new();
    for line in log.lines() {
        if let Some(entry) = Entry::parse(line) {
            found.push(entry);
        }
    }
    found
}

/// The message of the first entry at `level`, if there is one.
/// Borrows from `log` only: `level` may be dropped before the result is used.
pub fn first_message<'a>(log: &'a str, level: &str) -> Option<&'a str> {
    for entry in entries(log) {
        if entry.level() == level {
            return Some(entry.message());
        }
    }
    None
}

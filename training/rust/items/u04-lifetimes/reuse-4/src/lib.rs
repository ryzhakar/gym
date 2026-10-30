//! A service log. Each line reads `LEVEL source: message`, e.g. `WARN disk: 91% full`.

#[derive(Debug)]
pub struct Entry {
    level: String,
    source: String,
    message: String,
}

impl Entry {
    /// One log line, or `None` if it does not read `LEVEL source: message`.
    pub fn parse(line: &str) -> Option<Entry> {
        let (level, rest) = line.split_once(' ')?;
        let (source, message) = rest.split_once(": ")?;
        Some(Entry {
            level: level.to_string(),
            source: source.to_string(),
            message: message.to_string(),
        })
    }

    pub fn level(&self) -> String {
        self.level.clone()
    }

    pub fn source(&self) -> String {
        self.source.clone()
    }

    pub fn message(&self) -> String {
        self.message.clone()
    }
}

/// Every line of `log` that parses, in order.
pub fn entries(log: &str) -> Vec<Entry> {
    let mut found = Vec::new();
    for line in log.lines() {
        if let Some(entry) = Entry::parse(line) {
            found.push(entry);
        }
    }
    found
}

/// The message of the first entry at `level`, if there is one.
pub fn first_message(log: &str, level: &str) -> Option<String> {
    for entry in entries(log) {
        if entry.level() == level.to_string() {
            return Some(entry.message());
        }
    }
    None
}

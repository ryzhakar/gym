/// Appends `line` to `log` and returns the length of the line that was last before it, 0 if none.
pub fn append(log: &mut Vec<String>, line: String) -> usize {
    let previous = log.last();
    let previous_len = match previous {
        Some(text) => text.len(),
        None => 0,
    };
    log.push(line);
    previous_len
}

/// Marks the entry at `index` with " (done)", adds `next` at the end, and returns the number of entries.
pub fn finish(entries: &mut Vec<String>, index: usize, next: String) -> usize {
    let entry = &mut entries[index];
    entry.push_str(" (done)");
    entries.push(next);
    entries.len()
}

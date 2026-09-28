pub struct Tidy {
    pub removed: usize,
    pub last: Option<String>,
}

fn drop_repeats(mut names: Vec<String>) -> usize {
    let before = names.len();
    names.sort();
    names.dedup();
    before - names.len()
}

/// Sorts the names, drops repeats, and reports what was removed and what is last.
pub fn tidy(mut names: Vec<String>) -> Tidy {
    let removed = drop_repeats(names);
    let last = names.pop();
    Tidy { removed, last }
}

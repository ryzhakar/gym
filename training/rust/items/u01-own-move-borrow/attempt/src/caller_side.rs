//! Edit `a_report` only. `count_starting` stays as written.

/// Number of names that start with `letter`.
pub fn count_starting(names: Vec<String>, letter: char) -> usize {
    let mut n = 0;
    for name in &names {
        if name.starts_with(letter) {
            n += 1;
        }
    }
    n
}

/// `"<names starting with a>/<all names>"`.
pub fn a_report(names: Vec<String>) -> String {
    let a = count_starting(names, 'a');
    format!("{a}/{}", names.len())
}

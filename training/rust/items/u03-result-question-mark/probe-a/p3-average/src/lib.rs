use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum AvgError {
    /// No entries at all.
    Empty,
    /// The entry at `index` (counting from 0) has no `=`.
    NoEquals { index: usize },
    /// The number of the entry at `index` (counting from 0) is not an `i64`.
    Bad { index: usize, source: ParseIntError },
}

/// The integer average of the numbers in `entries`, each written `label=number`.
pub fn average(entries: &[&str]) -> Result<i64, AvgError> {
    let mut sum = 0;
    for entry in entries {
        let (_, number) = entry.split_once('=').unwrap();
        sum += number.parse::<i64>().unwrap();
    }
    Ok(sum / entries.len() as i64)
}

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
    if entries.is_empty() {
        return Err(AvgError::Empty);
    }
    let mut sum = 0;
    for (index, entry) in entries.iter().enumerate() {
        let (_, number) = entry.split_once('=').ok_or(AvgError::NoEquals { index })?;
        sum += number.parse::<i64>().map_err(|source| AvgError::Bad { index, source })?;
    }
    Ok(sum / entries.len() as i64)
}

use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum AvgError {
    /// No values at all.
    Empty,
    /// The value at `index` (counting from 0) is not an `i64`.
    Bad { index: usize, source: ParseIntError },
}

/// The integer average of `values`.
pub fn average(values: &[&str]) -> Result<i64, AvgError> {
    if values.is_empty() {
        return Err(AvgError::Empty);
    }
    let mut sum = 0;
    for (index, v) in values.iter().enumerate() {
        sum += v.parse::<i64>().map_err(|source| AvgError::Bad { index, source })?;
    }
    Ok(sum / values.len() as i64)
}

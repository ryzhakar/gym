use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum TallyError {
    /// No counts at all.
    NoBallots,
    /// The count at `at` (counting from 0) is not a `u32`.
    BadEntry { at: usize, source: ParseIntError },
}

#[derive(Debug, PartialEq)]
pub struct Tally {
    pub total: u32,
    pub largest: u32,
}

/// Totals whitespace-separated ballot counts, noting the largest.
pub fn tally(counts: &str) -> Result<Tally, TallyError> {
    if counts.split_whitespace().next().is_none() {
        return Err(TallyError::NoBallots);
    }
    let mut total: u32 = 0;
    let mut largest: u32 = 0;
    for (at, token) in counts.split_whitespace().enumerate() {
        let n: u32 = token.parse().map_err(|source| TallyError::BadEntry { at, source })?;
        total += n;
        if n > largest {
            largest = n;
        }
    }
    Ok(Tally { total, largest })
}

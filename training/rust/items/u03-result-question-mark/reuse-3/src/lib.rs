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
    todo!()
}

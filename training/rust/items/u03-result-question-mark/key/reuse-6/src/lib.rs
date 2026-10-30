use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum LoadError {
    /// No lines at all.
    Empty,
    /// The line at `line` (counting from 0) is not a `u32`.
    BadLine { line: usize, source: ParseIntError },
    /// The running total went past `u32::MAX`.
    Overflow,
}

#[derive(Debug, PartialEq)]
pub struct Load {
    pub grams: u32,
    pub heaviest: u32,
}

/// Weighs a manifest of one parcel weight in grams per line, noting the heaviest.
pub fn weigh(manifest: &str) -> Result<Load, LoadError> {
    if manifest.lines().next().is_none() {
        return Err(LoadError::Empty);
    }
    let mut grams: u32 = 0;
    let mut heaviest: u32 = 0;
    for (line, text) in manifest.lines().enumerate() {
        let weight: u32 = text.parse().map_err(|source| LoadError::BadLine { line, source })?;
        grams = grams.checked_add(weight).ok_or(LoadError::Overflow)?;
        heaviest = heaviest.max(weight);
    }
    Ok(Load { grams, heaviest })
}

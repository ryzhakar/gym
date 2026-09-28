use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum SizeError {
    /// No `x` in the input.
    MissingX,
    /// The part before the first `x` is not a `u32`.
    BadWidth(ParseIntError),
    /// The part after the first `x` is not a `u32`.
    BadHeight(ParseIntError),
}

/// Width times height, from `"<width>x<height>"`.
pub fn area(size: &str) -> Result<u32, SizeError> {
    let (w, h) = size.split_once('x').ok_or(SizeError::MissingX)?;
    let w = w.parse::<u32>()?;
    let h = h.parse::<u32>()?;
    Ok(w * h)
}

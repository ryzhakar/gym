use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum RangeError {
    NoSeparator,
    BadLow(ParseIntError),
    BadHigh(ParseIntError),
}

/// Parses a range written `lo..hi`.
pub fn parse_range(text: &str) -> Result<(i32, i32), RangeError> {
    let (lo, hi) = text.split_once("..").ok_or(RangeError::NoSeparator)?;
    let lo = lo.parse::<i32>()?;
    let hi = hi.parse::<i32>()?;
    Ok((lo, hi))
}

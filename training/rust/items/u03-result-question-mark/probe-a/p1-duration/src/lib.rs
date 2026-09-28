use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum DurationError {
    /// The text does not end in `s` or `m`.
    NoUnit,
    /// The part before the unit is not a `u32`.
    BadNumber(ParseIntError),
    /// The duration in seconds does not fit in a `u32`.
    TooLong,
}

/// `"<n>s"` or `"<n>m"`, in seconds.
pub fn seconds(text: &str) -> Result<u32, DurationError> {
    todo!()
}

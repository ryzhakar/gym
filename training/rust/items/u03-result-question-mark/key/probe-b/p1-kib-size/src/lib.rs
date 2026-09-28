use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum SizeError {
    MissingUnit,
    BadNumber(ParseIntError),
    TooLarge,
}

/// Converts a size written in kibibytes, such as "64KiB", to bytes.
pub fn kib_to_bytes(text: &str) -> Result<u32, SizeError> {
    let count = text.strip_suffix("KiB").ok_or(SizeError::MissingUnit)?;
    let count: u32 = count.parse().map_err(SizeError::BadNumber)?;
    count.checked_mul(1024).ok_or(SizeError::TooLarge)
}

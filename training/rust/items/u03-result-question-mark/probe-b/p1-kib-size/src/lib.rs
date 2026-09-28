use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum SizeError {
    MissingUnit,
    BadNumber(ParseIntError),
    TooLarge,
}

/// Converts a size written in kibibytes, such as "64KiB", to bytes.
pub fn kib_to_bytes(text: &str) -> Result<u32, SizeError> {
    todo!()
}

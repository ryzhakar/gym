use std::num::ParseIntError;
use std::str::Utf8Error;

#[derive(Debug, PartialEq)]
pub enum ReadError {
    /// The bytes are not UTF-8.
    Utf8(Utf8Error),
    /// The text, trimmed, is not a `u32`.
    Number(ParseIntError),
}

impl From<Utf8Error> for ReadError {
    fn from(e: Utf8Error) -> Self {
        ReadError::Utf8(e)
    }
}

impl From<ParseIntError> for ReadError {
    fn from(e: ParseIntError) -> Self {
        ReadError::Number(e)
    }
}

/// The number a sensor sent as raw bytes.
pub fn parse_reading(bytes: &[u8]) -> Result<u32, ReadError> {
    let text = std::str::from_utf8(bytes)?;
    let n = text.trim().parse::<u32>()?;
    Ok(n)
}

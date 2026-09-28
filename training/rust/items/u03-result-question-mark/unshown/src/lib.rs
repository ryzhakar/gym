use std::num::ParseIntError;
use std::str::Utf8Error;

#[derive(Debug, PartialEq)]
pub enum ReadError {
    /// The bytes are not UTF-8.
    Utf8(Utf8Error),
    /// The text, trimmed, is not a `u32`.
    Number(ParseIntError),
}

/// The number a sensor sent as raw bytes.
pub fn parse_reading(bytes: &[u8]) -> Result<u32, ReadError> {
    todo!()
}

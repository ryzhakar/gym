use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum TagError {
    /// No `:` in the input.
    NoColon,
    /// The part after the `:` is not a `u32`.
    BadCode(ParseIntError),
}

/// Parses `"name:code"`.
pub fn parse_tag(text: &str) -> Result<(String, u32), TagError> {
    let (name, code) = text.split_once(':').map_err(|_| TagError::NoColon)?;
    let code = code.parse::<u32>().map_err(TagError::BadCode)?;
    Ok((name.to_string(), code))
}

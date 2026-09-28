use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum AddrError {
    /// The input has no `:`.
    MissingColon,
    /// The part after the first `:` is not a `u16`.
    BadPort(ParseIntError),
}

/// Parses `"host:port"` and returns the port.
pub fn port_of(addr: &str) -> Result<u16, AddrError> {
    let (_host, port) = addr.split_once(':').ok_or(AddrError::MissingColon)?;
    let port = port.parse::<u16>().map_err(AddrError::BadPort)?;
    Ok(port)
}

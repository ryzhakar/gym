use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum AddrError {
    /// The address has no `:`.
    NoColon,
    /// The port is not a `u16`.
    BadPort(ParseIntError),
    /// The port is below 1024.
    Reserved(u16),
}

/// The host and port of `"host:port"`.
pub fn host_port(addr: &str) -> Result<(&str, u16), AddrError> {
    let (host, port) = addr.split_once(':').ok_or(AddrError::NoColon)?;
    let port = port.parse::<u16>().map_err(AddrError::BadPort)?;
    if port < 1024 {
        return Err(AddrError::Reserved(port));
    }
    Ok((host, port))
}

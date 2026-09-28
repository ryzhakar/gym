use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum LinkError {
    BadPort(ParseIntError),
    BadVlan(ParseIntError),
    ReservedVlan,
}

#[derive(Debug, PartialEq)]
pub struct Link {
    pub port: u8,
    pub vlan: u16,
}

/// Parses a switch port and the VLAN it carries.
pub fn link(port: &str, vlan: &str) -> Result<Link, LinkError> {
    let port = port.parse::<u8>()?;
    let vlan = vlan.parse::<u16>()?;
    if vlan == 0 {
        return Err(LinkError::ReservedVlan);
    }
    Ok(Link { port, vlan })
}

use std::num::ParseIntError;
use u03_probe_b_p2::{link, Link, LinkError};

fn u8_error(text: &str) -> ParseIntError {
    match text.parse::<u8>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

fn u16_error(text: &str) -> ParseIntError {
    match text.parse::<u16>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn parses_both() {
    assert_eq!(link("7", "300"), Ok(Link { port: 7, vlan: 300 }));
}

#[test]
fn bad_port() {
    assert_eq!(link("x", "300"), Err(LinkError::BadPort(u8_error("x"))));
}

#[test]
fn bad_vlan() {
    assert_eq!(link("7", "y"), Err(LinkError::BadVlan(u16_error("y"))));
}

#[test]
fn reserved_vlan() {
    assert_eq!(link("7", "0"), Err(LinkError::ReservedVlan));
}

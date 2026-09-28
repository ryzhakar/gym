use std::num::ParseIntError;
use u03_probe_b_p2::{link, Link, LinkError};

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

#[test]
fn no_panic_on_input() {
    let code = code();
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}

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
fn signature_is_kept() {
    let _: fn(&str, &str) -> Result<Link, LinkError> = link;
}

#[test]
fn types_are_kept() {
    fn variants(e: LinkError) -> u8 {
        match e {
            LinkError::BadPort(_) => 0,
            LinkError::BadVlan(_) => 1,
            LinkError::ReservedVlan => 2,
        }
    }
    assert_eq!(variants(LinkError::BadVlan(u16_error("x"))), 1);
    let Link { port, vlan } = Link { port: 1u8, vlan: 2u16 };
    assert_eq!((port, vlan), (1, 2));
}

#[test]
fn port_reported_first() {
    assert_eq!(link("x", "y"), Err(LinkError::BadPort(u8_error("x"))));
    assert_eq!(link("x", "0"), Err(LinkError::BadPort(u8_error("x"))));
    assert_eq!(link("", ""), Err(LinkError::BadPort(u8_error(""))));
}

#[test]
fn vlan_parse_reported_before_the_reserved_check() {
    assert_eq!(link("1", "-0"), Err(LinkError::BadVlan(u16_error("-0"))));
    assert_eq!(link("1", ""), Err(LinkError::BadVlan(u16_error(""))));
}

#[test]
fn port_overflows_where_a_u16_would_not() {
    assert_eq!(link("256", "1"), Err(LinkError::BadPort(u8_error("256"))));
}

#[test]
fn vlan_overflow() {
    assert_eq!(link("1", "65536"), Err(LinkError::BadVlan(u16_error("65536"))));
}

#[test]
fn extremes() {
    assert_eq!(link("255", "65535"), Ok(Link { port: 255, vlan: 65535 }));
    assert_eq!(link("0", "1"), Ok(Link { port: 0, vlan: 1 }));
    assert_eq!(link("0", "00"), Err(LinkError::ReservedVlan));
}

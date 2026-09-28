use b3_result::{port_of, AddrError};

#[test]
fn parses_the_port() {
    assert_eq!(port_of("db:5432"), Ok(5432));
}

#[test]
fn no_colon() {
    assert_eq!(port_of("db"), Err(AddrError::MissingColon));
}

#[test]
fn port_not_a_number() {
    assert!(matches!(port_of("db:http"), Err(AddrError::BadPort(_))));
}

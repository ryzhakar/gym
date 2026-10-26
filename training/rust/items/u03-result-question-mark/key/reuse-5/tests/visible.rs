use u03_reuse_5::{host_port, AddrError};

#[test]
fn host_and_port() {
    assert_eq!(host_port("example.org:8080"), Ok(("example.org", 8080)));
}

#[test]
fn no_colon() {
    assert_eq!(host_port("example.org"), Err(AddrError::NoColon));
}

#[test]
fn bad_port() {
    assert!(matches!(host_port("example.org:http"), Err(AddrError::BadPort(_))));
}

#[test]
fn reserved() {
    assert_eq!(host_port("example.org:80"), Err(AddrError::Reserved(80)));
}

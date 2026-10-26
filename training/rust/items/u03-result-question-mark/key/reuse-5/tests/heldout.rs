use u03_reuse_5::{host_port, AddrError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<u16>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn signature_is_unchanged() {
    let _: for<'a> fn(&'a str) -> Result<(&'a str, u16), AddrError> = host_port;
}

#[test]
fn port_bounds() {
    assert_eq!(host_port("h:1023"), Err(AddrError::Reserved(1023)));
    assert_eq!(host_port("h:0"), Err(AddrError::Reserved(0)));
    assert_eq!(host_port("h:1024"), Ok(("h", 1024)));
    assert_eq!(host_port("h:65535"), Ok(("h", 65535)));
    assert_eq!(host_port("h:65536"), Err(AddrError::BadPort(int_error("65536"))));
}

#[test]
fn splits_at_the_first_colon() {
    assert_eq!(host_port("h:80:90"), Err(AddrError::BadPort(int_error("80:90"))));
    assert_eq!(host_port(":2000"), Ok(("", 2000)));
    assert_eq!(host_port("h:"), Err(AddrError::BadPort(int_error(""))));
}

#[test]
fn propagates_and_never_panics() {
    let src = include_str!("../src/lib.rs");
    assert!(src.contains('?'), "no `?` in src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

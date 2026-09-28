use b3_result::{port_of, AddrError};

fn parse_error_of(text: &str) -> std::num::ParseIntError {
    match text.parse::<u16>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn out_of_range_carries_the_parse_error() {
    assert_eq!(port_of("db:70000"), Err(AddrError::BadPort(parse_error_of("70000"))));
}

#[test]
fn splits_at_the_first_colon() {
    assert_eq!(port_of("a:b:1"), Err(AddrError::BadPort(parse_error_of("b:1"))));
}

#[test]
fn empty_port_is_bad() {
    assert_eq!(port_of("db:"), Err(AddrError::BadPort(parse_error_of(""))));
}

#[test]
fn empty_host_is_fine() {
    assert_eq!(port_of(":80"), Ok(80));
}

#[test]
fn empty_input_has_no_colon() {
    assert_eq!(port_of(""), Err(AddrError::MissingColon));
}

#[test]
fn propagates_with_question_mark_and_never_panics() {
    let src = include_str!("../src/lib.rs");
    assert!(src.contains('?'), "no `?` in src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

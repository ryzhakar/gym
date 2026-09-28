use u03_unshown::{parse_reading, ReadError};

#[test]
fn empty_is_a_number_error() {
    assert!(matches!(parse_reading(b""), Err(ReadError::Number(_))));
    assert!(matches!(parse_reading(b"   "), Err(ReadError::Number(_))));
}

#[test]
fn utf8_is_checked_before_the_number() {
    assert!(matches!(parse_reading(&[b'x', 0xff]), Err(ReadError::Utf8(_))));
}

#[test]
fn largest_value() {
    assert_eq!(parse_reading(b"4294967295"), Ok(u32::MAX));
    assert!(matches!(parse_reading(b"4294967296"), Err(ReadError::Number(_))));
}

#[test]
fn conversions_go_through_from() {
    let src = include_str!("../src/lib.rs");
    assert!(src.contains('?'), "no `?` in src/lib.rs");
    assert!(!src.contains("map_err") && !src.contains("match "), "src/lib.rs converts by hand");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

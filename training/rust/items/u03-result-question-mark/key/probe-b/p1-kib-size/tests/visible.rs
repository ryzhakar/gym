use std::num::ParseIntError;
use u03_probe_b_p1::{kib_to_bytes, SizeError};

fn parse_error(text: &str) -> ParseIntError {
    match text.parse::<u32>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn converts_a_size() {
    assert_eq!(kib_to_bytes("64KiB"), Ok(65536));
}

#[test]
fn missing_unit() {
    assert_eq!(kib_to_bytes("64kb"), Err(SizeError::MissingUnit));
}

#[test]
fn bad_number() {
    assert_eq!(kib_to_bytes("sixKiB"), Err(SizeError::BadNumber(parse_error("six"))));
}

#[test]
fn too_large() {
    assert_eq!(kib_to_bytes("5000000KiB"), Err(SizeError::TooLarge));
}

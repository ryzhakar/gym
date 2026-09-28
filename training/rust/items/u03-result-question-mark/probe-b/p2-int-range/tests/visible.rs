use std::num::ParseIntError;
use u03_probe_b_p2::{parse_range, RangeError};

fn parse_error(text: &str) -> ParseIntError {
    match text.parse::<i32>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn parses_a_range() {
    assert_eq!(parse_range("3..9"), Ok((3, 9)));
}

#[test]
fn no_separator() {
    assert_eq!(parse_range("3-9"), Err(RangeError::NoSeparator));
}

#[test]
fn bad_low() {
    assert_eq!(parse_range("a..9"), Err(RangeError::BadLow(parse_error("a"))));
}

#[test]
fn bad_high() {
    assert_eq!(parse_range("3..z"), Err(RangeError::BadHigh(parse_error("z"))));
}

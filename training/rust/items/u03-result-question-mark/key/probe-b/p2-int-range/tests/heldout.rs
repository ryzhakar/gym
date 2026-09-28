use std::num::ParseIntError;
use u03_probe_b_p2::{parse_range, RangeError};

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

fn parse_error(text: &str) -> ParseIntError {
    match text.parse::<i32>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn signature_is_kept() {
    let _: fn(&str) -> Result<(i32, i32), RangeError> = parse_range;
}

#[test]
fn enum_is_kept() {
    fn variants(e: RangeError) -> u8 {
        match e {
            RangeError::NoSeparator => 0,
            RangeError::BadLow(_) => 1,
            RangeError::BadHigh(_) => 2,
        }
    }
    assert_eq!(variants(RangeError::BadHigh(parse_error("x"))), 2);
}

#[test]
fn low_reported_before_high() {
    assert_eq!(parse_range("x..y"), Err(RangeError::BadLow(parse_error("x"))));
    assert_eq!(parse_range(".."), Err(RangeError::BadLow(parse_error(""))));
}

#[test]
fn separator_reported_before_numbers() {
    assert_eq!(parse_range("xy"), Err(RangeError::NoSeparator));
    assert_eq!(parse_range(""), Err(RangeError::NoSeparator));
    assert_eq!(parse_range("3.9"), Err(RangeError::NoSeparator));
}

#[test]
fn empty_high() {
    assert_eq!(parse_range("5.."), Err(RangeError::BadHigh(parse_error(""))));
}

#[test]
fn only_the_first_separator_splits() {
    assert_eq!(parse_range("1..2..3"), Err(RangeError::BadHigh(parse_error("2..3"))));
}

#[test]
fn extremes() {
    assert_eq!(parse_range("-2147483648..2147483647"), Ok((i32::MIN, i32::MAX)));
    assert_eq!(parse_range("2147483648..0"), Err(RangeError::BadLow(parse_error("2147483648"))));
    assert_eq!(parse_range("0..-2147483649"), Err(RangeError::BadHigh(parse_error("-2147483649"))));
}

#[test]
fn reversed_bounds_are_kept_as_written() {
    assert_eq!(parse_range("9..-3"), Ok((9, -3)));
}

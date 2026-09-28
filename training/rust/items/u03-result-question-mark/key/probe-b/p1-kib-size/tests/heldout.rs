use std::num::ParseIntError;
use u03_probe_b_p1::{kib_to_bytes, SizeError};

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
    match text.parse::<u32>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn signature_is_kept() {
    let _: fn(&str) -> Result<u32, SizeError> = kib_to_bytes;
}

#[test]
fn enum_is_kept() {
    fn variants(e: SizeError) -> u8 {
        match e {
            SizeError::MissingUnit => 0,
            SizeError::BadNumber(_) => 1,
            SizeError::TooLarge => 2,
        }
    }
    assert_eq!(variants(SizeError::BadNumber(parse_error("x"))), 1);
}

#[test]
fn largest_count_that_fits() {
    assert_eq!(kib_to_bytes("4194303KiB"), Ok(4294966272));
}

#[test]
fn smallest_count_that_overflows() {
    assert_eq!(kib_to_bytes("4194304KiB"), Err(SizeError::TooLarge));
}

#[test]
fn count_too_big_to_parse() {
    assert_eq!(
        kib_to_bytes("4294967296KiB"),
        Err(SizeError::BadNumber(parse_error("4294967296")))
    );
}

#[test]
fn zero() {
    assert_eq!(kib_to_bytes("0KiB"), Ok(0));
}

#[test]
fn empty_input() {
    assert_eq!(kib_to_bytes(""), Err(SizeError::MissingUnit));
}

#[test]
fn unit_alone() {
    assert_eq!(kib_to_bytes("KiB"), Err(SizeError::BadNumber(parse_error(""))));
}

#[test]
fn negative_and_spaced_counts() {
    assert_eq!(kib_to_bytes("-1KiB"), Err(SizeError::BadNumber(parse_error("-1"))));
    assert_eq!(kib_to_bytes(" 64KiB"), Err(SizeError::BadNumber(parse_error(" 64"))));
    assert_eq!(kib_to_bytes("64 KiB"), Err(SizeError::BadNumber(parse_error("64 "))));
    assert_eq!(kib_to_bytes("64KiB "), Err(SizeError::MissingUnit));
}

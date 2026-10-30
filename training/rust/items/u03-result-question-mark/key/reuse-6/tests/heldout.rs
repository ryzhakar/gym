use u03_reuse_6::{weigh, Load, LoadError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<u32>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn first_bad_line_wins() {
    assert_eq!(weigh("x\ny"), Err(LoadError::BadLine { line: 0, source: int_error("x") }));
    assert_eq!(weigh("10\n\n20"), Err(LoadError::BadLine { line: 1, source: int_error("") }));
}

#[test]
fn overflow_is_an_error() {
    assert_eq!(weigh("4000000000\n300000000"), Err(LoadError::Overflow));
}

#[test]
fn total_may_reach_u32_max() {
    assert_eq!(weigh("4294967294\n1"), Ok(Load { grams: u32::MAX, heaviest: 4294967294 }));
}

/// The total overflows at line 1, before line 2 is reached. Parsing every
/// line before adding any reports line 2 instead.
#[test]
fn stops_at_the_first_error() {
    assert_eq!(weigh("4000000000\n300000000\nheavy"), Err(LoadError::Overflow));
}

#[test]
fn single_parcel() {
    assert_eq!(weigh("7"), Ok(Load { grams: 7, heaviest: 7 }));
}

#[test]
fn heaviest_is_not_always_last() {
    assert_eq!(weigh("5\n40\n3"), Ok(Load { grams: 48, heaviest: 40 }));
}

#[test]
fn never_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

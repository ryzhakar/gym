use u03_probe_a_p1::{seconds, DurationError};

#[test]
fn edges() {
    assert_eq!(seconds("0s"), Ok(0));
    assert_eq!(seconds("0m"), Ok(0));
    assert_eq!(seconds("4294967295s"), Ok(u32::MAX));
    assert_eq!(seconds("71582788m"), Ok(4_294_967_280));
    assert_eq!(seconds("71582789m"), Err(DurationError::TooLong));
}

#[test]
fn unit_alone_is_a_bad_number() {
    assert!(matches!(seconds("s"), Err(DurationError::BadNumber(_))));
    assert!(matches!(seconds("m"), Err(DurationError::BadNumber(_))));
}

#[test]
fn empty_has_no_unit() {
    assert_eq!(seconds(""), Err(DurationError::NoUnit));
}

#[test]
fn seconds_too_big_is_a_bad_number() {
    assert!(matches!(seconds("4294967296s"), Err(DurationError::BadNumber(_))));
}

#[test]
fn never_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

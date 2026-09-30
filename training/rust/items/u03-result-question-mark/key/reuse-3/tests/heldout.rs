use u03_reuse_3::{tally, Tally, TallyError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<u32>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn whitespace_only_is_no_ballots() {
    assert_eq!(tally("   "), Err(TallyError::NoBallots));
}

#[test]
fn first_bad_entry_wins() {
    assert_eq!(tally("x y"), Err(TallyError::BadEntry { at: 0, source: int_error("x") }));
    assert_eq!(tally("10 20 z"), Err(TallyError::BadEntry { at: 2, source: int_error("z") }));
}

#[test]
fn single_entry() {
    assert_eq!(tally("7"), Ok(Tally { total: 7, largest: 7 }));
}

#[test]
fn largest_is_not_always_last() {
    assert_eq!(tally("5 40 3"), Ok(Tally { total: 48, largest: 40 }));
}

#[test]
fn never_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

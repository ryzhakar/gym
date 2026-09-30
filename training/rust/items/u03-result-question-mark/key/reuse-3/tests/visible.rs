use u03_reuse_3::{tally, Tally, TallyError};

#[test]
fn totals_and_largest() {
    assert_eq!(tally("10 25 15"), Ok(Tally { total: 50, largest: 25 }));
}

#[test]
fn no_ballots() {
    assert_eq!(tally(""), Err(TallyError::NoBallots));
}

#[test]
fn names_the_bad_entry() {
    assert!(matches!(tally("10 xx 15"), Err(TallyError::BadEntry { at: 1, .. })));
}

use u03_reuse_6::{weigh, Load, LoadError};

#[test]
fn totals_and_heaviest() {
    assert_eq!(weigh("1200\n850\n40"), Ok(Load { grams: 2090, heaviest: 1200 }));
}

#[test]
fn empty_manifest() {
    assert_eq!(weigh(""), Err(LoadError::Empty));
}

#[test]
fn names_the_bad_line() {
    assert!(matches!(weigh("1200\nheavy\n40"), Err(LoadError::BadLine { line: 1, .. })));
}

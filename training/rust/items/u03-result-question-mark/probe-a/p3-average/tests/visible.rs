use u03_probe_a_p3::{average, AvgError};

#[test]
fn averages() {
    assert_eq!(average(&["2", "4", "9"]), Ok(5));
}

#[test]
fn empty() {
    assert_eq!(average(&[]), Err(AvgError::Empty));
}

#[test]
fn names_the_bad_index() {
    assert!(matches!(average(&["1", "two", "3"]), Err(AvgError::Bad { index: 1, .. })));
}

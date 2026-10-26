use u03_probe_a_p3::{average, AvgError};

#[test]
fn averages() {
    assert_eq!(average(&["a=2", "b=4", "c=9"]), Ok(5));
}

#[test]
fn empty() {
    assert_eq!(average(&[]), Err(AvgError::Empty));
}

#[test]
fn names_the_bad_index() {
    assert!(matches!(average(&["a=1", "b=two", "c=3"]), Err(AvgError::Bad { index: 1, .. })));
}

#[test]
fn names_the_entry_without_equals() {
    assert_eq!(average(&["a=1", "b"]), Err(AvgError::NoEquals { index: 1 }));
}

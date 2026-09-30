use u03_probe_a_p2::{administer, DoseError};

#[test]
fn good_dose_reduces_stock() {
    assert_eq!(administer(100, "30"), Ok(70));
}

#[test]
fn bad_number() {
    assert!(matches!(administer(100, "abc"), Err(DoseError::BadAmount(_))));
}

#[test]
fn zero_dose_is_empty() {
    assert_eq!(administer(100, "0"), Err(DoseError::Empty));
}

#[test]
fn dose_above_stock_is_too_much() {
    assert_eq!(administer(10, "11"), Err(DoseError::TooMuch { stock: 10, dose: 11 }));
}

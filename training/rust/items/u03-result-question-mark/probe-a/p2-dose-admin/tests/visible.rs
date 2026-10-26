use u03_probe_a_p2::{administer, DoseError};

const DOSES: &[(&str, u32)] = &[("aspirin", 30), ("saline", 0), ("morphine", 11)];

#[test]
fn good_dose_reduces_stock() {
    assert_eq!(administer(100, "aspirin", DOSES), Ok(70));
}

#[test]
fn unknown_drug() {
    assert_eq!(administer(100, "insulin", DOSES), Err(DoseError::UnknownDrug));
}

#[test]
fn zero_dose_is_empty() {
    assert_eq!(administer(100, "saline", DOSES), Err(DoseError::Empty));
}

#[test]
fn dose_above_stock_is_too_much() {
    assert_eq!(administer(10, "morphine", DOSES), Err(DoseError::TooMuch { stock: 10, dose: 11 }));
}

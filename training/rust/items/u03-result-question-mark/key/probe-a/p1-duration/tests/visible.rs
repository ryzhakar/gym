use u03_probe_a_p1::{seconds, DurationError};

#[test]
fn units() {
    assert_eq!(seconds("90s"), Ok(90));
    assert_eq!(seconds("5m"), Ok(300));
}

#[test]
fn no_unit() {
    assert_eq!(seconds("90"), Err(DurationError::NoUnit));
    assert_eq!(seconds("2h"), Err(DurationError::NoUnit));
}

#[test]
fn bad_number() {
    assert!(matches!(seconds("xs"), Err(DurationError::BadNumber(_))));
}

#[test]
fn too_long() {
    assert_eq!(seconds("100000000m"), Err(DurationError::TooLong));
}

use u03_probe_a_p2::{administer, DoseError};

#[test]
fn signature_is_unchanged() {
    let _: fn(u32, &str, &[(&str, u32)]) -> Result<u32, DoseError> = administer;
}

#[test]
fn dose_equal_to_stock_leaves_zero() {
    assert_eq!(administer(10, "a", &[("a", 10)]), Ok(0));
}

#[test]
fn first_entry_wins_and_names_match_exactly() {
    let doses: &[(&str, u32)] = &[("a", 3), ("a", 0), ("B", 5)];
    assert_eq!(administer(10, "a", doses), Ok(7));
    assert_eq!(administer(10, "b", doses), Err(DoseError::UnknownDrug));
    assert_eq!(administer(10, "a ", doses), Err(DoseError::UnknownDrug));
    assert_eq!(administer(10, "a", &[]), Err(DoseError::UnknownDrug));
}

#[test]
fn checks_run_in_order() {
    assert_eq!(administer(0, "z", &[("z", 0)]), Err(DoseError::Empty));
    assert_eq!(administer(0, "z", &[("z", u32::MAX)]), Err(DoseError::TooMuch { stock: 0, dose: u32::MAX }));
}

#[test]
fn no_banned_calls() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

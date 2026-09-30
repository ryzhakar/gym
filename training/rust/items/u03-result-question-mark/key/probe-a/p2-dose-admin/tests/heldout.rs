use u03_probe_a_p2::{administer, DoseError};

#[test]
fn signature_is_unchanged() {
    let _: fn(u32, &str) -> Result<u32, DoseError> = administer;
}

#[test]
fn dose_equal_to_stock_leaves_zero() {
    assert_eq!(administer(10, "10"), Ok(0));
}

#[test]
fn no_banned_calls() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

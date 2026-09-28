use u03_probe_a_p2::{area, SizeError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<u32>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn signature_is_unchanged() {
    let _: fn(&str) -> Result<u32, SizeError> = area;
}

#[test]
fn width_is_reported_first() {
    assert_eq!(area("axb"), Err(SizeError::BadWidth(int_error("a"))));
}

#[test]
fn empty_parts() {
    assert_eq!(area("x"), Err(SizeError::BadWidth(int_error(""))));
    assert_eq!(area("5x"), Err(SizeError::BadHeight(int_error(""))));
}

#[test]
fn zero_is_fine() {
    assert_eq!(area("0x9"), Ok(0));
}

#[test]
fn never_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

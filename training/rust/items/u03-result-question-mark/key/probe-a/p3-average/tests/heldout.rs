use u03_probe_a_p3::{average, AvgError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<i64>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn first_bad_value_wins() {
    assert_eq!(average(&["x", "y"]), Err(AvgError::Bad { index: 0, source: int_error("x") }));
    assert_eq!(average(&["1", "2", ""]), Err(AvgError::Bad { index: 2, source: int_error("") }));
}

#[test]
fn integer_division_and_negatives() {
    assert_eq!(average(&["1", "2"]), Ok(1));
    assert_eq!(average(&["-3", "-4"]), Ok(-3));
    assert_eq!(average(&["7"]), Ok(7));
}

#[test]
fn never_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

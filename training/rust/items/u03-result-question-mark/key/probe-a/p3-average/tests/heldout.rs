use u03_probe_a_p3::{average, AvgError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<i64>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn first_bad_entry_wins() {
    assert_eq!(average(&["x", "a=y"]), Err(AvgError::NoEquals { index: 0 }));
    assert_eq!(average(&["a=y", "x"]), Err(AvgError::Bad { index: 0, source: int_error("y") }));
    assert_eq!(average(&["a=1", "b=2", "c="]), Err(AvgError::Bad { index: 2, source: int_error("") }));
}

#[test]
fn splits_at_the_first_equals() {
    assert_eq!(average(&["a=b=3"]), Err(AvgError::Bad { index: 0, source: int_error("b=3") }));
    assert_eq!(average(&["=4", "x y=6"]), Ok(5));
}

#[test]
fn integer_division_and_negatives() {
    assert_eq!(average(&["p=1", "q=2"]), Ok(1));
    assert_eq!(average(&["p=-3", "q=-4"]), Ok(-3));
    assert_eq!(average(&["only=7"]), Ok(7));
}

#[test]
fn never_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

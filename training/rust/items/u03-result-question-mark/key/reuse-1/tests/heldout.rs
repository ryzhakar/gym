use u03_reuse_1::{parse_point, Point, PointError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<i32>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn both_bad_reports_x() {
    assert_eq!(parse_point("a,b"), Err(PointError::BadX(int_error("a"))));
}

#[test]
fn first_comma_only() {
    assert_eq!(parse_point("1,2,3"), Err(PointError::BadY(int_error("2,3"))));
}

#[test]
fn spaces_are_not_numbers() {
    assert_eq!(parse_point("1, 2"), Err(PointError::BadY(int_error(" 2"))));
}

#[test]
fn empty_parts() {
    assert_eq!(parse_point(","), Err(PointError::BadX(int_error(""))));
    assert_eq!(parse_point(""), Err(PointError::MissingComma));
}

#[test]
fn extremes() {
    assert_eq!(parse_point("-2147483648,2147483647"), Ok(Point { x: i32::MIN, y: i32::MAX }));
}

#[test]
fn propagates_and_never_panics() {
    let src = include_str!("../src/lib.rs");
    assert!(src.contains('?'), "no `?` in src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

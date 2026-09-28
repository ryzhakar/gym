use u03_reuse_1::{parse_point, Point, PointError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<i32>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn parses() {
    assert_eq!(parse_point("3,-4"), Ok(Point { x: 3, y: -4 }));
}

#[test]
fn missing_comma() {
    assert_eq!(parse_point("3 4"), Err(PointError::MissingComma));
}

#[test]
fn bad_x_and_bad_y_are_told_apart() {
    assert_eq!(parse_point("a,4"), Err(PointError::BadX(int_error("a"))));
    assert_eq!(parse_point("3,b"), Err(PointError::BadY(int_error("b"))));
}

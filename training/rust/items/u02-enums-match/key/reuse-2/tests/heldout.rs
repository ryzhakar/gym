use u02_reuse_2::{cost, dot, endpoint, line, pen_up};

#[test]
fn zero_length_line_costs_one() {
    assert_eq!(cost(line(3, 3, 3, 3)), 1);
}

#[test]
fn negative_directions() {
    assert_eq!(cost(line(5, 5, -5, 2)), 13);
    assert_eq!(endpoint(line(5, 5, -5, 2)), Some((-5, 2)));
}

#[test]
fn dot_at_origin() {
    assert_eq!(cost(dot(0, 0)), 1);
    assert_eq!(endpoint(dot(0, 0)), Some((0, 0)));
    assert_eq!(endpoint(pen_up()), None);
}

#[test]
fn an_enum_with_no_catch_all() {
    let src = include_str!("../src/lib.rs");
    assert!(src.contains("enum Command"), "Command is not an enum");
    assert!(!src.contains("_ =>") && !src.contains("_=>"), "src/lib.rs has a `_` arm");
}

use u04_unshown::{after, swap};

#[test]
fn after_points_into_line() {
    let line = String::from("left|right");
    let rest = after(&line, "|");
    let start = line.as_ptr() as usize;
    let at = rest.as_ptr() as usize;
    assert!(at >= start && at + rest.len() <= start + line.len(), "`after` returns text that is not part of `line`");
}

#[test]
fn after_edges() {
    assert_eq!(after("=x", "="), "x");
    assert_eq!(after("x=", "="), "");
    assert_eq!(after("", "="), "");
    assert_eq!(after("a::b::c", "::"), "b::c");
}

#[test]
fn swap_edges() {
    assert_eq!(swap("=x", "="), "x=");
    assert_eq!(swap("x=", "="), "=x");
    assert_eq!(swap("", "="), "");
    assert_eq!(swap("a::b::c", "::"), "b::c::a");
}

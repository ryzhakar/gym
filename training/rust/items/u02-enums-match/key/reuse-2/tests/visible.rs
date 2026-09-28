use u02_reuse_2::{cost, dot, endpoint, line, pen_up};

#[test]
fn costs() {
    assert_eq!(cost(dot(4, 4)), 1);
    assert_eq!(cost(line(0, 0, 3, -4)), 7);
    assert_eq!(cost(pen_up()), 0);
}

#[test]
fn endpoints() {
    assert_eq!(endpoint(dot(2, 5)), Some((2, 5)));
    assert_eq!(endpoint(line(1, 1, 6, 0)), Some((6, 0)));
    assert_eq!(endpoint(pen_up()), None);
}

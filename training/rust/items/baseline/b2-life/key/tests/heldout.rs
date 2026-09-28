use b2_life::key_of;

#[test]
fn result_borrows_from_line_only() {
    let _: for<'a, 'b> fn(&'a str, &'b str) -> &'a str = key_of;
}

#[test]
fn result_points_into_line() {
    let line = String::from("a::b::c");
    let key = key_of(&line, "::");
    assert_eq!(key, "a");
    assert_eq!(key.as_ptr(), line.as_ptr());
}

#[test]
fn separator_at_start() {
    assert_eq!(key_of("=x", "="), "");
}

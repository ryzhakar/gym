use b2_life::key_of;

#[test]
fn key_outlives_the_separator() {
    let line = String::from("user=arthur");
    let key;
    {
        let sep = String::from("=");
        key = key_of(&line, &sep);
    }
    assert_eq!(key, "user");
}

#[test]
fn no_separator_gives_the_whole_line() {
    assert_eq!(key_of("plain", ":"), "plain");
}

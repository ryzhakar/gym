use u04_reuse_2::Header;

#[test]
fn splits_at_the_first_colon_space_only() {
    let header = Header::parse("Link: a: b; c").unwrap();
    assert_eq!(header.name, "Link");
    assert_eq!(header.value, "a: b; c");
    assert_eq!(header.main_value(), "a: b");
}

#[test]
fn colon_without_space_is_none() {
    assert!(Header::parse("Host:example.com").is_none());
    assert!(Header::parse("").is_none());
}

#[test]
fn first_of_several_semicolons() {
    let header = Header::parse("Set-Cookie: id=7; Path=/; Secure").unwrap();
    assert_eq!(header.main_value(), "id=7");
}

#[test]
fn empty_value_and_empty_main_value() {
    assert_eq!(Header::parse("X-Empty: ").unwrap().main_value(), "");
    assert_eq!(Header::parse("X-Odd: ;q=1").unwrap().main_value(), "");
}

#[test]
fn fields_outlive_the_header() {
    let line = String::from("Accept: text/css");
    let (name, value): (&str, &str) = {
        let header = Header::parse(&line).unwrap();
        (header.name, header.value)
    };
    assert_eq!((name, value), ("Accept", "text/css"));
}

#[test]
fn main_values_collected_from_temporary_headers() {
    let text = String::from("Content-Type: text/csv; header=present\nAccept: */*\nVary: Origin; x");
    let mains: Vec<&str> = text.lines().map(|line| Header::parse(line).unwrap().main_value()).collect();
    assert_eq!(mains, ["text/csv", "*/*", "Origin"]);
}

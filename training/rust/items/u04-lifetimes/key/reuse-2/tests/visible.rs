use u04_reuse_2::Header;

#[test]
fn parse_splits_name_and_value() {
    let header = Header::parse("Content-Type: text/html; charset=utf-8").unwrap();
    assert_eq!(header.name, "Content-Type");
    assert_eq!(header.value, "text/html; charset=utf-8");
}

#[test]
fn parse_needs_colon_and_space() {
    assert!(Header::parse("Content-Type text/html").is_none());
}

#[test]
fn main_value_stops_at_the_first_semicolon() {
    let header = Header::parse("Content-Type: text/html; charset=utf-8").unwrap();
    assert_eq!(header.main_value(), "text/html");
    let header = Header::parse("Accept: */*").unwrap();
    assert_eq!(header.main_value(), "*/*");
}

#[test]
fn main_value_outlives_a_dropped_header() {
    let line = String::from("Content-Type: text/plain; charset=ascii");
    let main: &str = {
        let header = Header::parse(&line).unwrap();
        header.main_value()
    };
    assert_eq!(main, "text/plain");
}

#[test]
fn main_value_outlives_a_moved_header() {
    let line = String::from("Cache-Control: no-cache; private");
    let header = Header::parse(&line).unwrap();
    let main = header.main_value();
    let moved = header;
    drop(moved);
    assert_eq!(main, "no-cache");
}

fn media_type(line: &str) -> &str {
    Header::parse(line).unwrap().main_value()
}

#[test]
fn main_value_leaves_the_function_that_parsed() {
    let line = String::from("Content-Type: image/png");
    assert_eq!(media_type(&line), "image/png");
}

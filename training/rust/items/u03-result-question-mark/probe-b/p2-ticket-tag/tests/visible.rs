use u03_probe_b_p2::{parse_tag, TagError};

#[test]
fn good_tag() {
    assert_eq!(parse_tag("widget:42"), Ok(("widget".to_string(), 42)));
}

#[test]
fn no_colon() {
    assert_eq!(parse_tag("no-colon-here"), Err(TagError::NoColon));
}

#[test]
fn bad_code() {
    assert!(matches!(parse_tag("widget:oops"), Err(TagError::BadCode(_))));
}

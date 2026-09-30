use u03_probe_b_p2::{parse_tag, TagError};

#[test]
fn signature_is_unchanged() {
    let _: fn(&str) -> Result<(String, u32), TagError> = parse_tag;
}

#[test]
fn splits_at_the_first_colon_only() {
    assert!(matches!(parse_tag("a:1:2"), Err(TagError::BadCode(_))));
}

#[test]
fn no_banned_calls() {
    let src = include_str!("../src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

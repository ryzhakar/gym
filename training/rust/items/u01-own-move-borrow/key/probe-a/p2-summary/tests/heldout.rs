use u01_probe_a_p2::summary;

#[test]
fn signature_is_unchanged() {
    let _: fn(Vec<String>) -> String = summary;
}

#[test]
fn no_lines() {
    assert_eq!(summary(Vec::new()), "0 lines, 0 bytes");
}

#[test]
fn empty_lines_count() {
    assert_eq!(summary(vec![String::new(), "x".to_string(), String::new()]), "3 lines, 1 bytes");
}

#[test]
fn no_copies() {
    let src = include_str!("../src/lib.rs");
    for banned in ["clone", "to_owned", "to_vec", "to_string"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

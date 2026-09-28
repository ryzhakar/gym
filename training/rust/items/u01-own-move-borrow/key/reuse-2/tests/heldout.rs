use u01_reuse_2::broadcast;

#[test]
fn signature_is_unchanged() {
    let _: fn(&[String], String) -> Vec<String> = broadcast;
}

#[test]
fn nobody_to_tell() {
    assert!(broadcast(&[], "hi".to_string()).is_empty());
}

#[test]
fn three_recipients() {
    let to = vec!["a".to_string(), "b".to_string(), "c".to_string()];
    assert_eq!(broadcast(&to, "x".to_string()), vec!["a: x", "b: x", "c: x"]);
}

#[test]
fn msg_is_not_copied() {
    let src = include_str!("../src/lib.rs");
    for banned in ["clone", "to_owned", "to_string"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

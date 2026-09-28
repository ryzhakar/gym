use u02_probe_a_p2::sign_of;

#[test]
fn signature_is_unchanged() {
    let _: fn(Option<i32>) -> String = sign_of;
}

#[test]
fn extremes() {
    assert_eq!(sign_of(Some(i32::MAX)), format!("positive {}", i32::MAX));
    assert_eq!(sign_of(Some(i32::MIN)), format!("negative {}", i32::MIN));
    assert_eq!(sign_of(Some(1)), "positive 1");
    assert_eq!(sign_of(Some(-1)), "negative -1");
}

#[test]
fn no_arm_panics() {
    let src = include_str!("../src/lib.rs");
    for banned in ["panic!", "unreachable!", "todo!", "unimplemented!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

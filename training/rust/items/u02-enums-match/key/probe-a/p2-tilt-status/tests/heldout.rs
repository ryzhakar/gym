use u02_probe_a_p2::tilt_status;

#[test]
fn signature_is_unchanged() {
    let _: fn(Option<i32>) -> String = tilt_status;
}

#[test]
fn large_magnitudes() {
    assert_eq!(tilt_status(Some(1000)), "right 1000");
    assert_eq!(tilt_status(Some(-1000)), "left -1000");
}

#[test]
fn no_panicking_macros() {
    let src = include_str!("../src/lib.rs");
    for banned in ["panic!", "unreachable!", "todo!", "unimplemented!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

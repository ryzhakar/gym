use u02_probe_b_p2::{handling, Handling, Load};

#[test]
fn signature_is_unchanged() {
    let _: fn(Load) -> Handling = handling;
}

#[test]
fn heavy_and_fragile_is_still_careful() {
    assert_eq!(handling(Load::Crate { weight: 900, fragile: true }), Handling::Careful);
}

#[test]
fn boundary_weight_is_not_careful() {
    assert_eq!(handling(Load::Crate { weight: 500, fragile: false }), Handling::Normal);
}

#[test]
fn at_most_four_arms_and_no_panics() {
    let src = include_str!("../src/lib.rs");
    let match_count = src.matches("match ").count();
    assert_eq!(match_count, 1, "expected exactly one match");
    let arm_count = src.matches("=>").count();
    assert!(arm_count <= 4, "match has more than four arms");
    for banned in ["panic!", "unreachable!", "todo!", "unimplemented!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

use u02_probe_a_p2::sign_of;

#[test]
fn every_case() {
    assert_eq!(sign_of(None), "none");
    assert_eq!(sign_of(Some(5)), "positive 5");
    assert_eq!(sign_of(Some(0)), "zero");
    assert_eq!(sign_of(Some(-3)), "negative -3");
}

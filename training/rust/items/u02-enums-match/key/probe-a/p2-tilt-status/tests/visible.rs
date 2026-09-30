use u02_probe_a_p2::tilt_status;

#[test]
fn reports_each_case() {
    assert_eq!(tilt_status(None), "none");
    assert_eq!(tilt_status(Some(3)), "right 3");
    assert_eq!(tilt_status(Some(0)), "level");
    assert_eq!(tilt_status(Some(-3)), "left -3");
}

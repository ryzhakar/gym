use u02_probe_b_p2::{handling, Handling, Load};

#[test]
fn classifies_each_case() {
    assert_eq!(handling(Load::Crate { weight: 600, fragile: false }), Handling::Careful);
    assert_eq!(handling(Load::Crate { weight: 100, fragile: true }), Handling::Careful);
    assert_eq!(handling(Load::Crate { weight: 100, fragile: false }), Handling::Normal);
    assert_eq!(handling(Load::Empty), Handling::Skip);
}

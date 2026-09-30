use u01_probe_c_p3::{cart_summary, Cart};

#[test]
fn clears_and_reports_empty() {
    let cart = Cart { items: vec!["pen".to_string(), "cup".to_string()] };
    assert_eq!(cart_summary(cart), "2 items cleared, now empty: true");
}

use u01_probe_c_p3::{cart_summary, Cart};

#[test]
fn signature_is_unchanged() {
    let _: fn(Cart) -> String = cart_summary;
}

#[test]
fn already_empty_cart() {
    let cart = Cart { items: Vec::new() };
    assert_eq!(cart_summary(cart), "0 items cleared, now empty: true");
}

#[test]
fn one_item() {
    let cart = Cart { items: vec!["book".to_string()] };
    assert_eq!(cart_summary(cart), "1 items cleared, now empty: true");
}

#[test]
fn no_copies() {
    let src = include_str!("../src/lib.rs");
    for banned in ["clone", "to_owned", "to_vec", "to_string"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}

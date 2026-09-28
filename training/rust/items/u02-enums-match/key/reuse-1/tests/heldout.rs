use u02_reuse_1::{price, Ticket};

#[test]
fn boundaries() {
    assert_eq!(price(Ticket::Adult { age: 64 }), 1200);
    assert_eq!(price(Ticket::Adult { age: 65 }), 800);
    assert_eq!(price(Ticket::Child { age: 2 }), 0);
    assert_eq!(price(Ticket::Child { age: 3 }), 600);
    assert_eq!(price(Ticket::Group(9)), 9000);
    assert_eq!(price(Ticket::Group(10)), 9000);
    assert_eq!(price(Ticket::Group(0)), 0);
    assert_eq!(price(Ticket::Group(1)), 1000);
}

#[test]
fn every_arm_names_its_variant() {
    let src = include_str!("../src/lib.rs");
    assert!(!src.contains("_ =>") && !src.contains("_=>"), "src/lib.rs has a `_` arm");
}

use u02_reuse_1::{price, Ticket};

#[test]
fn adults() {
    assert_eq!(price(Ticket::Adult { age: 30 }), 1200);
    assert_eq!(price(Ticket::Adult { age: 70 }), 800);
}

#[test]
fn children() {
    assert_eq!(price(Ticket::Child { age: 1 }), 0);
    assert_eq!(price(Ticket::Child { age: 8 }), 600);
}

#[test]
fn groups() {
    assert_eq!(price(Ticket::Group(4)), 4000);
    assert_eq!(price(Ticket::Group(12)), 10800);
}

#[test]
fn staff() {
    assert_eq!(price(Ticket::Staff), 0);
}

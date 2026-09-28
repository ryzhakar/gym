use u02_probe_b_p2::{book, Book, Quote};

#[test]
fn each_state_once() {
    assert_eq!(book(Quote::Pair { bid: 101, ask: 100 }), Book::Crossed);
    assert_eq!(book(Quote::Pair { bid: 100, ask: 100 }), Book::Locked);
    assert_eq!(book(Quote::Pair { bid: 99, ask: 100 }), Book::Normal);
    assert_eq!(book(Quote::Halted), Book::Closed);
}

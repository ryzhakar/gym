use u02_probe_b_p2::{book, Book, Quote};

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

fn pair(bid: i64, ask: i64) -> Book {
    book(Quote::Pair { bid, ask })
}

#[test]
fn signature_is_kept() {
    let _: fn(Quote) -> Book = book;
}

#[test]
fn enums_are_kept() {
    fn quote(q: Quote) -> u8 {
        match q {
            Quote::Pair { bid: _, ask: _ } => 0,
            Quote::Halted => 1,
        }
    }
    fn state(b: Book) -> u8 {
        match b {
            Book::Crossed => 0,
            Book::Locked => 1,
            Book::Normal => 2,
            Book::Closed => 3,
        }
    }
    assert_eq!(quote(Quote::Pair { bid: 0i64, ask: 0i64 }), 0);
    assert_eq!(state(Book::Closed), 3);
}

#[test]
fn neighbours() {
    assert_eq!(pair(0, 1), Book::Normal);
    assert_eq!(pair(1, 0), Book::Crossed);
    assert_eq!(pair(-1, -1), Book::Locked);
    assert_eq!(pair(-5, -4), Book::Normal);
}

#[test]
fn extremes() {
    assert_eq!(pair(i64::MIN, i64::MAX), Book::Normal);
    assert_eq!(pair(i64::MAX, i64::MIN), Book::Crossed);
    assert_eq!(pair(i64::MIN, i64::MIN + 1), Book::Normal);
    assert_eq!(pair(i64::MAX, i64::MAX - 1), Book::Crossed);
}

#[test]
fn equal_at_both_extremes() {
    assert_eq!(pair(i64::MIN, i64::MIN), Book::Locked);
    assert_eq!(pair(i64::MAX, i64::MAX), Book::Locked);
}

#[test]
fn no_panicking_arm() {
    let code = code();
    for banned in ["panic!", "unreachable!", "todo!", "unimplemented!"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}

#[test]
fn no_arm_added() {
    let arms = code().matches("=>").count();
    assert!(arms <= 4, "the match has {arms} arms, at most 4 allowed");
}

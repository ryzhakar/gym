pub enum Quote {
    Pair { bid: i64, ask: i64 },
    Halted,
}

#[derive(Debug, PartialEq)]
pub enum Book {
    Crossed,
    Locked,
    Normal,
    Closed,
}

/// The state of the book a quote shows.
pub fn book(quote: Quote) -> Book {
    match quote {
        Quote::Halted => Book::Closed,
        Quote::Pair { bid, ask } if bid > ask => Book::Crossed,
        Quote::Pair { bid, ask } if bid == ask => Book::Locked,
        Quote::Pair { bid, ask } if bid < ask => Book::Normal,
    }
}

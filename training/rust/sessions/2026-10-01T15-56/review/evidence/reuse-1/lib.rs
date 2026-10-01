pub enum Ticket {
    Adult { age: u8 },
    Child { age: u8 },
    Group(u32),
    Staff,
}

/// Price in cents.
pub fn price(t: Ticket) -> u32 {
    match t {
        Ticket::Adult(age: (0..=65)) => 1200,
        Ticket::Adult{_} => 800,
        Ticket::Child(age: ..3) => 0,
        Ticket::Child(_) => 600,
    }
}

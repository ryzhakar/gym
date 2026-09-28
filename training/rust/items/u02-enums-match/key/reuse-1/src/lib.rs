pub enum Ticket {
    Adult { age: u8 },
    Child { age: u8 },
    Group(u32),
    Staff,
}

/// Price in cents.
pub fn price(t: Ticket) -> u32 {
    match t {
        Ticket::Adult { age: 65.. } => 800,
        Ticket::Adult { .. } => 1200,
        Ticket::Child { age: 0..=2 } => 0,
        Ticket::Child { .. } => 600,
        Ticket::Group(0) => 0,
        Ticket::Group(n @ 10..) => n * 900,
        Ticket::Group(n) => n * 1000,
        Ticket::Staff => 0,
    }
}

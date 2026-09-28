pub enum Ticket {
    Adult { age: u8 },
    Child { age: u8 },
    Group(u32),
    Staff,
}

/// Price in cents.
pub fn price(t: Ticket) -> u32 {
    todo!()
}

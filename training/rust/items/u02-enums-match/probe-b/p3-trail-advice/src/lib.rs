pub enum Surface {
    Paved,
    Gravel,
    Ice,
}

pub enum Segment {
    Climb { metres: u32, roped: bool },
    Path(Surface),
    River(u32),
    Closed,
}

#[derive(Debug, PartialEq)]
pub enum Advice {
    Go,
    Caution(u8),
    Stop,
}

/// The advice for one trail segment.
pub fn advise(segment: Segment) -> Advice {
    todo!()
}

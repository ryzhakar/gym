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
    match segment {
        Segment::Climb { metres: 0..=299, .. } => Advice::Go,
        Segment::Climb { metres: 300..=799, .. } => Advice::Caution(2),
        Segment::Climb { roped: true, .. } => Advice::Caution(3),
        Segment::Climb { roped: false, .. } => Advice::Stop,
        Segment::Path(Surface::Paved) => Advice::Go,
        Segment::Path(Surface::Gravel) => Advice::Caution(1),
        Segment::Path(Surface::Ice) => Advice::Stop,
        Segment::River(0..=49) => Advice::Caution(1),
        Segment::River(50..) => Advice::Stop,
        Segment::Closed => Advice::Stop,
    }
}

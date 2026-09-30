pub enum Load {
    Crate { weight: u32, fragile: bool },
    Empty,
}

#[derive(Debug, PartialEq)]
pub enum Handling {
    Careful,
    Normal,
    Skip,
}

/// How to handle a pallet load.
pub fn handling(load: Load) -> Handling {
    match load {
        Load::Crate { weight, .. } if weight > 500 => Handling::Careful,
        Load::Crate { fragile: true, .. } => Handling::Careful,
        Load::Crate { .. } => Handling::Normal,
        Load::Empty => Handling::Skip,
    }
}

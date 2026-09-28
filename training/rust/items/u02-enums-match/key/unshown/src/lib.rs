#[derive(Debug, PartialEq, Clone, Copy)]
pub enum Door {
    Open,
    Closed,
    Locked,
}

#[derive(Debug, Clone, Copy)]
pub enum Action {
    Push,
    Pull,
    Lock,
    Unlock,
}

/// The door's state after `action`.
pub fn next(door: Door, action: Action) -> Door {
    match (door, action) {
        (Door::Closed, Action::Pull) => Door::Open,
        (Door::Open, Action::Push) => Door::Closed,
        (Door::Closed, Action::Lock) => Door::Locked,
        (Door::Locked, Action::Unlock) => Door::Closed,
        (unchanged, _) => unchanged,
    }
}

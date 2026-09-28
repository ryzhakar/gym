// Define `Command` and the five functions. See spec.md.

pub enum Command {
    Dot { x: i32, y: i32 },
    Line { from: (i32, i32), to: (i32, i32) },
    PenUp,
}

pub fn dot(x: i32, y: i32) -> Command {
    Command::Dot { x, y }
}

pub fn line(x1: i32, y1: i32, x2: i32, y2: i32) -> Command {
    Command::Line { from: (x1, y1), to: (x2, y2) }
}

pub fn pen_up() -> Command {
    Command::PenUp
}

pub fn cost(c: Command) -> u32 {
    match c {
        Command::Dot { .. } => 1,
        Command::Line { from, to } if from == to => 1,
        Command::Line { from: (x1, y1), to: (x2, y2) } => x1.abs_diff(x2) + y1.abs_diff(y2),
        Command::PenUp => 0,
    }
}

pub fn endpoint(c: Command) -> Option<(i32, i32)> {
    match c {
        Command::Dot { x, y } => Some((x, y)),
        Command::Line { to, .. } => Some(to),
        Command::PenUp => None,
    }
}

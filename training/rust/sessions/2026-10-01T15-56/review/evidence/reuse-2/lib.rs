// Define `Command` and the five functions. See spec.md.
pub enum Command {
    Dot(i32, i32),
    Line{x1: i32, y1: i32, x2: i32, y2: i32},
    PenUp,
}

pub fn endpoint(c: Command) -> Option<(i32, i32)> {
    match c {
        Command::PenUp => None,
        Command::Dot(x, y) => Some((x, y)),
        Command::Line { x2, y2, .. } => Some((x2, y2)),
    }
}

pub fn cost(c: Command) -> u32 {
    match c {
        Command::PenUp => 0,
        Command::Dot(..) => 1,
        Command::Line { x1, y1, x2, y2} => {
            let x_length: u32 = (x2 - x1).unsigned_abs();
            let y_length = (y2 - y1).unsigned_abs();
            let cost: u32 = std::cmp::max(x_length + y_length, 1);
            cost
        },
    }
}

pub fn dot(x: i32, y: i32) -> Command { Command::Dot(x, y) }
pub fn line(x1: i32, y1: i32, x2: i32, y2: i32) -> Command {Command::Line { x1, y1, x2, y2 }}
pub fn pen_up() -> Command { Command::PenUp }

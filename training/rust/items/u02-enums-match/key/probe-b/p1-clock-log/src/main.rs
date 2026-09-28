enum Clock {
    Move(String),
    Pause,
    Left(i32),
    Side(char),
}

fn describe(event: Clock) -> String {
    match event {
        Clock::Left(s) if s < 10 => format!("hurry {s}"),
        Clock::Left(0) => String::from("flag fell"),
        Clock::Left(s @ 1..=60) => format!("last minute {s}"),
        Clock::Left(s) => format!("{s}s left"),
        Clock::Side('w' | 'W') => String::from("white to move"),
        Clock::Side(c) => format!("side {c}"),
        Clock::Move(m) if m.ends_with('+') => format!("check {m}"),
        Clock::Move(m) => format!("move {m}"),
        Clock::Pause => String::from("paused"),
    }
}

fn main() {
    let events = vec![
        Clock::Left(0),
        Clock::Move(String::from("Nf3")),
        Clock::Left(7),
        Clock::Side('W'),
        Clock::Left(60),
        Clock::Move(String::from("Qxf7+")),
        Clock::Left(-2),
        Clock::Side('b'),
        Clock::Left(61),
        Clock::Pause,
    ];
    for event in events {
        println!("{}", describe(event));
    }
}

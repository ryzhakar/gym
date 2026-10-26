enum Lift {
    Trip { from: i32, to: i32 },
    Door(char),
    Alarm(String),
    Idle,
}

fn describe(event: Lift) -> String {
    match event {
        Lift::Trip { from, to } if from == to => format!("stay at {from}"),
        Lift::Trip { from: 0, to } => format!("lobby to {to}"),
        Lift::Trip { from, to: t @ -3..=-1 } => format!("basement {t} from {from}"),
        Lift::Trip { from, to } if to > from => format!("up {}", to - from),
        Lift::Trip { from, to } => format!("down {}", from - to),
        Lift::Door('o' | 'O') => String::from("doors open"),
        Lift::Door(c) => format!("door signal {c}"),
        Lift::Alarm(msg) if msg.starts_with("FIRE") => format!("evacuate: {msg}"),
        Lift::Alarm(msg) => format!("alarm: {msg}"),
        Lift::Idle => String::from("idle"),
    }
}

fn main() {
    let events = vec![
        Lift::Trip { from: 0, to: 0 },
        Lift::Trip { from: 0, to: 5 },
        Lift::Trip { from: 0, to: -2 },
        Lift::Trip { from: 4, to: -1 },
        Lift::Door('O'),
        Lift::Trip { from: 3, to: 7 },
        Lift::Alarm(String::from("FIRE in shaft")),
        Lift::Trip { from: 9, to: 6 },
        Lift::Alarm(String::from("stuck")),
        Lift::Idle,
    ];
    for event in events {
        println!("{}", describe(event));
    }
}

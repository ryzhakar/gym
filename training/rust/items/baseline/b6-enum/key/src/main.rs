enum Cmd {
    Move { dx: i32, dy: i32 },
    Wait(u32),
    Say(String),
    Quit,
}

fn run(cmd: Cmd) -> String {
    match cmd {
        Cmd::Move { dx: 0, dy: 0 } => "stay".to_string(),
        Cmd::Move { dx, dy } if dx == dy => format!("diagonal {dx}"),
        Cmd::Move { dx, .. } => format!("move {dx}"),
        Cmd::Wait(n @ 1..=3) => format!("short {n}"),
        Cmd::Wait(n) => format!("long {n}"),
        Cmd::Say(text) if text.is_empty() => "silence".to_string(),
        Cmd::Say(text) => format!("say {text}"),
        Cmd::Quit => "bye".to_string(),
    }
}

fn main() {
    let script = vec![
        Cmd::Move { dx: 0, dy: 0 },
        Cmd::Move { dx: 2, dy: 2 },
        Cmd::Move { dx: 0, dy: 5 },
        Cmd::Wait(3),
        Cmd::Wait(0),
        Cmd::Say(String::new()),
        Cmd::Say("hi".to_string()),
        Cmd::Quit,
    ];
    for cmd in script {
        println!("{}", run(cmd));
    }
}

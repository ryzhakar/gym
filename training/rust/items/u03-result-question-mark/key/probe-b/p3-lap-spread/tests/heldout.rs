use u03_probe_b_p3::{spread, LapError, Spread};

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

#[test]
fn no_panic_on_input() {
    let code = code();
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}

#[test]
fn signature_is_kept() {
    let _: fn(&str) -> Result<Spread, LapError> = spread;
}

#[test]
fn types_are_kept() {
    fn variants(e: LapError) -> usize {
        match e {
            LapError::Empty => 0,
            LapError::BadLap { position } => position,
        }
    }
    assert_eq!(variants(LapError::BadLap { position: 7usize }), 7);
    let Spread { fastest, slowest } = Spread { fastest: 1u32, slowest: 2u32 };
    assert_eq!((fastest, slowest), (1, 2));
}

#[test]
fn bad_lap_first() {
    assert_eq!(spread("x;70"), Err(LapError::BadLap { position: 0 }));
}

#[test]
fn bad_lap_last() {
    assert_eq!(spread("70;71;-3"), Err(LapError::BadLap { position: 2 }));
}

#[test]
fn bad_lap_alone() {
    assert_eq!(spread("x"), Err(LapError::BadLap { position: 0 }));
    assert_eq!(spread(";"), Err(LapError::BadLap { position: 0 }));
}

#[test]
fn empty_field_between_separators() {
    assert_eq!(spread("70;;71"), Err(LapError::BadLap { position: 1 }));
}

#[test]
fn first_of_two_bad_laps() {
    assert_eq!(spread("70;a;b"), Err(LapError::BadLap { position: 1 }));
}

#[test]
fn single_lap() {
    assert_eq!(spread("70"), Ok(Spread { fastest: 70, slowest: 70 }));
}

#[test]
fn trailing_separator_ends_the_list() {
    assert_eq!(spread("70;64;"), Ok(Spread { fastest: 64, slowest: 70 }));
}

#[test]
fn extremes() {
    assert_eq!(spread("0;4294967295"), Ok(Spread { fastest: 0, slowest: 4294967295 }));
    assert_eq!(spread("1;4294967296"), Err(LapError::BadLap { position: 1 }));
}

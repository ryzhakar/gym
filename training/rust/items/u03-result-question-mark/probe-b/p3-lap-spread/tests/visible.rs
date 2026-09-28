use u03_probe_b_p3::{spread, LapError, Spread};

#[test]
fn fastest_and_slowest() {
    assert_eq!(spread("71;69;75;70"), Ok(Spread { fastest: 69, slowest: 75 }));
}

#[test]
fn empty_input() {
    assert_eq!(spread(""), Err(LapError::Empty));
}

#[test]
fn bad_lap_in_the_middle() {
    assert_eq!(spread("71;6x;75"), Err(LapError::BadLap { position: 1 }));
}

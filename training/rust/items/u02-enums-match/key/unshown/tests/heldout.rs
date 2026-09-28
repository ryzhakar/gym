use u02_unshown::{next, Action, Door};

#[test]
fn all_twelve_pairs() {
    use Action::*;
    use Door::*;
    let table = [
        (Open, Push, Closed), (Open, Pull, Open), (Open, Lock, Open), (Open, Unlock, Open),
        (Closed, Push, Closed), (Closed, Pull, Open), (Closed, Lock, Locked), (Closed, Unlock, Closed),
        (Locked, Push, Locked), (Locked, Pull, Locked), (Locked, Lock, Locked), (Locked, Unlock, Closed),
    ];
    for (door, action, want) in table {
        assert_eq!(next(door, action), want, "{door:?} + {action:?}");
    }
}

#[test]
fn one_match_no_if() {
    let src = include_str!("../src/lib.rs");
    assert_eq!(src.matches("match ").count(), 1, "`next` needs exactly one `match`");
    assert!(!src.contains("if "), "`next` uses `if`");
}

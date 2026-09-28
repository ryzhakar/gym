use u02_unshown::{next, Action, Door};

#[test]
fn the_four_moves() {
    assert_eq!(next(Door::Closed, Action::Pull), Door::Open);
    assert_eq!(next(Door::Open, Action::Push), Door::Closed);
    assert_eq!(next(Door::Closed, Action::Lock), Door::Locked);
    assert_eq!(next(Door::Locked, Action::Unlock), Door::Closed);
}

#[test]
fn a_locked_door_ignores_pull() {
    assert_eq!(next(Door::Locked, Action::Pull), Door::Locked);
}

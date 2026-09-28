use u02_probe_b_p3::{advise, Advice, Segment, Surface};

#[test]
fn short_climb() {
    assert_eq!(advise(Segment::Climb { metres: 120, roped: false }), Advice::Go);
}

#[test]
fn middle_climb() {
    assert_eq!(advise(Segment::Climb { metres: 500, roped: false }), Advice::Caution(2));
}

#[test]
fn long_climb_unroped() {
    assert_eq!(advise(Segment::Climb { metres: 1200, roped: false }), Advice::Stop);
}

#[test]
fn long_climb_roped() {
    assert_eq!(advise(Segment::Climb { metres: 1200, roped: true }), Advice::Caution(3));
}

#[test]
fn paths() {
    assert_eq!(advise(Segment::Path(Surface::Paved)), Advice::Go);
    assert_eq!(advise(Segment::Path(Surface::Gravel)), Advice::Caution(1));
    assert_eq!(advise(Segment::Path(Surface::Ice)), Advice::Stop);
}

#[test]
fn shallow_river() {
    assert_eq!(advise(Segment::River(20)), Advice::Caution(1));
}

#[test]
fn deep_river() {
    assert_eq!(advise(Segment::River(90)), Advice::Stop);
}

#[test]
fn closed() {
    assert_eq!(advise(Segment::Closed), Advice::Stop);
}

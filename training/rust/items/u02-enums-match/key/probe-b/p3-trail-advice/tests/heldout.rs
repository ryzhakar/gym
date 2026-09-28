use u02_probe_b_p3::{advise, Advice, Segment, Surface};

fn climb(metres: u32, roped: bool) -> Advice {
    advise(Segment::Climb { metres, roped })
}

#[test]
fn signature_is_kept() {
    let _: fn(Segment) -> Advice = advise;
}

#[test]
fn enums_are_kept() {
    fn segment(s: Segment) -> u8 {
        match s {
            Segment::Climb { metres: _, roped: _ } => 0,
            Segment::Path(_) => 1,
            Segment::River(_) => 2,
            Segment::Closed => 3,
        }
    }
    fn surface(s: Surface) -> u8 {
        match s {
            Surface::Paved => 0,
            Surface::Gravel => 1,
            Surface::Ice => 2,
        }
    }
    fn advice(a: Advice) -> u8 {
        match a {
            Advice::Go => 0,
            Advice::Caution(level) => level,
            Advice::Stop => 9,
        }
    }
    assert_eq!(segment(Segment::Climb { metres: 1u32, roped: true }), 0);
    assert_eq!(segment(Segment::River(1u32)), 2);
    assert_eq!(surface(Surface::Ice), 2);
    assert_eq!(advice(Advice::Caution(7u8)), 7);
}

#[test]
fn climb_boundaries_unroped() {
    assert_eq!(climb(0, false), Advice::Go);
    assert_eq!(climb(299, false), Advice::Go);
    assert_eq!(climb(300, false), Advice::Caution(2));
    assert_eq!(climb(799, false), Advice::Caution(2));
    assert_eq!(climb(800, false), Advice::Stop);
    assert_eq!(climb(u32::MAX, false), Advice::Stop);
}

#[test]
fn climb_boundaries_roped() {
    assert_eq!(climb(0, true), Advice::Go);
    assert_eq!(climb(299, true), Advice::Go);
    assert_eq!(climb(300, true), Advice::Caution(2));
    assert_eq!(climb(799, true), Advice::Caution(2));
    assert_eq!(climb(800, true), Advice::Caution(3));
    assert_eq!(climb(u32::MAX, true), Advice::Caution(3));
}

#[test]
fn river_boundaries() {
    assert_eq!(advise(Segment::River(0)), Advice::Caution(1));
    assert_eq!(advise(Segment::River(49)), Advice::Caution(1));
    assert_eq!(advise(Segment::River(50)), Advice::Stop);
    assert_eq!(advise(Segment::River(u32::MAX)), Advice::Stop);
}
